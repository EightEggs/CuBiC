from enum import Enum, unique
import time
import pigpio


# pigpio uses BCM encoding.
HandL_ENA = 1
HandL_DIR = 3
HandL_PUL = 5

HandR_ENA = 2
HandR_DIR = 4
HandR_PUL = 6

MagnetL_GPIO = 7
MagnetR_GPIO = 8

NUM_OF_STEPS_FOR_360 = 2000
PWM_FREQ = 5000  # Hz
DELAY = 500000/PWM_FREQ  # microseconds


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
    __slots__ = ('status', 'side', 'pi', 'wave', 'wave_id')

    def __init__(self, side: str, status: HandStatus = HandStatus.DeftHld):
        if isinstance(status, HandStatus) and side in ('left', 'right'):
            self.status = status
            self.side = side

            self.pi = pigpio.pi()
            if not self.pi.connected:
                pass
                # raise RuntimeError("Connect to pigpio failed!")
            self.pi.wave_clear()
            self.pi.set_mode(HandL_ENA if side ==
                             'left' else HandL_ENA, pigpio.OUTPUT)
            self.pi.set_mode(HandL_DIR if side ==
                             'left' else HandR_DIR, pigpio.OUTPUT)
            self.wave = [pigpio.pulse(1 << HandL_PUL if side ==
                                      'left' else HandR_PUL, 0, DELAY),
                         pigpio.pulse(0, 1 << HandL_PUL if side ==
                                      'left' else HandR_PUL, DELAY)]
            self.pi.wave_add_generic(self.wave)
            self.wave_id = self.pi.wave_create()
            if self.wave_id >= 0:
                print(f"Wave {self.wave_id} created successfully.")

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
        # loop x + y*256
        chain = [255, 0, self.wave_id, 255, 1, x, y]
        while self.pi.wave_tx_busy():
            time.sleep(0.1)
        self.pi.wave_chain(chain)

    def _move(self, angle: int, direct: int):
        '''Move the specified angle.
        :param angle: angle to move to
        :param direct: direction to move, 0 == left, 1 == right
        '''
        num_of_pulse = int(angle * NUM_OF_STEPS_FOR_360/360)
        if 0 < angle < 360 and direct in (0, 1):
            self.pi.write(HandL_DIR if self.side == "left" else HandR_DIR, direct)
            self._send_pulse(num_of_pulse)
        else:
            raise ValueError(f"Invalid angle {angle} or direction {direct}!")

    def Hold(self):
        if self.status.value in [1, 3, 5, 7]:
            self.status = Hand._value2key(self.status.value - 1)
            self.pi.write(MagnetL_GPIO if self.side ==
                          'left' else MagnetR_GPIO, 0)
            return self
        else:
            raise ValueError(
                f"{self.status} already holds.")

    def Release(self):
        if self.status.value in [0, 2, 4, 6]:
            self.status = self._value2key(self.status.value + 1)
            self.pi.write(MagnetL_GPIO if self.side ==
                          'left' else MagnetR_GPIO, 1)
            return self
        else:
            raise ValueError(
                f"{self.status} already released.")

    def TurnL90(self):
        v = [2, 3, 4, 5, 6, 7, 0, 1][self.status.value]
        self.status = Hand._value2key(v)
        self._move(90, 0)
        return self

    def TurnR90(self):
        v = [6, 7, 0, 1, 2, 3, 4, 5][self.status.value]
        self.status = Hand._value2key(v)
        self._move(90, 1)
        return self

    def Turn180(self):
        v = [4, 5, 6, 7, 0, 1, 2, 3][self.status.value]
        self.status = Hand._value2key(v)
        self._move(180, 0) if self.status.value % 2 else self._move(180, 1)
        return self


if __name__ == '__main__':
    lhand = Hand(side='left')
    rhand = Hand(side='right')
