from f_parser import parse
from context import Context


class Expression:
    def __init__(self, data: str, ctx: Context):
        self.args = []
        self.is_monomial = False
        self.variables = []
        self.type, self.value, arg1, arg2 = parse(data)
        if self.type == 'func':
            for arg in (arg1, arg2):
                self.__get_args(arg, self.value, ctx)
        elif self.type == 'symbol':
            expr = ctx.get_func_from_list(self.value)
            if expr != -1:
                self.args = expr.args
                self.value = expr.value
                self.type = expr.type
                self.is_monomial = expr.is_monomial
                self.variables = expr.variables
            else:
                self.variables.append([self.value, 1])
                self.value = 1
                self.is_monomial = True
        else:
            self.is_monomial = True

    def __get_args(self, data, op, ctx):
        _, arg_value, arg1, arg2 = parse(data)
        if arg_value == op:
            for arg in (arg1, arg2):
                self.__get_args(arg, arg_value, ctx)
        else:
            self.args.append(Expression(data, ctx))

    def make_monomial(self):
        count = 0
        if self.value == '*':
            return -1
        for arg in self.args:
            if arg.type != 'func' or arg.value == '^':
                count += 1
        if count == len(self.args):
            self.value = self.args[0].value
            for arg in self.args:
                if arg.value == '^':
                    self.variables.append([arg.args[0], arg.args[1]])
                elif arg.type == 'symbol':
                    self.variables.append([arg.value, 1])
            self.variables.sort()
            self.args = []
            self.is_monomial = True
            return 0
        else:
            return -1

    def __str__(self):
        math_str = ''
        if self.is_monomial:
            if not (self.value == 1 and len(self.variables) != 0):
                math_str += str(self.value)
            for var in self.variables:
                math_str += var[0]
                if var[1] != 1:
                    math_str += ('^' + str(var[1]))
        elif self.type == "func":
            for expr in self.args:
                if len(math_str) != 0:
                    math_str += (' ' + str(self.value) + ' ')
                math_str += expr.__str__()
        else:
            math_str += str(self.value)
        return math_str
