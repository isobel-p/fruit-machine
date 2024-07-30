import winsound
from threading import Thread
import time
import os
import sys
import random
import math
import turtle

# turtle functions
def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
def polygon(sides, length, colour):
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)
    turtle.begin_fill()
    angle = 180-((180*(sides-2))/sides)
    for i in range(sides):
        turtle.forward(length)
        turtle.left(angle)
    turtle.end_fill()
    turtle.penup()
def rectangle(width, length, colour):
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor(colour)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
def circle(radius, colour):
    turtle.pendown()
    turtle.color(colour)
    turtle.fillcolor(colour)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

# icon functions
def cherry(x, y):
    x -= 40
    y -= 20
    turtle.setheading(225)
    for _ in range(2):
        goto(x, y)
        turtle.color("green")
        turtle.circle(300, 20)
        turtle.color("red")
        circle(30, "red")
        turtle.left(20)
    turtle.setheading(0)
def bell(x, y):
    x -= 40
    y -= 10
    goto(x, y-130)
    circle(10, "gold")
    goto(x, y)
    turtle.setheading(180)
    turtle.color("black")
    turtle.fillcolor("gold")
    turtle.begin_fill()
    turtle.circle(60, 90)
    turtle.forward(60)
    turtle.right(270)
    turtle.forward(60)
    turtle.forward(60)
    turtle.right(270)
    turtle.forward(60)
    turtle.circle(60, 90)
    turtle.end_fill()
def lemon(x, y):
    x -= 40
    y -= 140
    goto(x, y)
    circle(60, "yellow")
    goto(x, y+5)
    circle(55, "white")
    goto(x, y+15)
    circle(45, "yellow")
    turtle.color("white")
    turtle.pendown()
    for i in range (3):
        turtle.penup()
        turtle.circle(45, 60)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(90)
        turtle.left(90)
def orange(x, y):
    x -= 40
    y -= 140
    goto(x, y)
    circle(60, "orange")
    goto(x, y+5)
    circle(55, "white")
    goto(x, y+15)
    circle(45, "orange")
    turtle.color("white")
    turtle.pendown()
    for i in range (3):
        turtle.penup()
        turtle.circle(45, 60)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(90)
        turtle.left(90)
def star(x, y):
    x -= 105
    y -= 65
    goto(x, y)
    turtle.color("deep sky blue")
    turtle.fillcolor("deep sky blue")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(130)
        turtle.right(144)
    turtle.end_fill()
def skull(x, y):
    x -= 40
    y -= 150
    goto(x, y)
    circle(70, "black")
    turtle.goto(x-20, y+50)
    rectangle(40, 30, "white")
    turtle.color("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.goto(x-40, y+60)
    turtle.right(45)
    for i in range(2):
        turtle.circle(60,90)
        turtle.circle(30,90)
    turtle.left(45)
    turtle.end_fill()
    goto(x-20, y+80)
    for i in range(2):
        circle(10, "black")
        turtle.forward(40)
    goto(x-5, y+65)
    polygon(3, 7, "black")

# game functions
def setup():
    global credit
    global streak
    global music
    global font_name
    credit = 100
    streak = 1.0
    music = False
    font_name = "Terminal"
    screen = turtle.Screen()
    screen.title("Fruit Machine")
    screen.setup(width=600, height=600)
    screen.bgpic("background.gif")
    goto(0, 0)
def bgm():
    while True:
        winsound.PlaySound("bgm.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
        time.sleep(1613)
def check_winnings(rolled):
    not_duplicates = []
    duplicates = []
    print("\n")
    for i in rolled:
        if i in not_duplicates:
            duplicates.append(i)
        else:
            not_duplicates.append(i)
    goto(-250, -200)
    rectangle(500, 70, "white")
    goto(0, -265)
    if len(duplicates) == 1:
        if duplicates[0] == "D":
            turtle.write(arg="2 Skulls!", move=False, align="center", font=("font_name", 45, "italic"))
            return -100
        else:
            turtle.write(arg="2 of a Kind!", move=False, align="center", font=("font_name", 45, "italic"))
            return 50
    elif len(duplicates) == 2:
        if duplicates[0] == "D":
            turtle.write(arg="3 Skulls!", move=False, align="center", font=("font_name", 45, "italic"))
            return "fail"
        elif duplicates[0] == "B":
            turtle.write(arg="3 Bells!", move=False, align="center", font=("font_name", 45, "italic"))
            return 500
        else:
            turtle.write(arg="3 of a Kind!", move=False, align="center", font=("font_name", 45, "italic"))
            return 100
    else:
        turtle.write(arg="Too Bad!", move=False, align="center", font=("font_name", 45, "italic"))
        return 0
def play():
    global streak
    global credit
    symbols = ["C", "B", "L", "O", "S", "D"]
    names = [cherry, bell, lemon, orange, star, skull]
    rolled = []
    input("ROUND BEGIN!\nPull lever to spin [ENTER]")
    credit -= 20
    x_pos = [-150, 40, 230]
    numbers = []
    for i in range(3):
        number = random.randint(0, 5)
        rolled.append(symbols[number])
        numbers.append(number)
    count = 0
    for num in numbers:
        turtle.width(5)
        names[num](x_pos[count], 80)
        turtle.setheading(0)
        turtle.width(0)
        count += 1
    x = check_winnings(rolled)
    if x == "fail":
        credit = 0
        streak = 1.0
    elif x <= 0:
        streak = 1.0
        credit += x
        credit = math.floor(credit)
    else:
        credit += x*streak
        credit = math.floor(credit)
        streak += 0.5
    input("Press ENTER to continue...")
    menu()
def menu():
    global credit
    turtle.speed(0)
    turtle.width(0)
    goto(-250, 230)
    rectangle(500, 70, "white")
    goto(0, 160)
    turtle.write(arg="Fruit Machine", move=False, align="center", font=("font_name", 45, "bold"))
    turtle.width(5)
    x_pos = [-270, -80, 110]
    for i in range(3):
        goto(x_pos[i], 80)
        rectangle(160, 160, "white")
    turtle.width(1)
    goto(-250, -100)
    rectangle(500, 70, "white")
    goto(0, -165)
    turtle.write(arg=f'Credit: {credit} x{streak}', move=False, align="center", font=("font_name", 45, "normal"))
    goto(-250, -200)
    rectangle(500, 70, "white")
    goto(0, -265)
    turtle.write(arg="Spin to Win!", move=False, align="center", font=("font_name", 45, "normal"))
    #skull(-150, 80)
    os.system('cls')
    print("""
  ______          _ _     __  __            _     _                        _____            _             _   _____                 _ 
 |  ____|        (_) |   |  \\/  |          | |   (_)                      / ____|          | |           | | |  __ \\               | |
 | |__ _ __ _   _ _| |_  | \\  / | __ _  ___| |__  _ _ __   ___   ______  | |     ___  _ __ | |_ _ __ ___ | | | |__) |_ _ _ __   ___| |
 |  __| '__| | | | | __| | |\\/| |/ _` |/ __| '_ \\| | '_ \\ / _ \\ |______| | |    / _ \\| '_ \\| __| '__/ _ \\| | |  ___/ _` | '_ \\ / _ \\ |
 | |  | |  | |_| | | |_  | |  | | (_| | (__| | | | | | | |  __/          | |___| (_) | | | | |_| | | (_) | | | |  | (_| | | | |  __/ |
 |_|  |_|   \\__,_|_|\\__| |_|  |_|\\__,_|\\___|_| |_|_|_| |_|\\___|           \\_____\\___/|_| |_|\\__|_|  \\___/|_| |_|   \\__,_|_| |_|\\___|_|               
""")
    credit_txt = f"{credit:03d}"
    print(f'''
    _________________________________________
    | ________ ________ ________             |
    | |      | |      | |      | PLEASE TAKE |
    | |  ON  | |  GO  | | QUIT | YOUR MONEY: |
    | |______| |______| |______| =========== |
    |                                        |
    |  __     ______ __  __   ______________ |
    | |__|   |  ____|  \\/  | |   BALANCE:   ||
    |   |    | |__  | \\  / | |     {credit_txt}      ||
    |   |    |  __| | |\\/| | | STREAK: x{streak} ||
    |   |    | |    | |  | | |______________||
    | =====  |_|    |_|  |_| - Fruit Machine |
    |________________________________________|
    ''')
    if credit < 0:
        turtle.speed("normal")
        goto(-300, 300)
        rectangle(600, 600, "black")
        os.system('cls')
        sys.exit("The Fruit Machine is out of funds!")
    choice = input("""Press a button:
ON [0]
GO [1/ENTER]
PULL [2]
QUIT [3]
> """)
    if choice == "0":
        input("The Fruit Machine is already on!")
        menu()
    elif choice == "1":
        play()
    elif choice == "2":
        input("You haven't started a round yet!")
        menu()
    elif choice == "3":
        print(f'Know your limits!\nYou finished with £{credit/100}\n\nClosing down...')
        credit = 0
        turtle.speed("normal")
        goto(-300, 300)
        rectangle(600, 600, "black")
        winsound.PlaySound("quit.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
        sys.exit()
    else:
        play()

setup()
bgm = Thread(target=bgm)
bgm.start()
menu()
#bell(0, 0)
