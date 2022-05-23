# Create a temperature class
# Create the conversion method
# Create the operation methods
# Test methods
# Work in the main part

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
