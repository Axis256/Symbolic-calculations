def simplify_add(expr):
    temp_list = []
    for i in range(len(expr.args)):
        if expr.args[i] != -1:
            temp_list.append(expr.args[i])
            if expr.args[i].is_monomial:
                for j in range(i + 1, len(expr.args)):
                    if (expr.args[j].variables == temp_list[-1].variables) and expr.args[j].is_monomial:
                        temp_list[-1].value += expr.args[j].value
                        expr.args[j] = -1
    expr.args = temp_list
    reduce(expr)


def simplify_mul(expr):
    var_exists = False
    expr.value = 1
    for arg in expr.args:
        if arg.is_monomial:
            expr.value *= arg.value
            if len(arg.variables) != 0:
                for var_out in arg.variables:
                    for var_in in expr.variables:
                        if len(var_in) != 0 and var_out[0] == var_in[0]:
                            var_in[1] += var_out[1]
                            var_exists = True
                            break
                    if not var_exists:
                        expr.variables.append(var_out)
    expr.is_monomial = True
    expr.args = []
    if len(expr.variables) > 0:
        expr.type = 'symbol'
    else:
        expr.type = 'value'


def simplify_pow(expr):
    if expr.args[0].type == 'value':
        expr.value = expr.args[0].value ** expr.args[1].value
        expr.type = 'value'
        expr.args = []
        expr.is_monomial = True
    if expr.args[0].type == 'symbol':
        for var in expr.args[0].variables:
            var[1] *= expr.args[1].value
        expr.value = expr.args[0].value ** expr.args[1].value
        expr.variables = expr.args[0].variables
        expr.type = 'symbol'
        expr.is_monomial = True
        expr.args = []


def reduce(expr):
    if len(expr.args) == 1:
        expr.value = expr.args[0].value
        expr.type = expr.args[0].type
        expr.variables = expr.args[0].variables
        expr.is_monomial = expr.args[0].is_monomial
        expr.args = expr.args[0].args
        return 0
    else:
        return -1


def simplify(expr):
    for arg in expr.args:
        if arg.type == 'func':
            simplify(arg)
    if expr.value == '+':
        simplify_add(expr)
    elif expr.value == '*':
        simplify_mul(expr)
    elif expr.value == '^':
        simplify_pow(expr)
