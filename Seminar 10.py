# Даны два списка из чисел. Найдите все числа, которые входят как в первый, так и во второй список, и выведите их в порядке возрастания.
 
def random_list(n):
    from random import randint
    some_list=[]
    for i in range(n):
        some_list.append(randint(0,10))
    return some_list

lst1=random_list(7)
lst2=random_list(7)
print(f'Первый список: {lst1}')
print(f'Второй список: {lst2}')
result=set(lst1).intersection(set(lst2))
print(sorted(list(result)))