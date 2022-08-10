def greet(name):
    return "Привет, " + name
name = "Олег"
print(f"{greet(name)}")


name = "Pythonru"
type_of_site = "Блог"
print(f"{name} это {type_of_site}.")


import  random
a = random.randint(1, 100)
print(a)
if a > 50:
   print("Big")
else:
    print("Small")


a = "hello"
b = "world"
print(f"{a}, {b}")
num_1 = int(input("enter any number: "))
num_2 = int(input("enter any number one more time: "))
print(f"You have chosen the numbers {num_1} and {num_2}")
word = input("enter any word: ")
print(f"{word} - it's good choice")

time = int(input("введите число в секундах:"))
Hours = time // 3600
minutes = time // 60 - hours * 60
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")



n = input("enter an integer: ")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")


def solve(n):
    n1 = int(n)
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
print("n1 + n2 + n3")
solve(5)


n = input("enter an integer: ")


while n < '0':
    print("I've asked for numbergreater than 0! please try again!")
   n = input('please enter numbergreater than 0: ')


num_init = int(input("введите целое полжительное число: "))
greatest_dig = 0
num = num_init

while num >0:
    digit =num % 10
    if digit > greatest_dig:
        greatest_dig = digit
       if greatest_dig == 9:
           break
    num =num // 10

    print(f"наибольшая цифра в числе {num_init} равна {greatest_dig}")


revenue = float(input("Введите значение выручки (тугрики) - "))
costs = float(input("ведите значение издержек (тугрики) - "))
result = revenue - costs
if result > 0:
    print(f"поздравляю! Ваша компания работает с прибылью {result} тугриков!")
    print(f"Рентабельность выручки составила {100 * (result / costs):.1f}%")
    personal_n = int(input("сколько счастливых людей работает в вашей компании? " ))
    print(f"Если вы раздадите прибыль компании сотрудникам, то каждый получит по {result / personal_n:.3f} тугриков.")
elif result < 0:
   print(f"Увы, ваша компания работает с убытком {-result} тугриков")
else:
    print(f"ноль - это тоже хороший результат")





























