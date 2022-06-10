class FirstParent():
    # Base class
    def __init__(self):
        print('First parent !')

class SecondParent():
    # Base class
    def __init__(self):
        print('Second parent !')

class ThirdParent(SecondParent):
    # Inherits SecondParent's methods
    def __init__(self):
        super().__init__()
        print('Third parent, after the second parent !')

class UselessParent(ThirdParent):
    def __init__(self):
        # A "ghost" class that serves only as a means to
        # use super() to call the init functions of both
        # its parents, which, in this case, are the 
        # SecondParent and ThirdParent classes.

        # Thus, by calling super() on this class, the 
        # interpreter will call the init function for
        # SecondParent and ThirdParent, respectively

        super().__init__()

class DerivedClass(FirstParent, UselessParent):
    def __init__(self):
        # Call super for the first parent passed to the
        # derived class
        super().__init__()
        # Call super searching for an init function in a 
        # class "above" the UselessParent.
        super(UselessParent, self).__init__()

# Thus, by using the UselessParent class, we get the 
# correct output, which is the first, second, and third
# parent classes' output, when initializing an object from
# the DerivedClass.
DerivedClass()
