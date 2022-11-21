def show(num):
  count = 0
  if num >= 1:
    while num >= 10:
      num /= 10
      count += 1
    print('Формат плавающей точки:', round(num, 3),'* 10 **', count)
  
  elif num < 1:
    while num < 1:
      num *= 10
      count += 1
    print('Формат плавающей точки:', round(num, 3),'* 10 **', -count)

num = float(input('Введите любое число: '))
show(num)