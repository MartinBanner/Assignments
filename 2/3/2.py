# -*- coding: UTF-8 -*-



def print_string(*args, sep=' ', end='\n'):
    ls = []
    result = ''

    ls = [str(arg) for arg in args]
    result = sep.join(ls) + end

    return result



print(print_string('This is a test') == 'This is a test\n')
print(print_string('This', 'is', 'a', 'test') == 'This is a test\n')
print(print_string('This', 'is', 'a', 'test', sep = '-') == 'This-is-a-test\n')
print(print_string('This', 'is', 'a', 'test', ',', 'Yes', sep = '_', end = '.') == 'This_is_a_test_,_Yes.')
