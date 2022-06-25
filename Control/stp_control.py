from curses.ascii import DEL
from enum import Enum, unique
import time
import pigpio


# pigpio uses BCM encoding.
HandL_ENA = 4
HandL_DIR = 22
HandL_PUL = 17

HandR_ENA = 25
HandR_DIR = 18
HandR_PUL = 24

MagnetL_GPIO = 13
MagnetR_GPIO = 6

NUM_OF_STEPS_FOR_360 = 1000
PWM_FREQ = 1440  # Hz
DELAY = int(500000/PWM_FREQ)  # microseconds


@unique
class HandStatus(Enum):
    '''Enum class of hand status.
    '''

    DeftHld = 0
    DeftRel = 1
    LeftHld = 2
    LeftRel = 3
    BackHld = 4
    BackRel = 5
    RighHld = 6
    RighRel = 7


class Hand:
    '''Hand class
    '''
    # constrain the attributes
    __slots__ = ('status', 'side', 'pi', 'wavel', 'waver', 't180', 'wave_id')

    def __init__(self, side: str, status: HandStatus = HandStatus.DeftRel):
        if isinstance(status, HandStatus) and side in ('left', 'right'):
            self.status = status
            self.side = side
            self.t180 = True

            self.pi = pigpio.pi()
            if not self.pi.connected:
                raise RuntimeError("Connect to pigpio failed!")
            self.pi.wave_clear()
            self.pi.write(HandL_ENA, 0)
            self.pi.set_mode(HandL_PUL, pigpio.OUTPUT)
            self.pi.set_mode(HandR_PUL, pigpio.OUTPUT)
            self.wavel = [pigpio.pulse(1 << HandL_PUL, 0, DELAY),
                          pigpio.pulse(0, 1 << HandL_PUL, DELAY)]
            self.waver = [pigpio.pulse(1 << HandR_PUL, 0, DELAY),
                          pigpio.pulse(0, 1 << HandR_PUL, DELAY)]

        else:
            raise ValueError("Unknown param(s).")

    @staticmethod
    def _value2key(value: int) -> HandStatus:
        '''Get the HandStatus name via value.
        :param value: value of the HandStatus
        '''
        for v in HandStatus._member_map_.items():
            if v[1].value == value:
                return v[1]

    def set_status(self, status: HandStatus):
        '''Set the HandStatus name via name.
        :param status: name of the HandStatus:
        DeftHld | LeftHld | LeftRel | BackHld | BackRel | RighHld | RighRel
        '''
        if isinstance(status, HandStatus):
            self.status = status
        else:
            raise ValueError(f"Invalid status {status}")

    def _send_pulse(self, num_of_pulse: int):
        '''Send the pulse to the hand.
        :param num_of_pulses: number of pulses to send
        '''
        x = num_of_pulse & 255
        y = num_of_pulse >> 8
        # loop x + y*256 times
        chain = [255, 0, self.wave_id, 255, 1, x, y]
        # infinite loop (for test):
        # chain = [255, 0, self.wave_id, 255, 3]
        print(chain)
        while self.pi.wave_tx_busy():
            time.sleep(0.1)
        self.pi.wave_chain(chain)
        while self.pi.wave_tx_busy():
            time.sleep(0.1)
        self.pi.wave_tx_stop()


    def _move(self, angle: int, direct: int):
        '''Move the specified angle.
        :param angle: angle to move to
        :param direct: direction to move, 0 == left, 1 == right
        '''
        self.pi.wave_add_generic(self.wavel if self.side=='left' else self.waver)
        self.wave_id = self.pi.wave_create()
        #if self.wave_id >= 0:
            #print(f"Wave {self.wave_id} created successfully.")
        num_of_pulse = int(angle * NUM_OF_STEPS_FOR_360/360)
        if 0 < angle < 360 and direct in (0, 1):
            self.pi.write(HandL_DIR if self.side ==
                          "left" else HandR_DIR, direct)
            self._send_pulse(num_of_pulse)
        else:
            raise ValueError(f"Invalid angle {angle} or direction {direct}!")

    def Hold(self):
        if self.status.value in [1, 3, 5, 7]:
            self.status = Hand._value2key(self.status.value - 1)
            self.pi.write(MagnetL_GPIO if self.side ==
                          'left' else MagnetR_GPIO, 0)
            time.sleep(0.3)
            return self
        else:
            raise ValueError(
                f"{self.status} already holds.")

    def Release(self):
        if self.status.value in [0, 2, 4, 6]:
            self.status = self._value2key(self.status.value + 1)
            self.pi.write(MagnetL_GPIO if self.side ==
                          'left' else MagnetR_GPIO, 1)
            time.sleep(0.3)
            return self


    def TurnL90(self):
        v = [2, 3, 4, 5, 6, 7, 0, 1][self.status.value]
        self.status = Hand._value2key(v)
        self._move(90, 1)
        time.sleep(0.2)
        return self

    def TurnR90(self):
        v = [6, 7, 0, 1, 2, 3, 4, 5][self.status.value]
        self.status = Hand._value2key(v)
        self._move(90, 0)
        time.sleep(0.2)
        return self

    def Turn180(self):
        v = [4, 5, 6, 7, 0, 1, 2, 3][self.status.value]
        self.status = Hand._value2key(v)
        self._move(180, 0) if self.t180 else self._move(180, 1)
        self.t180 = not self.t180
        time.sleep(0.4)
        return self

    def __del__(self):
        self.pi = pigpio.pi()
        self.pi.wave_tx_stop()
        self.pi.wave_clear()
        self.pi.stop()


if __name__ == '__main__':
    lhand = Hand(side='left')
    rhand = Hand(side='right')
    lhand.Hold()
    rhand.Hold()
    rhand.TurnL90()
    rhand.TurnR90()
    lhand.TurnL90()
    lhand.TurnR90()
    time.sleep(1)
    lhand.Release()
    rhand.Release()