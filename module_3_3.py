print('____Функция с параметрами по умолчанию:____')
def print_params(a=1, b='now', c=56.878):
    print(a, b, c)


print_params()
print_params(123)
print_params(25, c=45)
print_params(b=25)
print_params(c=[1, 2, 3])

print('________Распаковка параметров:_________')

values_list = [4, 'Tree', True]
values_dict = {'a': 56.67, 'b': 9, 'c': 'rang'}
print_params(*values_list)
print_params(**values_dict)

print('____Распаковка + отдельные параметры_____')

values_list_2 = ['num_', 34]
print_params(*values_list_2, 42)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
