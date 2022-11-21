def adishe(s_credit, n, i_proc):
  i = i_proc / 100
  k1 = i * ((1 + i) ** n)
  k2 = ((1 + i) ** n) - 1
  k = k1 / k2
  a_pay = k * s_credit
  s_credit += a_pay 
  
  for circle in range(count_circles):
    ost = s_credit - a_pay
    print('\nОстаток:', round(ost, 2))
    vip = i * ost
    print('Выплата процентов:',round(vip, 2))
    telo = a_pay - vip
    print('Тело кредита:',round(telo, 2))
    s_credit -= telo
    print('=====================================')
  ost = s_credit - a_pay
  return ost

s_credit = float(input('Введите сумму кредита S: '))
n = int(input('Введите кол-во лет n: '))
i_proc = int(input('Введите i% годовых: ')) 
count_circles = n - 2

res1 = adishe(s_credit, n, i_proc)
print('\nОстаток:', round(res1, 2))
print('=====================================')

s_credit = res1
n_new = int(input('\nНа сколько лет продлевается договор? '))
n_new += 2
n = n_new
count_circles = n
print(n)
i_proc_new = int(input('Увеличение ставки i% до: '))
i_proc = i_proc_new

res2 = adishe(s_credit, n, i_proc)
print('\nОстаток:', round(res2, 2))
