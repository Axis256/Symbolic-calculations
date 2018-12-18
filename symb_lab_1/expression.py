class Expression:
    def __init__(self, data):
        self.args = []
        self.value = data["value"]
        self.type = data["exprType"]
        self.is_monomial = False
        self.variables = []
        if self.type == "binary":
            self.__get_args(data, data["value"])
        elif self.type == 'symbol':
            self.value = 1
            self.variables.append([data["value"], 1])
            self.is_monomial = True
        else:
            self.value = data["value"]
            self.is_monomial = True

    def __get_args(self, data, operator):
        if data["left"]["exprType"] == "binary" and data["left"]["value"] == operator:
            self.__get_args(data["left"], operator)
        else:
            self.args.append(Expression(data["left"]))
        if data["right"]["exprType"] == "binary" and data["right"]["value"] == operator:
            self.__get_args(data["right"], operator)
        else:
            self.args.append(Expression(data["right"]))

    def make_monomial(self):
        count = 0
        if self.value == '*':
            return -1
        for arg in self.args:
            if arg.type != 'binary' or arg.value == '^':
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

    def make_str(self):
        math_str = ''
        if self.type == "binary":
            for expr in self.args:
                if self.value != '*' and len(math_str) != 0:
                    math_str += (' ' + str(self.value) + ' ')
                math_str += expr.make_str()
        else:
            math_str += str(self.value)
        return math_str
