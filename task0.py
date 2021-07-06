import random
#Виведення списку та кількість чисел цього ж списку
random_list = [random.randrange(-100,100) for i in range(30)]
print("\nList => ", random_list)
#Максимальне число
max_element = max(random_list)
#Пошук порядкового номеру цього числа
position = random_list.index(max_element)
print("\nMax => ", max_element, "\n№ => ", position + 1)
new_list=[]
#Функція непарних чисел
for element in random_list:
    if (element % 2) == 1:
        new_list.append(element)
if len(new_list) == 0:
  print("\nThe list has no odd numbers")
else:
#Виведення списку непарних чисел
  new_list.sort(reverse=True)
  print("\nList of odd numbers =>", new_list)
