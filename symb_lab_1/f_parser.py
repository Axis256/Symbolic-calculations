def parse(input_expr: str):

    __viable_functions = [
        'add',
        'sub',
        'mul',
        'div',
        'pow',
        'simplify'
    ]

    __func_dict = {
        'add': '+',
        'sub': '-',
        'mul': '*',
        'div': '/',
        'pow': '^'
    }

    def is_func(text: str):
        pos = text.find('(')
        if pos == -1 or text[0:pos] not in __viable_functions or text[-1] != ')':
            return False
        else:
            return True

    def find_comma(text: str):
        pos_par = text.find('(')
        pos = text.find(',')
        if pos_par != -1 and pos_par < pos:
            par_open = 1
            i = pos_par
            while par_open != 0:
                i += 1
                if text[i] == '(':
                    par_open += 1
                if text[i] == ')':
                    par_open -= 1
            pos = i + 1
        else:
            pos = text.find(',')
        first_arg = text[0:pos]
        second_arg = text[pos + 2:]
        if pos != -1 and (is_func(first_arg) or first_arg.isalnum()) and (is_func(second_arg) or second_arg.isalnum()):
            return pos
        else:
            return -1

    if is_func(input_expr):
        pos_par = input_expr.find('(')
        args = input_expr[pos_par + 1:-1]
        comma_pos = find_comma(args)
        if comma_pos != -1:
            arg1 = args[0:comma_pos]
            arg2 = args[comma_pos + 2:]
            return 'func', __func_dict[input_expr[0:pos_par]], arg1, arg2
        elif input_expr[0:pos_par] == 'simplify':
            return 'symp', args, None, None
        else:
            return -1
    elif input_expr.isnumeric():
        return 'value', int(input_expr), None, None
    elif input_expr.isalnum():
        return 'symbol', input_expr, None, None
