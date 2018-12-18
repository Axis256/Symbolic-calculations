from expression import *


class Monominal:
    def __init__(self, expr: Expression):
        self.coefficient = expr.args[0]
        self.variables = []
        for i in range(1, len(expr.args)):
            if expr.args[i].type == 'symbol':
                self.variables.append((expr.args[i].value, 1))
            else:
                self.variables.append((expr.args[i].args[0].value, expr.args[i].args[0].value))
        self.variables.sort()

def sum_monoms(monom_1: Monominal, monom_2: Monominal):
    monom_1.coefficient += monom_2.coefficient
    return(monom_1)


def mul_monoms(*monoms: Monominal):
    for monom in monoms:
        pass
