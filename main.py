import random

welcome = "Вас вітає гра. Kамінь, Ножниці, Папір!"
print(welcome)
start_command = "так"
choices = ["Камінь", "Ножниці", "Папір"]

while True:
    start = input("Щоб розпочати напишіть так: ")
    if start == start_command:
        print("Гра почалась!")
        break
    else:
        print("Ви ввели не правильну команду!!!!!")

wins = 0 
losses = 0

while True:
    computer_choice = random.choice(choices).lower()
    
    game = input("Введіть свою фігуру: ")
    game_lower = game.lower()

    choices_lower = [choice.lower() for choice in choices]

    if game_lower in choices_lower:
        print("Ваш суперник вибирає фігуру.")
        print(f"Ваша фігура: {game_lower}, Фігура суперника: {computer_choice}")
    else: 
        print("Ви ввели не дійсну фігуру!!!!!")
        continue
            
    if game_lower == computer_choice:
        print("Нічия!")
    elif (game_lower == "камінь" and computer_choice == "ножниці") or \
         (game_lower == "ножниці" and computer_choice == "папір") or \
         (game_lower == "папір" and computer_choice == "камінь"):
        print("Ви перемогли!")
        wins += 1
    else:
        print("Ви програли!")
        losses += 1

    if wins >= 2:
        print("Кінець гри, Ви перемогли!")
        break
    elif losses >= 2:
        print("Кінець гри, Ви програли!")
        break
