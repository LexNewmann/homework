def maximum(a, b, c):
  max2 = (a + b + abs(a - b)) // 2
  return (max2 + c + abs(max2 - c)) // 2

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

res = maximum(a, b, c)
print('Максимальное число из трех:', res)