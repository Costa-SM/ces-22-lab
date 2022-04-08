# Example decorator

def sample_decorator(function, arguments, dictionary):
    print('Decorate the ', function, ' function')
    function(arguments, dictionary)
    print('Function ', function, ' has been decorated.')

def sample_function(argument_list, key_dictionary):
    element_str = ''
    for element in argument_list:
        element_str += str(element) + ' '
    print('List elements: ', element_str)

    print('Dictionary keys and values')
    for key in key_dictionary:
        print(key, key_dictionary[key])

arguments = [1, 2, 3, 4, 5]
dictionary= {'apple': 5, 'banana': 4}

sample_decorator(sample_function, arguments, dictionary)