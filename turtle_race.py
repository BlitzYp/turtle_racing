import turtle
from typing import List
from random import choice, randint
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = ["red", "green", "yellow", "blue", "orange"]

def arrange(competitors: List[turtle.Turtle]) -> None:
    prev_y = (-SCREEN_HEIGHT / 2) + 30
    chosen = []
    for i in competitors:
        res = choice(list(filter(lambda x: not x in chosen, COLORS)))
        chosen.append(res)
        i.color(res)
        i.speed("normal")
        i.penup()
        i.setpos((-SCREEN_WIDTH / 2) + 30, prev_y)
        prev_y += 130

def race(competitors: List[turtle.Turtle]):
    current_max = competitors[0].xcor()
    winner = None
    results = {i.color()[0]: i.xcor() for i in competitors}
    while current_max < (SCREEN_WIDTH / 2) - 30:
        for t in competitors:
            t.fd(randint(5, 20))
            if t.xcor() > current_max:
                current_max = t.xcor()
                winner = t.color()[0]
            results[t.color()[0]] = t.xcor()
        index = 0
    return winner, results

if __name__ == "__main__":
    screen = turtle.Screen()
    while True:
        competitors = [turtle.Turtle("turtle") for _ in range(5)]
        screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.title("Turtle racing")
        arrange(competitors)
        data = turtle.textinput(title="Bet", prompt="Who will win: ")
        if not len(data) or not data in COLORS: 
            screen.clearscreen()
            continue
        winner, results = race(competitors)
        if winner.lower() == data.lower(): print(f"Your turtle won! The winner turtle was {winner}")
        else: print(f"Your turtle lost! The winner turtle was {winner}")
        print("RESULTS\n-------------")
        for i, k in sorted(results.items(), key=lambda x: x[1], reverse=True):
            print(f"Color: {i}, score: {k}")
        sleep(2)  
        screen.clearscreen() 
    turtle.mainloop()
