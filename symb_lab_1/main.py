# from input_json import make_data
from expression import *
from out_fancy import success_message
from my_plot import plot
import numpy as np

# data = make_data("data_file.json")
# expr = Expression(data)
# print(expr.args[0].args[1].value, expr.args[0].value)

ctx = Context()
expr_in = 0
while expr_in != '0':
    expr_in = input()
    eq_pos = expr_in.find('=')
    if eq_pos == -1:
        if expr_in[0:4] == 'plot':
            pos_par = expr_in.find('(')
            pos_comma1 = expr_in.find(',')
            pos_comma2 = expr_in.find(',', pos_comma1 + 1)
            pos_comma3 = expr_in.find(',', pos_comma2 + 1)
            pos_comma4 = expr_in.find(',', pos_comma3 + 1)
            expr_str = expr_in[pos_par + 1:pos_comma1]
            x = expr_in[pos_comma1 + 2:pos_comma2]
            x = np.linspace(int(x[0:x.find(':')]), int(x[x.find(':') + 1:]), 100)
            y = expr_in[pos_comma2 + 2:pos_comma3]
            y = np.linspace(int(y[0:y.find(':')]), int(y[y.find(':') + 1:]), 100)
            X, Y = np.meshgrid(x, y)
            var1 = expr_in[pos_comma3 + 2:pos_comma4]
            var2 = expr_in[pos_comma4 + 2:expr_in.find(')')]
            expr = Expression(expr_str, ctx)
            simplify(expr)
            plot(expr, X, Y, var1, var2)
        else:
            expr = Expression(expr_in, ctx)
            print(expr)
            # success_message()
    else:
        ctx.add_func(expr_in[0:eq_pos - 1], expr_in[eq_pos + 2:])

# expr = Expression('mul(pow(10, 2), pow(z, 11))', ctx)
# expr2 = Expression('mul(pow(x, 4), pow(y, 2))', ctx)
# simplify(expr)
# simplify(expr2)
# print(expr)
# print(expr2)
# expr = expr * expr2
# simplify(expr)
# print(expr)

# expr = Expression('add(add(y, mul(x, 6)), 5)', ctx)
# simplify(expr)
# x = np.linspace(1, 10, 10)
# y = np.linspace(1, 10, 10)
# X, Y = np.meshgrid(x, y)
# print(expr, X, Y, 'x', 'y')
# plot(expr, X, Y, 'x', 'y')

#print(expr.substitute(X, Y, 'x', 'y'))

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
