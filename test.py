from Processing import str_parser as sp
import twophase.solver as sv

cubestring = 'UUFFUUBRLDRUFRULLFUDBBFLRDDDLFBDURDRBRLBLLDDFLFRBBRUFB'
res = sv.solve(cubestring, 20, 0.2)
solvestring = sp.solvestring_parser(res, True)
print(solvestring)
opstring = sp.to_opstring(solvestring, True)
print(opstring)