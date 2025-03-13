import random


class Cart:
    def __init__(self):
        self.numbers = sorted(random.sample(range(1, 91), 15))
        self.rows = [self.numbers[i * 5:(i + 1) * 5] for i in range(3)]
        for row in self.rows:
            row.sort()
            empty_indices = random.sample(range(9), 4)
            for i in sorted(empty_indices, reverse=True):
                row.insert(i, '  ')

    def __str__(self):
        result = "\n".join(" ".join(f"{num:2}" for num in row) for row in self.rows)
        print(f"__str__ вызван: \n{result}")
        return result

    def __eq__(self, other):
        if isinstance(other, Cart):
            result = self.numbers == other.numbers
            print(f"__eq__ вызван: {result}")
            return result
        return False

    def display(self, title):
        print(title)
        print(self)

    def mark_number(self, number):
        """Зачеркивает число на карточке, если оно есть."""
        for row in self.rows:
            if number in row:
                index = row.index(number)
                row[index] = '--'  # Обозначаем зачеркнутое число
                print(f"mark_number вызван: {number} зачеркнуто")
                return True
        print(f"mark_number вызван: {number} отсутствует")
        return False

    def is_complete(self):
        """Проверяет, все ли числа зачеркнуты."""
        return all(num == '--' for row in self.rows for num in row if num != '  ')

class Player:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def __str__(self):
        result = f"Игрок: {self.name}\nКарточка:\n{self.cart}"
        print(f"__str__ вызван: \n{result}")
        return result

    def __eq__(self, other):
        if isinstance(other, Player):
            result = self.name == other.name and self.cart == other.cart
            print(f"__eq__ вызван: {result}")
            return result
        return False



class PlayerComp(Player):
    def take_turn(self, number):
        if self.cart.mark_number(number):
            print(f"{self.name} зачеркнул число {number}")
        else:
            print(f"{self.name} пропустил число {number}")
        return True


class PlayerHuman(Player):
    def take_turn(self, number):
        self.cart.display(f"------ Карточка {self.name} ------")
        choice = input(f"Число {number} есть на вашей карточке? Зачеркнуть? (y/n): ")
        if choice.lower() == 'y':
            if not self.cart.mark_number(number):
                print(f"{self.name}, такого числа нет на вашей карточке. Вы проиграли!")
                return False
            return True
        else:
            if self.cart.mark_number(number):
                print(f"{self.name}, вы пропустили число, которое есть на вашей карточке. Вы проиграли!")
                return False
            return True


class Game:
    def __init__(self, player1_type='human', player2_type='comp', player1_name="Игрок 1", player2_name="Игрок 2"):
        self.barrels = random.sample(range(1, 91), 90)
        self.player1 = PlayerHuman(player1_name) if player1_type == 'human' else PlayerComp(player1_name)
        self.player2 = PlayerHuman(player2_name) if player2_type == 'human' else PlayerComp(player2_name)

    def __str__(self):
        result = f"Игра между {self.player1.name} и {self.player2.name}"
        print(f"__str__ вызван: {result}")
        return result

    def __eq__(self, other):
        if isinstance(other, Game):
            result = self.player1 == other.player1 and self.player2 == other.player2
            print(f"__eq__ вызван: {result}")
            return result
        return False

    def start(self):
        for turn, number in enumerate(self.barrels, 1):
            print(f"\nНовый бочонок: {number} (осталось {90 - turn})")
            if not self.player1.take_turn(number):
                print(f"{self.player1.name} проиграл. Игра завершена.")
                break
            if not self.player2.take_turn(number):
                print(f"{self.player2.name} проиграл. Игра завершена.")
                break
            if self.player1.cart.is_complete():
                print(f"Поздравляем! {self.player1.name} выиграл!")
                break
            if self.player2.cart.is_complete():
                print(f"Поздравляем! {self.player2.name} выиграл!")
                break


def select_player_type(player_number):
    while True:
        choice = input(f"Выберите тип игрока {player_number} (human/comp): ").lower()
        if choice in ['human', 'comp']:
            return choice
        print("Неверный ввод. Пожалуйста, введите 'human' или 'comp'.")


def enter_player_name(player_number):
    name = input(f"Введите имя для игрока {player_number}: ")
    return name if name else f"Игрок {player_number}"


if __name__ == "__main__":
    print("Добро пожаловать в игру Лото!")
    player1_type = select_player_type(1)
    player1_name = enter_player_name(1)
    player2_type = select_player_type(2)
    player2_name = enter_player_name(2)

    game1 = Game(player1_type, player2_type, player1_name, player2_name)
    game2 = Game(player1_type, player2_type, player1_name, player2_name)

    print(game1 == game2)  # Проверка игры
    print(game1.player1 == game2.player1)  # Проверка игроков
    print(game1.player1.cart == game2.player1.cart)  # Проверка карточек

    game1.start()
