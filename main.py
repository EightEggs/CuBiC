import Vision.capture as capture
import Vision.svm as svm
import Processing.str_parser as sp
import Control.stp_control as sc


def main(lhand, rhand, oplist):
    '''
    !!! WARNING: This function has NOT been tested yet.
    '''
    for i in range(len(oplist)):
        if oplist[i] == 'L1':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release().TurnR90().Hold()
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release().TurnL90().Hold()
            lhand.TurnR90()
        if oplist[i] == 'L2':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release().TurnR90().Hold()
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release().TurnL90().Hold()
            lhand.Turn180()
        if oplist[i] == 'L3':
            if rhand.status == sc.HandStatus.LeftHld:
                rhand.Release().TurnR90().Hold()
            if rhand.status == sc.HandStatus.RighHld:
                rhand.Release().TurnL90().Hold()
            lhand.TurnL90()
        if oplist[i] == 'F1':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release().TurnR90().Hold()
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release().TurnL90().Hold()
            rhand.TurnR90()
        if oplist[i] == 'F2':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release().TurnR90().Hold()
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release().TurnL90().Hold()
            rhand.Turn180()
        if oplist[i] == 'F3':
            if lhand.status == sc.HandStatus.LeftHld:
                lhand.Release().TurnR90().Hold()
            if lhand.status == sc.HandStatus.RighHld:
                lhand.Release().TurnL90().Hold()
            rhand.TurnL90()
        if oplist[i] == 'LL':
            rhand.Release()
            lhand.TurnR90()
            rhand.Hold()
        if oplist[i] == 'LL2':
            rhand.Release()
            lhand.Turn180()
            rhand.Hold()
        if oplist[i] == 'FF':
            lhand.Release()
            rhand.TurnR90()
            lhand.Hold()
        if oplist[i] == 'FF2':
            lhand.Release()
            rhand.Turn180()
            lhand.Hold()


if __name__ == '__main__':
    capture.capture_all()
    cubestring = svm.color_detect("/home/pi/...")

    if sp.valid_cubestring(cubestring):
        solvestring = sp.sv.solve(cubestring)
        solvelist = sp.solvestring_parser(solvestring)
        oplist = sp.to_oplist(solvelist)
        print(oplist)

    lhand = sc.Hand('left')
    rhand = sc.Hand('right')

    main(lhand, rhand, oplist)
