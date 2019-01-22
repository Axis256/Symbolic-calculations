# from input_json import make_data
from expression import *
from out_fancy import success_message

# data = make_data("data_file.json")
# expr = Expression(data)
# print(expr.args[0].args[1].value, expr.args[0].value)

ctx = Context()
expr_in = 0
while expr_in != '0':
    expr_in = input()
    eq_pos = expr_in.find('=')
    if eq_pos == -1:
        print(Expression(expr_in, ctx))
        # success_message()
    else:
        ctx.add_func(expr_in[0:eq_pos - 1], Expression(expr_in[eq_pos + 2:], ctx))

# success_message()
# expr = Expression('add(mul(mul(2, 3), mul(mul(1, 6), 9)), pow(y, 2))', ctx)
# print(expr)
# simplify(expr)
# print(expr)
#
# simplify_mul(expr.args[0])
# print(expr)

# expr1 = Expression(data)
# for arg in expr1.args:
#     print(arg.make_monomial())
# print(expr1.args[0].is_monomial)

# simplify_mul(expr1)
# print(expr1.value)
# print(expr1.variables)
# print(expr1)
# ctx = Context()
# print(ctx.parse('smth(wtf niggas)'))


# expr2 = Expression(data['right'])

# print(expr1.args[0].value == expr2.args[0].value)
#
# print(is_eq(Expression(data['left']), Expression(data['left'])))
# print(expr1.make_monomial())
# print(expr1.variables)
# print(expr1.value)
