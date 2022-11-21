def count_numbers(test_number):
  count_numbers = 0
  while(test_number > 0):
    count_numbers = count_numbers + 1
    test_number = test_number // 10
  return count_numbers

first_n = int(input('Введите первое число: '))
test_number = first_n
res1 = count_numbers (test_number)

second_n = int(input('Введите второе число: '))
test_number = second_n
res2 = count_numbers(test_number)

if (res1 < 3) or (res2 < 4):
  print('Ошибка ввода. Значения меньше минимальных.')
else:
  def inversion(test_number, res_test):
    last_digit = test_number % 10
    test_digit = test_number // 10 ** (res_test - 1)
    between_digits = test_number % 10 ** (res_test - 1) // 10
    test_number = last_digit * 10 ** (res_test - 1) + between_digits * 10 + test_digit
    return test_number

  test_number = first_n
  res_test = res1
  res1_1 = inversion(test_number, res_test)
  print('Изменённое первое число:', res1_1)

  test_number = second_n
  res_test = res2
  res2_1 = inversion (test_number, res_test)
  print('Изменённое второе число:', res2_1)

print('Сумма измененных чисел:', res1_1 + res2_1)