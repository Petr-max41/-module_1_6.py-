my_dict = {'Petr': 1983, 'Maxsim': 2007, 'Ivan': 2015 }
print(my_dict)
print(my_dict['Petr'])
print(my_dict.get('Masha'))
my_dict.update({'Alena': 1983, 'Dima': 1986})
print(my_dict)
i = (my_dict.pop('Petr'))
print(i)
print(my_dict)
my_set = {2,3,4,2,4,3,'ключ','замок','ключ','замок'}
print(my_set)
my_set.add(8)
my_set.add(9)
my_set.discard(4)
print(my_set)