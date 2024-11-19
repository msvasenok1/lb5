import random
#

def welcome():
    print(
        "Добро пожаловать в игру с камнями!\nПравила игры:\nКаждый игрок по очереди берет 1, 2 или 3 камня.\nВыигрывает тот, кто оставляет последний камень сопернику.")
    print("Всего камней: ", stones)


def user(stones):
    while True:
        try:
            move = int(input("Сколько камней вы хотите взять (1, 2 или 3)? "))
            if move in [1, 2, 3] and move <= stones:
                return move
            else:
                print("Ошибка: Вы можете взять только 1, 2 или 3 камня, и не больше, чем осталось.")
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")


def computer(stones):
    if stones >= 4:
        return min(3, stones)
    else:
        return stones


stones = random.randint(4, 30)
welcome()

while stones > 0:
    user_move = user(stones)
    stones -= user_move
    print(f"Вы взяли {user_move} камней. Осталось {stones} камней.")

    if stones == 0:
        print("Поздравляем! Вы выиграли!")
        break

    computer_move = computer(stones)
    stones -= computer_move
    print(f"Компьютер взял {computer_move} камней. Осталось {stones} камней.")

    if stones == 0:
        print("Компьютер выиграл! Попробуйте снова.")
