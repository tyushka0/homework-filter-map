from functools import reduce

numbers = [5,12,7,20,3,18,2,15,9,30,11,6]
text = 'Напишите генератор который возвращает слова строки по одному тест три два один'
def greater_than_ten(num_list):
    for n in num_list:
        if n > 10:
            yield n
print(f'(1)Числа списка {numbers}, которые больше 10')
gtt = greater_than_ten(numbers)
for _ in range(6):
    print(next(gtt))

print('-'*100)


def square_numbers(num_list):
    for n in num_list:
        yield n**2
sq_nums = square_numbers(numbers)
print('(2)Возврат квадратов чисел')
for _ in range(12):
    print(next(sq_nums))
print('-'*100)

even_num = list(filter(lambda x: x % 2 == 0,square_numbers(numbers)))
print("(3)Оставить только четные квадраты чисел")
print(even_num)
print('-'*100)

string_result = list(map(lambda x: f"value = {x}",square_numbers(numbers)))
print('(4)Используя map, преобразуйте числа: число → строка вида "value=ЧИСЛО" ')
print(string_result)
print('-'*100)

print(f'(5)Используя reduce, найдите:\n    a)сумму всех чисел списка')
sum_result = reduce(lambda a,b:a+b,numbers)
sum_result_greater_than_ten= reduce(lambda a,b: a + b, greater_than_ten(numbers))
sum_result_square_numbers = reduce(lambda a,b: a + b, square_numbers(numbers))
print(f'Сумма по списку numbers({numbers}) = {sum_result}')
print(f'Сумма по списку чисел, которые больше 10 = {sum_result_greater_than_ten}')
print(f'Сумма по списку квадратов чисел = {sum_result_square_numbers}')

print('    b)максимальное число списка')
max_value = reduce(lambda a,b: max(a,b), numbers)
max_value_greater_than_ten= reduce(lambda a,b: max(a,b), greater_than_ten(numbers))
max_value_square_numbers = reduce(lambda a,b: max(a,b), square_numbers(numbers))
print(f'Максимально число по списку numbers({numbers}) = {max_value}')
print(f'Максимально число по списку , которые больше 10 = {max_value_greater_than_ten}')
print(f'Максимально число по списку квадратов чисел = {max_value_square_numbers}')

print('-'*100)
print('(6)Генератор, который возвращает первые n чисел, кратных 3')
def multiples_of_three(numb_list):
    for num in numb_list:
        if num % 3 == 0:
            yield num

result_three = multiples_of_three(numbers)
n = int(input("Введите число, которое выведет n чисел, кратных 3\n"))
for _ in range(n):
    print(next(result_three))
print('-'*100)
print('(7) Напишите генератор word_generator(text), который возвращает слова строки по одному ')
def word_generator(text_list):
    words = text_list.split()
    for word in words:
        yield word
one_word_generator = word_generator(text)

for _ in range(8):
    print(next(one_word_generator))
print('-'*100)
print('(8)Используя map и filter, обработайте текст в следующей последовательности:\n   a) Оставить слова длиной > 4')
len_four = filter(lambda x: len(x) > 4, word_generator(text))
print(list(len_four))
print('-'*100)
print('   b)Преобразовать в верхний регистр')
up_register = map(lambda x: x.upper(), word_generator(text))
print(list(up_register))
print('-'*100)

def fib(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b

def fibonacci(n):
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(10)))