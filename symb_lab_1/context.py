from expression import Expression


class Context:
    def __init__(self):

        self._user_functions = []

    def add_func(self, symb: str, expr: Expression):
        self._user_functions.append((symb, expr))
