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
        if self.scale == obj.scale:
            return obj
        elif self.scale == "K":
            if obj.scale == "C":
                obj.scale = "K"
                obj.value += 273.15
                return obj
            elif obj.scale == "F":
                obj.scale = "K"
                obj.value = ((obj.value - 32) * 5/9) + 273.15
                return obj
        elif self.scale == "C":
            if obj.scale == "K":
                obj.scale = "C"
                obj.value -= 273.15
                return obj
            elif obj.scale == "F":
                obj.scale = "C"
                obj.value = (obj.value - 32) * 5/9
                return obj
        elif self.scale == "F":
            if obj.scale == "C":
                obj.scale = "F"
                obj.value = (obj.value * 9/5) + 32
                return obj
            elif obj.scale == "K":
                obj.scale = "F"
                obj.value = ((obj.value - 273.15) * 9/5) + 32
                return obj

    def add(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(self.value + obj.value, self.scale)
        return temp

    def substract(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(self.value - obj.value, self.scale)
        return temp

    def multiply(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(self.value * obj.value, self. scale)
        return temp

    def divide(self, obj):
        obj = Temperature.conversion(self, obj)
        temp = Temperature(self.value / obj.value, self.scale)
        return temp


def main():
    t1 = Temperature(294.78, 'K')
    t2 = Temperature(168.16, "F")

    t3 = t1.substract(t2)

    print(t3.value, t3.scale)


main()