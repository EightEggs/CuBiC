from Processing import str_parser as sp
import twophase.solver as sv

cubestring = 'UUFFUUBRLDRUFRULLFUDBBFLRDDDLFBDURDRBRLBLLDDFLFRBBRUFB'
res = sv.solve(cubestring, 20, 0.2)
solvelist = sp.solvestring_parser(res, True)
print(solvelist)
oplist= sp.to_oplist(solvelist, True)
print(oplist)
