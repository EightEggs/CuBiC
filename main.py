import Vision.capture as capture
import Vision.recognition as recog
import Processing.str_parser as sp
import Control.stp_control as sc


def main(lhand, rhand, oplist):
    for i in range(len(oplist)):
        if oplist[i] == 'L1':
            pass


if __name__ == '__main__':
    capture.capture_all()
    cubestring = recog.recognize("/home/pi/...")

    if sp.valid_cubestring(cubestring):
        solvestring = sp.sv.solve(cubestring)
        solvelist = sp.solvestring_parser(solvestring)
        oplist = sp.to_oplist(solvelist)
        print(oplist)

    lhand = sc.Hand('left')
    rhand = sc.Hand('right')

    main(lhand, rhand, oplist)
