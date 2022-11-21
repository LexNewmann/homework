num = float(input('Введите число: '))
count = 0
if num >= 1:
  while num >= 10:
    num /= 10
    count += 1
  print('Мантисса это:', round(num * 10))
  print('Порядок это:', count)
  
elif num < 1:
  while num < 1:
    num *= 10
    count += 1
  print('Мантисса это:', round(num * 10))
  print('Порядок это:', -count)
