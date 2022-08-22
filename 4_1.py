
         задание 1

from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Salary - {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers. Not string or empty character.")


salary()
    задание 2
from random import randint

original_list = [randint(0, 1000) for _ in range(0, randint(2,20))]
answer_list = [num for i, num in enumerate(original_list[1:]) if num > original_list[i]]

print(original_list)
print(answer_list)


    задание 3

uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

        задание 4


from random import randint
my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(f"source list\n{my_list}\nNo repetition list\n{uniq_list}")

         задание 5

def fact_gen(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1



for el in fact_gen(int(input('Factorial number: '))):
    print(el)


       задание 6


from itertools import count, cycle

my_count = count(7)
my_cycle = cycle("ABC")
for _ in range(5):
    print("(my_count, my cycle) = ({},{})".format(next(my_count), next(my_cycle)))


content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')
my_file = open('test.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('test.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()
