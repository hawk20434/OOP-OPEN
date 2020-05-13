
def dec_method(method_to_dec):
    def foo(self, other):
        obg3 = method_to_dec(self, other)
        print(f'({self.x},{self.y}) + ({other.x},{other.y}) = ({obg3.x},{obg3.x})')
    return foo


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    @dec_method
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


obg1 = Vector(4, 9)
obg2 = Vector(1, 6)
obg3 = obg1 + obg2
