class PizzaComponent:
    '''
    Abstract pizza component. Determines the methods that a component must have.
    '''
    def get_description(self):
        return self.__class__.__name__

    def get_total_cost(self):
        return self.__class__.cost
    
class PizzaTray(PizzaComponent):
    '''
    The base component for the pizza, must be included in every pizza that is made.
    '''
    cost = 0.0

class Decorator(PizzaComponent):
    '''
    Generic pizza component that implements the methods of the abstract class.
    Makes it so that the implementation has a recursive characteristic, which allows
    it to have all the components for the pizza.
    '''    
    def __init__(self, pizza_component):
        self.component = pizza_component

    def get_total_cost(self):
        return self.component.get_total_cost() + PizzaComponent.get_total_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + PizzaComponent.get_description(self)


# Pizza components
class Pepperoni(Decorator):
    cost = 5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Cheese(Decorator):
    cost = 2
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Catupiry(Decorator):
    cost = 4
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Chicken(Decorator):
    cost = 8
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Chocolate(Decorator):
    cost = 10
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)
    
class CondensedMilk(Decorator):
    cost = 8
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

# Sample tests
pepperoni_pizza = Pepperoni(Cheese(PizzaTray()))
print(pepperoni_pizza.get_description(), ": $", str(pepperoni_pizza.get_total_cost()))

chicken_catupiry_pizza = Chicken(Catupiry(PizzaTray()))
print(chicken_catupiry_pizza.get_description(), ": $", str(chicken_catupiry_pizza.get_total_cost()))


sweet_pizza = Chocolate(CondensedMilk(PizzaTray()))
print(sweet_pizza.get_description(), ": $", str(sweet_pizza.get_total_cost()))