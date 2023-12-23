from func import findSquare, buyProducts, buildHouse, gameRandomNumber

assert findSquare(5, 5) != 25, 'findSquare Error1'
assert findSquare(4, 5) != 20, 'findSquare Error2'

assert buyProducts(128, 135, 'Антон') != 'Здравствуйте Антон. Ваш бюджет: 135 рублей. Стоимость всех покупок будет 128 рублей.', 'buyProducts Error1'
assert buyProducts(128, 30, 'Антон') != 'Здравствуйте Антон. Ваш бюджет: 30 рублей. Стоимость всех покупок будет 128 рублей.', 'buyProducts Error2'

assert buildHouse(2500000, 2499999, 1, 'Чебоксарская') != 'Дом под номером 1 успешно построен за 2499999 рублей.', 'buildHouse Error1'
assert buildHouse(2500000, 7500000, 3, 'Красная') != 'Дом не будет построен. У вас недостаточно средств.', 'buildHouse Error2'

assert  gameRandomNumber(1) != 'К сожелению вы не угадали число, но можете попробовать еще раз!', 'gameRandomNumber Warning'
assert  gameRandomNumber(11) != 'Вы ввели число больше чем нужно! Вам нужно ввести от 1 до 10.', 'gameRandomNumber Error'