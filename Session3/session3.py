class Temperature:
    def __init__(self, value, scale):  # Class constructor
        self.value = value
        self.scale = scale

    def conversion(self, o):
        if self.scale == o.scale:  # Checks if both scales are the same
            return o
        elif self.scale == "C" and o.scale == "F":  # Checks if main scale is Celsius and secondary scale is Fahrenheit
            return Temperature((o.value - 32) * 5/9, self.scale)
        elif self.scale == "C" and o.scale == "K":  # Checks if main scale is Celsius and secondary scale is Kelvin
            return Temperature(o.value - 273.15, self.scale)
        elif self.scale == "F" and o.scale == "C":  # Checks if main scale is Fahrenheit and secondary scale is Celsius
            return Temperature((o.value * 9/5) + 32, self.scale)
        elif self.scale == "F" and o.scale == "K":  # Checks if main scale is Fahrenheit and secondary scale is Kelvin
            return Temperature(((o.value - 273.15) * 9/5) + 32, self.scale)
        elif self.scale == "K" and o.scale == "C":  # Checks if main scale is Kelvin and secondary scale is Celsius
            return Temperature(o.value + 273.15, self.scale)
        elif self.scale == "K" and o.scale == "F":  # Checks if main scale is Kelvin and secondary scale is Fahrenheit
            return Temperature(((o.value - 32) * 5/9) + 273.15, self.scale)

    def addition(self, o):
        o = self.conversion(o)  # Conversion method call
        if round(self.value + o.value, 4) != 0:
            return Temperature(round(self.value + o.value, 4), self.scale)
        else:
            raise ValueError

    def subtraction(self, o):  
        o = self.conversion(o)  # Conversion method call
        if round(self.value - o.value, 4) != 0:
            return Temperature(round(self.value - o.value, 4), self.scale)
        else:
            raise ValueError

    def multiplication(self, o):  
        o = self.conversion(o)  # Conversion method call
        if round(self.value * o.value, 4) != 0:
            return Temperature(round(self.value * o.value, 4), self.scale)
        else:
            raise ValueError

    def division(self, o):
        o = self.conversion(o)  # Conversion method call 
        if round(self.value / o.value, 4) != 0:
            return Temperature(round(self.value / o.value, 4), self.scale)
        elif self.value == 0 or o.value == 0:  # Checks if any of the dividends is 0
            raise ZeroDivisionError
        else:
            raise ValueError

