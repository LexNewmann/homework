SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
ogrnip = 0
inn = 0
mail_index = 0
adress = ''

# bank_info
bank_account = 0
bank_name = ''
bik = 0
corr_account = 0

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

# check number для ОГРНИП и к/с
def check_number(number):
  count = 0
  while(number > 0):
    count = count + 1
    number = number // 10
  return count

# Главное меню
def main_menu(option1):
    return option1
def input_menu(option2):
    return option2
  
# Подменю 1: личная информация
def common_info():
  name = input('Введите имя: ')
  while 1:
  # Проверка возраста
    age = int(input('Введите возраст: '))
    if age > 0:
      break
    print('Возраст должен быть положительным')
  uphone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
  phone = ''
  for number in uphone:
    if number == '+' or ('0' <= number <= '9'):
      phone += number
  email = input('Введите адрес электронной почты: ')
  ogrnip = int(input('Введите ОГРНИП: '))
  number = ogrnip
  result_ogrnip = check_number(number)
  if result_ogrnip != 15:
    print('Ошибка ввода! ОГРНИП должен содержать 15 цифр. Введено:', result_ogrnip, 'Пожалуйста, повторите ввод.')
    common_info()
  inn = int(input('Введите ИНН: '))
  mail_index = input('Введите почтовый индекс: ')
  pattern = "0123456789"
  result_check = list(filter(lambda a: a in pattern, mail_index))
  result_check = "".join(result_check)
  mail_index = result_check 
  adress = input('Введите адрес: ')
  info = input('Введите дополнительную информацию:\n')
  return (name, age, phone, email, ogrnip, inn, mail_index, adress, info)
  
# Подменю 2: Банковские реквизиты
def bank_info():
  bank_account = int(input('Введите рассчетный счёт: '))
  bank_name = input('Введите название банка: ')
  bik = int(input('Введите БИК: '))
  corr_account = int(input('Введите корр. счёт: '))
  number = corr_account
  result_corr = check_number(number)
  if result_corr != 20:
    print('Ошибка ввода! Корр.счёт должен содержать 20 цифр. Введено:', result_corr, 'Пожалуйста, повторите ввод.')
    bank_info()
  return (bank_account, bank_name, bik, corr_account)
    
# Подменю 3: Показать информацию
def show_info(option3):
  return option3
    
# Подменю 4: Показать общую информацию
def show_common():
  # print general information
  print(SEPARATOR)
  print('Имя:    ', name)
  if 11 <= age % 100 <= 19: years_name = 'лет'
  elif age % 10 == 1: years_name = 'год'
  elif 2 <= age % 10 <= 4: years_name = 'года'
  else: years_name = 'лет'
  print('Возраст:', age, years_name)
  print('Телефон:', phone)
  print('E-mail: ', email)
  print('ОГРНИП: ', ogrnip)
  print('ИНН: ', inn)
  print('Почтовый индекс: ', mail_index)
  print('Адрес: ', adress)
  if info:
    print('')
    print('Дополнительная информация:')
    print(info)
    
# Подменю 5: Показать банковскую информацию
def show_bank():
  print('')
  print('Банковские реквизиты')
  print('Расчётный счёт: ', bank_account)
  print('Название банка: ', bank_name)
  print('БИК: ', bik)
  print('Корр. счёт: ', corr_account)

# цикл самой программы
while True:
  print(SEPARATOR)
  print('ГЛАВНОЕ МЕНЮ')
  print('1 - Ввести или обновить информацию')
  print('2 - Вывести информацию')
  print('0 - Завершить работу')
  option1 = int(input('Введите номер пункта меню: ')) # Главное меню
  result_main = main_menu(option1)
  if result_main == 0: # Прекращение работы
    break
    
  if result_main == 1: # Ввод личной инф-ии
    print(SEPARATOR)
    print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
    print('1 - Ввести общую информацию')
    print('2 - Ввести банковские реквизиты')
    print('0 - Назад')
    option2 = int(input('Введите номер пункта меню: '))
    result_input = input_menu(option2)
    if result_input == 0:
      main_menu(option1)
    if result_input == 1:
      name, age, phone, email, ogrnip, inn, mail_index, adress, info = common_info()
    if result_input == 2:
      bank_account, bank_name, bik, corr_account = bank_info()
      
  if result_main == 2: # Показать информацию
    print(SEPARATOR)
    print('ВЫВЕСТИ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Вся информация')
    print('0 - Назад')
    option3 = int(input('Введите номер пункта меню: ')) 
    result_show = show_info(option3)
    if result_show == 0:
      main_menu(option1)
    if result_show == 1:
      show_common() # Подменю 4: Показать общую информацию
    if result_show == 2:
      show_common() # Подменю 4: Показать общую информацию
      show_bank() # Подменю 5: Показать банковскую информацию
    else:   
      print('Введите корректный пункт меню')
  else:       
    print('Введите корректный пункт меню')