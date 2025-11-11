class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name + ':' + self.description


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = list()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                break



class Player:
    def __init__(self, current_room):
        self.inventory = []
        self.current_room = current_room

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"Ти перейшов в нову локацію {self.current_room.name}")
        else:
            print(f"Ти не можеш йти у напрямку {direction}")

    def take(self, item_name):
        item_to_take = None
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                item_to_take = item
                break

        if item_to_take:
            self.current_room.items.remove(item_to_take)
            self.inventory.append(item_to_take)
            print(f"Ви успішно взяли {item_to_take.name}")
        else:
            print(f"Предмету {item_name} немає в кімнаті")

    def drop(self, item_name):
        item_to_drop = None
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item_to_drop = item
                break

        if item_to_drop:
            self.inventory.remove(item_to_drop)
            self.current_room.add_item(item_to_drop)
            print(f"Ви викинули: {item_to_drop.name}")
        else:
            print(f"У вас в інвентарі немає '{item_name}'.")

    def look(self):
        print(f"Ви зараз в кімнаті {self.current_room.name} {self.current_room.description}")
        print(f"У кімнаті лежать предмети {self.current_room.items}")
        print(f"Доступні виходи: {self.current_room.exits.keys()}")




key = Item("Ключ", "Цей ключ потрібен для перемоги")
gun = Item("Меч", "Цим мечем можна захищатись")
lobby = Room("Лоббі", "Це початкова кімната з якої розпочинається гра")
kitchen = Room("Кухня", "На цій локації можна приготувати собі їсти")
toilet = Room("Туалет", "В цій кімнаті знаходиться цінна річ")
lobby.exits["схід"] = toilet
lobby.exits["північ"] = kitchen
kitchen.exits["схід"] = lobby
kitchen.exits["північ"] = toilet
toilet.exits["північ"] = lobby
toilet.exits["схід"] = kitchen
lobby.add_item(gun)
kitchen.add_item(key)
dima = Player(lobby)
win_room = toilet
win_item = "Ключ"
while True:
    command = input("Введіть команду що потрібно зробити(перевірити список команда /help) : ").lower()
    command1 = ""
    item = ""
    if " " in command:
        try:
            command1, item = command.split(" ",1)
        except ValueError:
            print("Помилка команди.")
            continue
    else:
        command1 = command

    if command1 == "/help":
        print("взяти (предмет), йти (напрямок), оглянутись, викинути (предмет)")

    elif command1 == "оглянутись":
        dima.look()

    elif command1 == "взяти":
        if item:
            dima.take(item)
        else:
            print("Взяти що? (напр., 'взяти ключ')")

    elif command1 == "йти":
        if item:
            dima.move(item)
        else:
            print("Йти куди? (напр., 'йти схід')")

    elif command1 == "викинути":
        if item:
            dima.drop(item)
        else:
            print("Викинути що?")

    if dima.current_room == win_room:
        win = False
        for item in dima.inventory:
            if item.name == win_item:
                print("Ви виграли!")
                win = True
                break
        if win:
            break


