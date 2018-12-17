from expression import Expression


def find_matching_values(expr: Expression):
    pass


def s_multiplication(expr: Expression):
    pass


def simplify_add(expr: Expression):
    dump_index = -1
    for i in range(len(expr.args)):
        if expr.args[i].type == 'value':
            dump_index = i
            break
    if dump_index == -1:
        return -1
    for i in range(len(expr.args)):
        if expr.args[i].type == 'value' and i != dump_index:
            expr.args[dump_index] += expr.args[i]
    reduce(expr)
    return 0


def simplify_mul(expr: Expression):
    for i in range(len(expr.args)):
        if expr.args[i].value == '^' and expr.args[i].args[0].type == 'value':
            expr.args[i].args = [ expr.args[i].args[0].value ** expr.args[i].args[1].value ]
            reduce(expr.args[i])


def reduce(expr: Expression):
    if len(expr.args) == 1:
        expr.value = expr.args[0].value
        expr.type = expr.args[0].type
        expr.args = []
        return 0
    else:
        return -1
