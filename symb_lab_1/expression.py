class Expression:
    def __init__(self, data):
        self.args = []
        self.value = data["value"]
        self.type = data["exprType"]
        if self.type == "binary":
            self.__get_args(data, data["value"])
        else:
            self.value = data["value"]

    def __get_args(self, data, operator):
        if data["left"]["exprType"] == "binary" and data["left"]["value"] == operator:
            self.__get_args(data["left"], operator)
        else:
            self.args.append(Expression(data["left"]))
        if data["right"]["exprType"] == "binary" and data["right"]["value"] == operator:
            self.__get_args(data["right"], operator)
        else:
            self.args.append(Expression(data["right"]))
