import twophase.solver as sv
import twophase.face as face
import twophase.cubie as cubie


def valid_cubestring(cubestring: str) -> bool:
    '''check if the given cubestring is valid.
    :param cubestring: the cubestring to check.
    '''
    fc = face.FaceCube()
    sfc = fc.from_string(cubestring)
    cc = fc.to_cubie_cube()
    scc = cc.verify()
    # TODO: indicate where the fault is.
    if sfc == cubie.CUBE_OK and scc == cubie.CUBE_OK:
        return True
    return False


def solvestring_parser(solvestring: str, including_count: bool = False) -> dict:
    '''parse the solvestring to a dict containing each solution step.
    :param solvestring: the solvestring to parse.
    :param including_count: set to True if you want to show the step counts.
    '''
    solvedict = solvestring.split()
    if including_count:
        solvedict[-1] = solvedict[-1][1:3]
    else:
        solvedict.pop()
    return solvedict


if __name__ == "__main__":

    cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
    if valid_cubestring(cubestring):
        res = sv.solve(cubestring, 30, 1)

    print(valid_cubestring(cubestring))
    print(solvestring_parser(res, True))

