import re

#Ввод символів
row=input("\nВведіть слова та числа: ")

#Виведення введених символів
print("\nВведені символи ", row)

extract_letter=" ".join(re.split("[0-9]+", row))
extract_number="".join(re.split("[a-zA-Z]+", row))
 
extract_com_let=", ".join(extract_letter.split())
extract_com_num=", ".join(extract_number.split())

# Виведення введених чисел
print("\nВсі числа: ", str(extract_com_num))

#Виведення введених слів
print("\nВсі слова ", str(extract_com_let))



for let in extract_letter.split():
    print("\nВиведення слів з першими та останніми великими буквами ", let[0].upper() + let[1:-1].lower() + let[-1].upper(), end="\n")

new_num_max=list(map(int, extract_number.split()))

max_num=max(new_num_max)

# Функція заходження та виведення максимального значення
print("\nМаксимальне значення ", max_num)
for element in new_num_max:
    if element != max_num:
        element=element**new_num_max.index(element)
        print("\nЧисла піднесені до кореня їх індексу ", element)
    else:
        continue
