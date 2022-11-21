def number(n_num, k_num):
  
  new_num_1 = 0
  while n_num > 0:
    digit = n_num % 10
    n_num = n_num // 10
    new_num_1 *= 10
    new_num_1 = new_num_1 + digit  
  print('Первое число наоборот:', new_num_1)

  new_num_2 = 0
  while k_num > 0:
    digit = k_num % 10
    k_num = k_num // 10
    new_num_2 *= 10
    new_num_2 = new_num_2 + digit  
  print('Второе число наоборот:', new_num_2)
  
  summ = new_num_1 + new_num_2
  print('Сумма:', summ)
  
  new_num_3 = 0
  while summ > 0:
    digit = summ % 10
    summ = summ // 10
    new_num_3 *= 10
    new_num_3 = new_num_3 + digit  
  print('Сумма наоборот:', new_num_3)

n_num = int(input('Введите первое число: '))
k_num = int(input('Введите второе число: '))
number(n_num, k_num)