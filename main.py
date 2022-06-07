import Vision.capture as capture
import Vision.svm as svm
import Processing.str_parser as sp
import Control.stp_control as sc


def main(lhand, rhand, oplist):
    for i in range(len(oplist)):
        if oplist[i] == 'L1':
            lhand.TurnR90()
        if oplist[i] == 'L2':
            lhand.Turn180()
        if oplist[i] == 'L3':
            lhand.TurnL90()
        if oplist[i] == 'F1':
            rhand.TurnR90()
        if oplist[i] == 'F2':
            rhand.Turn180()
        if oplist[i] == 'F3':
            rhand.TurnL90()
        if oplist[i] == 'LL':
            lhand.Release().TurnR90()
        if oplist[i] == 'LL2':
            lhand.Release().Turn180()
        if oplist[i] == 'FF':
            rhand.Release().TurnR90()
        if oplist[i] == 'FF2':
            rhand.Release().Turn180()


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
