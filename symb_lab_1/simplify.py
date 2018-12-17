from expression import Expression


def simplify_add(expr: Expression):
    temp_list = [0]
    for i in range(len(expr.args)):
        if expr.args[i].type == 'value':
            temp_list[0] += expr.args[i]
        else:
            temp_list.append(expr.args[i])
    expr.args = temp_list
    reduce(expr)


def simplify_mul(expr: Expression):
    temp_list = [1]
    for i in range(len(expr.args)):
        if expr.args[i].type == 'value':
            temp_list[0] += expr.args[i]
        elif expr.args[i].type == 'symbol':
            temp_list.append(expr.args[i])
    for i in range(len(expr.args)):
        if expr.args[i].type == 'binary':
            temp_list.append(expr.args[i])
    expr.args = temp_list
    # dump_index = -1
    # for i in range(len(expr.args)):
    #     if expr.args[i].value == '^' and expr.args[i].args[0].type == 'value':
    #         expr.args[i].args = [expr.args[i].args[0].value ** expr.args[i].args[1].value]
    #         reduce(expr.args[i])
    #     if expr.args[i].type == 'value':
    #         dump_index = i
    #         break
    # if dump_index == -1:
    #     return -1
    # for i in range(dump_index, len(expr.args)):
    #     if expr.args[i].type == 'value' and i != dump_index:
    #         expr.args[dump_index] += expr.args[i]
    reduce(expr)


def reduce(expr: Expression):
    if len(expr.args) == 1:
        expr.value = expr.args[0].value
        expr.type = expr.args[0].type
        expr.args = []
        return 0
    else:
        return -1
