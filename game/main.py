import random

def choose_options():
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if user_option not in options:
        print("Esa opción no es válida")
        return None, None

    computer_option = random.choice(options)

    print("Opción del usuario =>", user_option)
    print("Opción de la computadora =>", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera")
            print("¡El usuario ganó!")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("¡La computadora ganó!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra")
            print("¡El usuario ganó!")
            user_wins += 1
        else:
            print("Tijera gana a papel")
            print("¡La computadora ganó!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("¡El usuario ganó!")
            user_wins += 1
        else:
            print("Piedra gana a tijera")
            print("¡La computadora ganó!")
            computer_wins += 1

    return user_wins, computer_wins

def play_game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_option, computer_option = choose_options()

        if user_option is None or computer_option is None:
            continue

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        print("Puntuación:")
        print("Usuario:", user_wins)
        print("Computadora:", computer_wins)

        play_again = input("¿Quieres jugar de nuevo? (s/n) => ")
        if play_again.lower() != "s":
            break

    print("¡Gracias por jugar!")

play_game()

            
