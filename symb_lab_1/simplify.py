from expression_old import Expression


def simplify_add(expr: Expression):
    temp_list = []
    for i in range(len(expr.args)):
        if isinstance(expr.args[i], Expression) and expr.args[i].is_monomial:
            temp_list.append(expr.args[i])
            for j in range(i + 1, len(expr.args)):
                if expr.args[j].variables == temp_list[-1].variables:
                    temp_list[-1].value += expr.args[j].value
                    expr.args[j] = False
    expr.args = temp_list
    reduce(expr)


def simplify_mul(expr: Expression):
    var_exists = False
    expr.value = 1
    for arg in expr.args:
        if isinstance(arg, Expression) and arg.is_monomial:
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


def reduce(expr: Expression):
    if len(expr.args) == 1:
        expr.value = expr.args[0].value
        expr.type = expr.args[0].type
        expr.variables = expr.args[0].variables
        expr.is_monomial = expr.args[0].is_monomial
        expr.args = expr.args[0].args
        return 0
    else:
        return -1
