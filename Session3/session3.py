class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def conversion(self, o):
        if self.scale == o.scale:
            return o
        elif self.scale == "C" and o.scale == "F":
            return Temperature((o.value - 32) * 5/9, self.scale)
        elif self.scale == "C" and o.scale == "K":
            return Temperature(o.value - 273.15, self.scale)
        elif self.scale == "F" and o.scale == "C":
            return Temperature((o.value * 9/5) + 32, self.scale)
        elif self.scale == "F" and o.scale == "K":
            return Temperature(((o.value - 273.15) * 9/5) + 32, self.scale)
        elif self.scale == "K" and o.scale == "C":
            return Temperature(o.value + 273.15, self.scale)
        elif self.scale == "K" and o.scale == "F":
            return Temperature(((o.value - 32) * 5/9) + 273.15, self.scale)

    def add(self, o):
        o = self.conversion(o)
        if round(self.value + o.value, 4) != 0:
            return Temperature(round(self.value + o.value, 4), self.scale)
        else:
            raise ValueError

    def substraction(self, o):
        o = self.conversion(o)
        if round(self.value - o.value, 4) != 0:
            return Temperature(round(self.value - o.value, 4), self.scale)
        else:
            raise ValueError

    def multiply(self, o):
        o = self.conversion(o)
        if round(self.value * o.value, 4) != 0:
            return Temperature(round(self.value * o.value, 4), self.scale)
        else:
            raise ValueError

    def division(self, o):
        o = self.conversion(o)
        if round(self.value / o.value, 4) != 0:
            return Temperature(round(self.value / o.value, 4), self.scale)
        elif self.value == 0 or o.value == 0:
            raise ZeroDivisionError
        else:
            raise ValueError

