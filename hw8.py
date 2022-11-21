def task(num, epsil):
  sum_temp = 0
  addMember = 1
  i = 0
  while (abs(addMember) > epsil):
    sum_temp += addMember
    addMember = - addMember * num * num / ((2 * i + 1) * (2 * i + 2))
    i += 1
  return sum_temp

epsil = float(input('Введите точность: '))
num = float(input('Введите x: '))
summ = task(num, epsil)
print('Сумма ряда =', summ)