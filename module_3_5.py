def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)
print(result, ",", result2)

#если нужна проверка на 0 - чтобы не умножить на 0 конечный результат,
# то нужно добавить проверку на 0:
# if first == 0:
#    if len(str_number) == 1:
#       return 1
#    else:
#       return get_multiplied_digits(int(str_number[1:]))