import Vision.capture as capture
import Vision.svm as svm
import Processing.str_parser as sp
import Control.stp_control as sc
import time


DELAY = 0


def delay(delay_time: float):
    time.sleep(delay_time)


def main(lhand, rhand, oplist):
    '''
    !!! WARNING: This function has NOT been tested yet.
    '''
    for i in range(len(oplist)):
        if oplist[i] == 'L1':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release()
                rhand.TurnR90()
                rhand.Hold()
                delay(DELAY)
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release()
                rhand.TurnL90()
                rhand.Hold()
                delay(DELAY)
            lhand.TurnR90()
            delay(DELAY)
        if oplist[i] == 'L2':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release()
                rhand.TurnR90()
                rhand.Hold()
                delay(DELAY)
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release()
                rhand.TurnL90()
                rhand.Hold()
                delay(DELAY)
            lhand.Turn180()
            delay(DELAY)
        if oplist[i] == 'L3':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release()
                rhand.TurnR90()
                rhand.Hold()
                delay(DELAY)
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release()
                rhand.TurnL90()
                rhand.Hold()
                delay(DELAY)
            lhand.TurnL90()
            delay(DELAY)
        if oplist[i] == 'F1':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release()
                lhand.TurnR90()
                lhand.Hold()
                delay(DELAY)
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release()
                lhand.TurnL90()
                lhand.Hold()
                delay(DELAY)
            rhand.TurnR90()
            delay(DELAY)
        if oplist[i] == 'F2':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release()
                lhand.TurnR90()
                lhand.Hold()
                delay(DELAY)
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release()
                lhand.TurnL90()
                lhand.Hold()
                delay(DELAY)
            rhand.Turn180()
            delay(DELAY)
        if oplist[i] == 'F3':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release()
                lhand.TurnR90()
                lhand.Hold()
                delay(DELAY)
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release()
                lhand.TurnL90()
                lhand.Hold()
                delay(DELAY)
            rhand.TurnL90()
            delay(DELAY)
        if oplist[i] == 'LL':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release()
                rhand.TurnR90()
                rhand.Hold()
                delay(DELAY)
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release()
                rhand.TurnL90()
                rhand.Hold()
                delay(DELAY)
            rhand.Release()
            lhand.TurnR90()
            rhand.Hold()
            delay(DELAY)
        if oplist[i] == 'LL2':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release()
                rhand.TurnR90()
                rhand.Hold()
                delay(DELAY)
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release()
                rhand.TurnL90()
                rhand.Hold()
                delay(DELAY)
            rhand.Release()
            lhand.Turn180()
            rhand.Hold()
            delay(DELAY)
        if oplist[i] == 'FF':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release()
                lhand.TurnR90()
                lhand.Hold()
                delay(DELAY)
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release()
                lhand.TurnL90()
                lhand.Hold()
                delay(DELAY)
            lhand.Release()
            rhand.TurnR90()
            lhand.Hold()
            delay(DELAY)
        if oplist[i] == 'FF2':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release()
                lhand.TurnR90()
                lhand.Hold()
                delay(DELAY)
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release()
                lhand.TurnL90()
                lhand.Hold()
                delay(DELAY)
            lhand.Release()
            rhand.Turn180()
            lhand.Hold()
            delay(DELAY)


if __name__ == '__main__':
    # capture.capture_all()
    # cubestring = svm.color_detect("/home/pi/...")
    cubestring = 'DDDDUDDDDRRRRRRRRRBBBBFBBBBUUUUDUUUULLLLLLLLLFFFFBFFFF'
    if sp.valid_cubestring(cubestring):
        solvestring = sp.sv.solve(cubestring)
        solvelist = sp.solvestring_parser(solvestring)
        oplist = sp.to_oplist(solvelist)
        print(oplist)

    lhand = sc.Hand('left')
    rhand = sc.Hand('right')
    lhand.Hold()
    rhand.Hold()
    delay(1)
    main(lhand, rhand, oplist)
    lhand.Release()
    rhand.Release()
