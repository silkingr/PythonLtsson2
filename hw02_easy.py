# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("------Задача 1--------")
fruits = ["яблоко", "банан", "киви", "арбуз"]
print('fruits = ',fruits)
i = 0
while len(fruits) > i:
    print(i+1,'.', '{0:>10}'.format(fruits[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print ("-----------Задача 2-----------")
first_list = [1, 2, 3, 'ddd', 45, 't']
second_list = [2,'ddd']
print ('first_list = ',first_list)
print ('second_list = ',second_list)
i = 0
while len(first_list) > i:
    if first_list[i] in second_list:
        # first_list[i] = Nont   #Удаляем значение элемента, не изменяя длины и структуры списка first_list
        del first_list[i]
    i += 1
print ('Обновленный first_list = ',first_list)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


print ("-----------Задача 3-----------")
list = [2, 34, 445, 1, 3, 237, 56]
print(list)
i = 0
while len(list) > i:
    if list[i]%2:
        list[i]=list[i]*2
    else:
        list[i]=list[i]/4
    i += 1
print(list)