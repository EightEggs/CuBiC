from enum import Enum, unique


@unique
class HandStatus(Enum):
    '''Enum class of motor status.
    '''

    Default = 0
    LeftHld = 1
    LeftRel = 2
    BackHld = 3
    BackRel = 4
    RighHld = 5
    RighRel = 6


class Motor:
    '''Motor class
    '''

    def __init__(self):
        self.status = HandStatus.Default

    def set_status(self, status: HandStatus):
        if status in HandStatus:
            self.status = status
        else:
            raise ValueError(f"Invalid status {status}")


if __name__ == '__main__':
    lm = Motor()
    lm.set_status(HandStatus.RighRel)
    print(lm.status)
