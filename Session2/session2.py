class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def conversion(self, o):
        if self.scale == o.scale:
            return o
        elif self.scale == "C":
            if o.scale == "F":
                return Temperature((o.value - 32) * 5/9, "C")
            elif o.scale == "K":
                return Temperature((o.value - 273.15), "C")
        elif self.scale == "K":
            if o.scale == "F":
                return Temperature(((o.value - 32) * 5/9) + 273.15, "K")
            elif o.scale == "C":
                return Temperature(o.value + 273.15, "K")
        elif self.scale == "F":
            if o.scale == "C":
                return Temperature((o.value * 9/5) + 32, "F")
            elif o.scale == "K":
                return Temperature(((o.value - 273.15) * 9/5) + 32, "F")

    def add(self, o):
        if round(self.value + o.value, 4) != 0:
            return Temperature(round(self.value + o.value, 4), self.scale)
        else:
            raise BaseException("This cannot result in 0")

    def substract(self, o):
        if round(self.value - o.value, 4) != 0:
            return Temperature(round(self.value - o.value, 4), self.scale)
        else:
            raise BaseException("This cannot result in 0")

    def multiply(self, o):
        if round(self.value * o.value, 4) != 0:
            return Temperature(round(self.value * o.value, 4), self.scale)
        else:
            raise BaseException("This cannot result in 0")

    def divide(self, o):
        if round(self.value / o.value, 4) != 0 and o.value != 0:
            return Temperature(round(self.value / o.value, 4), self.scale)
        elif o.value == 0:
            raise ZeroDivisionError
        else:
            raise BaseException("This cannot result in 0")