# 🧭 Console Text Adventure Game (OOP)

This is a text-based adventure game written in Python to practice Object-Oriented Programming (OOP) principles.

The core of this project demonstrates **Object Composition** ("HAS-A" relationship) over inheritance ("IS-A").

* The `Player` object **has** an inventory (`list` of `Item` objects) and a reference to its `current_room` (`Room` object).
* The `Room` object **has** a list of items (`list` of `Item` objects) and a dictionary of exits (`dict` mapping to other `Room` objects).

## 🚀 How to Run

1.  Clone the repository or download `main.py`.
2.  Make sure you have Python 3 installed.
3.  Run the game from your terminal:

```bash
python main.py
```


## 💻 Tech Stack
Python 3

Object-Oriented Programming (Classes, Objects, Composition)

##🎮 Basic Commands
look (to see the room)

go [direction] (e.g., go north)

take [item] (e.g., take key)

drop [item] (e.g., drop sword)

inventory (to see your items)

/help (to see commands)
