
#================================
#          mymath module
#================================

def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def division(x, y):
    return x / y

def multiplication(x, y):
    return x * y

class MyMathClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self, x, y):
        return x / y
