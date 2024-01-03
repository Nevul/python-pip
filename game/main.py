import random
options = ('piedra', 'papel', 'tijera')

round = 1
computer_wins = 0
user_wins = 0


while True:
  print('\n')
  print('*' * 10)
  print('Round ', round)
  print('*' * 10)
  print('\n')
  
  user_option = input('Piedra, papel o tijera => ')
  user_option = user_option.lower()
  '''selection = random.randint(0, 2)
  computer_option = options[selection]'''
  computer_option = random.choice(options)
  
  if not user_option in options:
    print('Opcion no valida')
    continue
  else:
    if user_option == computer_option:
      print(f'\nComputer: {computer_option}')
      print('Empate')
    elif user_option == 'piedra':
      if computer_option == 'tijera':
        print(f'\nComputer: {computer_option}')
        print('piedra gana a tijera')
        print('user gana')
        user_wins += 1
      else:
        print(f'\nComputer: {computer_option}')
        print('papel gana a la piedra')
        print('computer gana')
        computer_wins += 1
    elif user_option == 'papel':
      if computer_option == 'piedra':
        print(f'\nComputer: {computer_option}')
        print('papel le gana a la piedra')
        print('user gana')
        user_wins += 1
      else:
        print(f'\nComputer: {computer_option}')
        print('Tijera le gana a papel')
        print('computer gana')
        computer_wins += 1
    elif user_option == 'tijera':
      if computer_option == 'papel':
        print(f'\nComputer: {computer_option}')
        print('tijera gana a papel')
        print('user gana')
        user_wins += 1
      else:
        print(f'\nComputer: {computer_option}')
        print('piedra gana a tijera')
        print('computer gana')
        computer_wins += 1
  
  print('\nComputer wins: ', computer_wins)
  print('User wins: ', user_wins)
  
  if computer_wins == 2 or user_wins == 2:
    break
  round += 1