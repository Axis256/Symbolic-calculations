import json

class Expression:
    def __init__(self, data, parent = None):
        self.parent: Expression =  parent
        self.exp_type = data['expType']
        self.value = data['value']
        if self.exp_type == 'symbol' or self.exp_type == 'value':
            self.left = self.right = None
        else:
            self.left = Expression(data['left'], self)
            self.right = Expression(data['right'], self)


with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

fun = Expression(data)
print(fun.left.left.parent.left.value)