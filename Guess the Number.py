import random
import os
import time

logo = '''
   ___                                             _               
  / _ \_   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\ | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  

-------------------------------------------------------------------

  I'm thinking of a number between 1 and 100. Guess the number!

-------------------------------------------------------------------
'''

number = random.randint(0, 100)

while True:
    os.system('cls')
    print(logo)
    level = input("          Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == "easy":
        lives = 10
        break
    elif level == "hard":
        lives = 5
        break

while lives != 0:
    for _ in range(lives):
        os.system('cls')
        print(f'''
   ___                                             _               
  / _ \_   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\ | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  

-------------------------------------------------------------------

   Be careful! You have {lives} attempts remains to guess the number!

-------------------------------------------------------------------
''')

        answer = int(input("                          Make a guess: "))
        if answer == number:
            os.system('cls')
            print(f'''
   ___                                             _               
  / _ \_   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\ | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  

-------------------------------------------------------------------

                            Congratulation!

-------------------------------------------------------------------

                               You won!   
''')
            lives = 0
            break

        elif answer < number:
            os.system('cls')
            print('''
   ___                                             _               
  / _ \_   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\ | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  

-------------------------------------------------------------------

                               Too low!

-------------------------------------------------------------------


''')
            time.sleep(2)

        else:
            os.system('cls')
            print('''
   ___                                             _               
  / _ \_   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\ | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  

-------------------------------------------------------------------

                               Too high!

-------------------------------------------------------------------


''')
            time.sleep(2)
        lives -= 1

if answer != number:
    os.system('cls')
    print(f'''
   ___                                             _               
  / _ \_   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\ | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  

-------------------------------------------------------------------

                                Whoops!

-------------------------------------------------------------------
  ''')
    print("                  You've run out of guesses, you lose.")



