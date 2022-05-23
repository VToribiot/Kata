class Temperature:
    def __init__(self, value, scale):
        self.value = value  # Numerical Value
        self.scale = scale  # Scales being C -> Celcius, K -> Kelvin and F -> Fahrenheit

    def conversion(self, o):
        if self.scale == o.scale:  # Checks if both scales are the same
            return o
        elif self.scale == "Cº":  # If main scale is Celcius
            if o.scale == "Fº":  # If secondary scale is Fahrenheit
                return Temperature((o.value - 32) * 5/9, "Cº")
            elif o.scale == "Kº":  # If secondary scale is Kelvin
                return Temperature((o.value - 273.15), "Cº")
        elif self.scale == "Kº":  # If main scale is Kelvin
            if o.scale == "Fº":  # If secondary scale is Fahrenheit
                return Temperature(((o.value - 32) * 5/9) + 273.15, "Kº")
            elif o.scale == "Cº":  # If secondary scale is Celcius
                return Temperature(o.value + 273.15, "Kº")
        elif self.scale == "Fº":  # If main scale is Fahrenheit
            if o.scale == "Cº":  # If secondary scale is Celcius
                return Temperature((o.value * 9/5) + 32, "Fº")
            elif o.scale == "Kº":  # If secondary scale is Kelvin
                return Temperature(((o.value - 273.15) * 9/5) + 32, "Fº")

    def add(self, o):
        o = self.conversion(o)  # Conversion method invocation
        if round(self.value + o.value, 4) != 0:
            return Temperature(round(self.value + o.value, 4), self.scale)  # Resultant Object
        else:
            raise ValueError

    def substract(self, o):
        o = self.conversion(o)  # Conversion method invocation
        if round(self.value - o.value, 4) != 0:
            return Temperature(round(self.value - o.value, 4), self.scale)  # Resultant Object
        else:
            raise ValueError

    def multiply(self, o):
        o = self.conversion(o)  # Conversion method invocation
        if self.value * o.value != 0:
            return Temperature(round((self.value * o.value), 4), self.scale)  # Resultant Object
        else:
            raise ValueError

    def divide(self, o):
        o = self.conversion(o)  # Conversion method invocation
        if round(self.value / o.value, 4) != 0 and o.value != 0:
            return Temperature(round((self.value / o.value), 4), self.scale)  # Resultant Object
        elif round(o.value, 4) == 0 or round(self.value, 4) == 0:
            raise ZeroDivisionError
        else:
            raise ValueError