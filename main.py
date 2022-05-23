# Create a temperature class
# Create the conversion method
# Create the operation methods
# Work in the main part
# Test methods

class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def conversion(self, obj): # The second object scale changes into the first one's
        if self.scale == obj.scale:  # Checks if both are the same scale
            return obj
        elif self.scale == "K":  # Checks if main object is Kelvin
            if obj.scale == "C":  # Checks if secondary object is Celcius
                obj.scale = "K"
                obj.value += 273.15
                return obj
            elif obj.scale == "F": # Checks if secondary object is Fahrenheit
                obj.scale = "K"
                obj.value = ((obj.value - 32) * 5/9) + 273.15
                return obj
        elif self.scale == "C":  # Checks if main object is Celcius
            if obj.scale == "K":  # Checks if secondary object is Kelvin
                obj.scale = "C"
                obj.value -= 273.15
                return obj
            elif obj.scale == "F":  # Checks if secondary object is Fahrenheit
                obj.scale = "C"
                obj.value = (obj.value - 32) * 5/9
                return obj
        elif self.scale == "F":  # Checks if main object is Fahrenheit
            if obj.scale == "C":  # Checks if secondary object is Celcius
                obj.scale = "F"
                obj.value = (obj.value * 9/5) + 32
                return obj
            elif obj.scale == "K":  # Checks if secondary object is Kelvin
                obj.scale = "F"
                obj.value = ((obj.value - 273.15) * 9/5) + 32
                return obj

    def add(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(round((self.value + obj.value), 4), self.scale)
        if temp.value == 0:
            raise Exception("It cannot result in 0")
        return temp

    def substract(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(round((self.value - obj.value), 4), self.scale)
        if temp.value == 0:
            raise Exception("It cannot result in 0")
        return temp

    def multiply(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(round((self.value * obj.value), 4), self. scale)
        if temp.value == 0:
            raise Exception("It cannot result in 0")
        return temp

    def divide(self, obj):
        if obj.value != 0:
            obj = Temperature.conversion(self, obj)
            temp = Temperature(round((self.value / obj.value), 4), self.scale)
        else:
             raise ZeroDivisionError
        return temp


def main():
    t1 = Temperature(294.78, 'K')
    t2 = Temperature(168.16, "F")

    t3 = t1.substract(t2)

    print(t3.value, t3.scale)


# main()