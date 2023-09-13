#Juego piedra papel o tijera
import random

tijera = '✌'
papel = '🤚'
piedra = '✊'

def escoger_opciones():
  options = ('piedra', 'papel', 'tijera')
  user = input("Ingrese piedra, papel o tijera => ")
  user = user.lower()

  if not user in options:
    print('esa opción no es valida')
  
  computadora = random.choice(options)
  print('user option => ', user)
  print('computer option => ', computadora)
  return user, computadora
  

def rules_game(user, computadora, user_win, compu_win):
  if user == computadora:
    print("¡Empate!")
  elif user == "piedra":
    if computadora == "papel":
      print(f"{papel} gana a {piedra}")
      print("Computadora gana")
      compu_win += 1
    else:
      print(f"{piedra} gana a {tijera}")
      print("Usuario gana")
      user_win += 1
  elif user == "papel":
    if computadora == "piedra":
      print(f"{papel} gana a {piedra}")
      print("Usuario gana")
      user_win += 1
    else:
      print(f"{tijera} gana a {papel}")
      print("Computadora gana")
      compu_win += 1
  elif user == "tijera":
    if computadora == "piedra":
      print(f"{piedra} gana a {tijera}")
      print("Computadora gana")
      compu_win += 1
    else:
      print(f"{tijera} gana a {papel}")
      print("Usuario gana")
      user_win += 1
  return user_win, compu_win 

def winner(user_win, compu_win):
  if compu_win == 2:
    print('🏆 El ganador es la computadora 🏆💻')
    
    
  if user_win == 2:
    print('🏆 El ganador es el usuario 👤🏆')
    

def run_game():
  
  rounds = 1
  
  print(f"Bienvenido al juego {piedra} {papel} o {tijera}")
  print("Modalidad de juego: 2️⃣  de 3️⃣")
  compu_win = 0
  user_win = 0
  
  while user_win < 2 and compu_win < 2:
    print('-' * 40)
    print('Ronda', rounds)
    print('-' * 40)
    
    print('Computadora 💻 ', compu_win)
    print('Usuario 👤', user_win)
  
    rounds += 1
  
    user, computadora = escoger_opciones()
    user_win, compu_win = rules_game(user, computadora, user_win, compu_win)
    winner(user_win, compu_win)
    
    
run_game()
