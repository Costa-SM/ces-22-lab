# Create examples that illustrate the difference between abstract methods,
# static methods, class methods and instance methods.

class Sandwich(object):
    def __init__(self, length):
        self.ingredients = []
        self.length = length

    # Static Method
    # A static method does not depend on the class or its variables
    @staticmethod
    def mix_ingredients(x, y):
        # This method does not use the Sandwich object.
        return x + y

    # Instance Method
    # You can use the class's variables in these methods
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients

    def get_length(self):
        return self.length

    # Class Method
    # You can create another object of the same class using a class method
    @classmethod
    def new_sandwich(cls, size):
        return cls(size)    

# An abstract class
class Bread():
    # Abstract Method
    # These methods should be implemented in abstract classes, and so, will
    # never be used directly.
    def bake_sandwich(self):
        pass
