print('Загадай число от 1 до 100.')
start = 1
finish = 100
while True:
  number = (start + finish) // 2
  print('Твоё число равно, меньше или больше, чем число:', number)
  prompt = int(input('1 - равно, 2 - больше, 3 - меньше: '))
  if prompt == 2:
    start = number
  elif prompt == 3:
    finish = number
  else:
    print('Ты загадал число -', number)
    break
print('Угадал! Молодец!')
