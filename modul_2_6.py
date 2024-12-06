first_number = int(input('Введите число от 3 до 20: '))
def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2,number):
            if i >= j:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password

result = get_password(first_number)
print(result)