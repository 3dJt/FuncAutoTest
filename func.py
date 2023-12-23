def findSquare(length, width):
    print('Площадь равна ' + str(length * width) + ' см.')


def buyProducts(fullCost, money, name):
    products = ['хлеб', 'воду', 'печенье']
    p_cost = [29, 20, 79]
    print(f'Здравствуйте {name}. Ваш бюджет: {money} рублей. Стоимость всех покупок будет {fullCost} рублей.')
    fullCost = p_cost[0] + p_cost[1] + p_cost[2]
    if money >= fullCost:
        print('Вам хватит на ' + products[0] + ', ' + products[1] + ' и ' + products[2] + '.')
    elif money >= p_cost[0] + p_cost[1]:
        print('Вам хватит на ' + products[0] + ' и ' + products[1] + '.')
    elif money >= p_cost[0]:
        print('Вам хватит на ' + products[0] + '.')
    else:
        print('К сожелению вам ни на что не хватает.')


def buildHouse(balance, cost, number, street):
    print(f'Ваш баланс на данный момент: {balance} рублей.')
    print(f'Дом под номером {number} будет построен на улице {street} за {cost} рублей.')

    if balance >= cost:
        print(f'Дом под номером {number} успешно построен за {cost} рублей.')
        balance = balance - cost
        print(f'Ваш баланс составляет: {balance} рублей.')

    elif balance < cost:
        print('Дом не будет построен. У вас недостаточно средств.')

    else:
        print('Дом не будет построен.')


def gameRandomNumber(plrNumber):
    import random

    computerNumber = random.randint(1, 10)

    if plrNumber > 10:
        print('Вы ввели число больше чем нужно! Вам нужно ввести от 1 до 10.')

    elif plrNumber < 0:
        print('Вы ввели отрицательное число! Вам нужно ввести от 1 до 10.')

    while plrNumber != computerNumber:
        print('К сожелению вы не угадали число, но можете попробовать еще раз!')
        break

    if plrNumber == computerNumber:
        print('Вы угадали число!')
