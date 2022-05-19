from enum import Enum, unique
import pigpio

pi = pigpio.pi()
if not pi.connected:
    pass
    # exit("pigpiod is not connected")

HandL_GPIO = 1
HandR_GPIO = 2
MagnetL_GPIO = 3
MagnetR_GPIO = 4


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

    def __init__(self):
        self.status = HandStatus.DeftHld

    def _value2key(self, value: int) -> HandStatus:
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
        if status in HandStatus:
            self.status = status
        else:
            raise ValueError(f"Invalid status {status}")

    def Hold(self):
        if self.status.value in [1, 3, 5, 7]:
            self.status = self._value2key(self.status.value - 1)
        else:
            raise ValueError(
                f"{self.status} already holds.")

    def Release(self):
        if self.status.value in [0, 2, 4, 6]:
            self.status = self._value2key(self.status.value + 1)
        else:
            raise ValueError(
                f"{self.status} already released.")

    def TurnL90(self):
        pass

    def TurnR90(self):
        pass

    def Turn180(self):
        pass


if __name__ == '__main__':
    lm = Hand()
    print(lm.status)
    lm.set_status(HandStatus.RighRel)
    print(lm.status)
    lm.Hold()
    print(lm.status)
    lm.Release()
    print(lm.status)
