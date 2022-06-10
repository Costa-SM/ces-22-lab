# Model of a bakery using the abstract factory design pattern.
from abc import ABC, abstractmethod

class CakeFactory(ABC):
    '''
    Creates an abstract cake.
    Cakes have a type, a style and a topping.
    '''

    @abstractmethod
    def bake_cake(self):
        pass

    @abstractmethod
    def set_topping(self):
        pass

    @abstractmethod
    def set_style(self):
        pass


class ChocolateCakeFactory(CakeFactory):
    '''
    A chocolate cake, which implements the Cake class methods.
    '''

    def bake_cake(self):
         print('A chocolate cake with the style', self.style, 'and topping', self.topping, 'has been baked!')
        
    def set_style(self, style):
        self.style = style
    
    def set_topping(self, topping):
        self.topping = topping
    
    
class CarrotCakeFactory(CakeFactory):
    '''
    A carrot cake, which implements the Cake class methods.
    '''
    
    def bake_cake(self):
         print('A carrot cake with the style', self.style, 'and topping', self.topping, 'has been baked!')
        
    def set_style(self, style):
        self.style = style
    
    def set_topping(self, topping):
        self.topping = topping

    

class VanillaCakeFactory(CakeFactory):
    '''
    A vanilla cake, which implements the Cake class methods.
    '''

    def bake_cake(self):
         print('A vanilla cake with the style', self.style, 'and topping', self.topping, 'has been baked!')
        
    def set_style(self, style):
        self.style = style
    
    def set_topping(self, topping):
        self.topping = topping

cakes = [ChocolateCakeFactory(), CarrotCakeFactory(), VanillaCakeFactory()]

for cake in cakes:
    cake.set_style('wedding party')
    cake.set_topping('confetti')
    cake.bake_cake()