from expression import *
from input_json import make_data

data = make_data("data_file.json")
expr = Expression(data)
#print(expr.args[0].args[1].value, expr.args[0].value)

def is_eq(expr1: Expression, expr2: Expression):

    match_count = 0

    if len(expr1.args) != len(expr2.args):
        return False

    for item1 in expr1.args:
        if item1.type == 'value':
            continue
        for item2 in expr2.args:
            if (item1.type == item2.type == 'symbol') and (item1.value == item2.value) or \
                                    (item1.type == item2.type == 'binary') and \
                                    (item1.value == item2.value == 'pow') and (item1.args == item2.args):
                match_count += 1
                break
    print(match_count)
    print(len(expr1.args))
    if match_count + 1 == len(expr1.args):
        return True
    else:
        return False


expr1 = Expression(data)
expr2 = Expression(data)
#print(expr1.args[0].value == expr2.args[0].value)

print(is_eq(Expression(data['left']), Expression(data['left'])))