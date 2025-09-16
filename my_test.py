
print('Welcome back, Mike!')
def main(s = input()):
    #Пробелы могут быть, а могут не быть. Создадим список, исключив пробелы,
    #затем обратно сделаем список строкой
    s = ''.join([j for j in s if j != ' '])
    sym = ''
    # Определяем оператор в строке
    for c in s:
        if not c.isdigit() and c != '.':
            sym = c
            break
    #Проверяем, что оператор - нужный символ
    try:
        if sym not in ['/', '*', '+', '-']:
            raise ValueError
    except ValueError:
        return 'throws Exception //т.к. строка не является математической операцией'

    #Исключаем попадание оператора на 0й или -1й индекс строки
    try:
        if s.find(sym) == 0 or s.rfind(sym) == len(s) - 1:
            raise ValueError
    except ValueError:
        return 'throws Exception //т.к. строка не является математической операцией'

    #Проверим количество операторов (и возможно других символов), убрав цифры и точки
    try:
        if len([j for j in s if not j.isdigit() and j != '.']) > 1:
            raise ValueError
    except ValueError:
        return 'throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)'

    #Определим первое число
    try:
        num1 = int(s[:s.find(sym)])
    except ValueError:
        return 'throws Exception //т.к. числа должны быть целыми'

    #Определим второе число
    try:
        num2 = int(s[s.find(sym) + 1:])
    except ValueError:
        return 'throws Exception //т.к. числа должны быть целыми'

    #Проверим нужный диапазон чисел
    try:
        if 1 > num1 or num1 > 10 or 1 > num2 or num2 > 10:
            raise ValueError
    except ValueError:
        return 'throws Exception //т.к. числа должны быть от 1 до 10 включительно'

    #Вычисление самого результата
    if sym == '/':
        result = num1 // num2
    elif sym == '*':
        result = num1 * num2
    elif sym == '-':
        result = num1 - num2
    elif sym == '+':
        result = num1 + num2
    return result #Возвращаем результат


print(main())








































































