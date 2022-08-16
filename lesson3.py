#               задание к уроку № 1


time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
second = time - (hours * 3600 + minutes * 60)
print(f"время в формате чч:мм:сс  {hours} : {minutes} : {second}")

#               задание №1 к уроку 3

def div(s_1, s_2):
    try:
        s_1, s_2 = int (s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return round(div_num, 4)

print(div(input("введите первое число: - "), input("введите второе число: - ")))

def calculator(a, b):
   try:
       return a/b
   except ZeroDivisionError as e:
       print(f'Ошибка! Делить на ноль нельзя')


print(calculator(int(input('Первое число: ')), int(input('Второе число: '))))


#            задание № 2

def personal_info(** kwargs):
    return  ' '.join(kwargs.values())

print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
                    birthday=input("Enter your birthday: "), city=input("Enter yor city: "),
                    mail=input("Enter yor email: "),

phonep_number=input("Enter yor phonep_number: ")))


             задание № 3

def my_func(num_1, num_2, num_3):
    try:
        my_list = list(map(float, [num_1,num_2, num_3]))
        my_list.remove(min(my_list))
        return sum(my_list)
    except (TypeError, ValueError):
        return "enter only a numbers!"

    print(my_func(input(), input(), input()))


def my_func(arg1, arg2, arg3):
    return sum(sorted([arg1, arg2, arg3])[1:])
print(my_func(1978, 1, 2))

#              задание № 4

def my_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return  "Enter a float number and a negative power"
    return res

print(my_pow_fun(4.5, -2))

def i_involve_r(x, y):
    return 1 if y == 0 else i_involve_r(x, y + 1) *1 / x
x = 2
y = -4
print(i_involve_r(x, y))


#              адание №5


def sum_num():
    s =0
    while True:
        err = False
      in_list = input("Enter a number , input 'q' to exit: ").split()
       for num in in_list:
            if num.lower() == "q":
                return  s
           else:
                try:
                    s += int(num)
                except ValueError:
                   err = True
       if err:
            print("The data is incorrect!")
       print(f"sum of numbers = {s}")
print(sum_num())




#                         задание №6


def int_func(word):
    latin_char = 'vbhgfcdsertyioplljgfdsazcbm'
    return word.title()if not set(word).difference(latin_char) else False
words = input('Введите строку из слов разделенных пробелом: ').split()
for w in words:

    result = int_func(w)
    if result:
        print(result, ' ')



















