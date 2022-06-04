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


def solvestring_parser(solvestring: str, including_count: bool = False) -> list:
    '''parse the solvestring to a list containing each solution step.
    :param solvestring: the solvestring to parse.
    :param including_count: set to True if you want to show the step counts.
    '''
    solvelist = solvestring.split()
    if including_count:
        solvelist[-1] = solvelist[-1][1:3]
    else:
        solvelist.pop()
    return solvelist


def to_oplist(solvestring: list, including_count: bool = False) -> list:
    '''generate the operation string list from the solvestring list.
    :param solvestring: the solvestring list to parse.
    '''
    # 定义初始方位，左手为L，右手为F
    state = ['F', 'B', 'L', 'R', 'U', 'D']
    oplist = []
    for i in range(len(solvestring)):
        step = solvestring[i]
        if step[0] == state[0]:  # 空间位置：前，直接操作右手
            oplist.append('F'+step[1])
            # print(state)
        if step[0] == state[2]:  # 空间位置：左，直接操作左手
            oplist.append('L'+step[1])
            # print(state)
        elif step[0] == state[4]:  # 空间位置：上，先转到右手
            oplist.append('LL')
            oplist.append('F'+step[1])
            # 更新state
            state[0], state[5] = state[5], state[0]
            state[1], state[4] = state[4], state[1]
            state[0], state[1] = state[1], state[0]
            # print(state)
        elif step[0] == state[5]:  # 空间位置：下，先转到左手
            oplist.append('FF')
            oplist.append('L'+step[1])
            # 更新state
            state[2], state[5] = state[5], state[2]
            state[3], state[4] = state[4], state[3]
            state[4], state[5] = state[5], state[4]
            # print(state)
        elif step[0] == state[1]:  # 空间位置：后，先转到右手
            oplist.append('LL2')
            oplist.append('F'+step[1])
            # 更新state
            state[0], state[1] = state[1], state[0]
            state[5], state[4] = state[4], state[5]
            # print(state)
        elif step[0] == state[3]:  # 空间位置：右，先转到左手
            oplist.append('FF2')
            oplist.append('L'+step[1])
            # 更新state
            state[2], state[3] = state[3], state[2]
            state[5], state[4] = state[4], state[5]
            # print(state)
        else:
            pass
            # raise ValueError("Unknown solve step.")
    if including_count:
        oplist.append(len(oplist))
    return oplist


if __name__ == "__main__":

    cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
    if valid_cubestring(cubestring):
        res = sv.solve(cubestring, 30, 1)

    print(valid_cubestring(cubestring))
    print(solvestring_parser(res, True))
