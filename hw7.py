def calculate_danger(depth):
  result = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
  return result

acceptable_danger = float(input('Введите максимально допустимый уровень опасности: '))
min_depth = 0
max_depth = 4.0

while True:
  cur_depth = (max_depth + min_depth) / 2
  cur_hazard = calculate_danger(cur_depth)
  if cur_hazard < 0:
    max_depth = cur_depth
    calculate_danger(cur_depth)
  elif cur_hazard > acceptable_danger:
    min_depth = cur_depth
    calculate_danger(cur_depth)
  else:
    break
print('Приблизительная глубина безопасной кладки:', cur_depth)
