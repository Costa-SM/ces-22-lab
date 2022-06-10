from abc import ABC, abstractmethod

class Baker():
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder

    def bakeCake(self):
        print('A cake with the following characteristics is being baked:')
        self.__builder.getType()
        self.__builder.getStyle()
        self.__builder.getTopping()

class CakeBuilder(ABC):
    '''
    The CakeBuilder specifies methods for creating different
    types of cakes.
    '''

    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def getStyle(self):
        pass

    @abstractmethod
    def getTopping(self):
        pass

class Cake1Builder(CakeBuilder):
    '''
    This concrete builder makes chocolate cakes, with a birthday
    party style, and a chocolate topping.
    '''
    def getType(self):
        print('This cake is has a chocolate type.')

    def getStyle(self):
        print('This cake is has a birthday party style.')

    def getTopping(self):
        print('This cake is has a chocolate topping.')

class Cake2Builder(CakeBuilder):
    '''
    This concrete builder makes carrot cakes, with a wedding
    party style, and a vanilla topping.
    '''
    def getType(self):
        print('This cake is has a carrot type.')

    def getStyle(self):
        print('This cake is has a wedding party style.')

    def getTopping(self):
        print('This cake is has a vanilla topping.')



new_director = Baker()
chocolate_builder = Cake1Builder()
vanilla_builder = Cake2Builder()

new_director.setBuilder(chocolate_builder)
new_director.bakeCake()

new_director.setBuilder(vanilla_builder)
new_director.bakeCake()