import tkinter as tk
import random

game_width = 700
game_height = 700
speed = 50
space_size = 50
body_parts = 3
snake_color = "#00FF00"
food_color = "#FF0000"
background_color = "#000000"

class Snake:
    def init_(self):
        self.body_size = body_parts
        sel.coordinates = []
        self.squares = []

        for i in range(0, body_parts):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(x,y, x + space_size, fill=snake_color, tag="snake")
            self.squares.append(square)

    

class Food:
    
    def init_(self):

        x= random.randint(0, (game_width/space_size)-1)* space_size
        y = random.randint(0, (game_height/space_size)-1)*space_size

        self.coordinates = [x,y]

        canvas.create_oval(x,y,x + space_size, y+ space_size, fill=food_color, tag="food")



def next_turn(snake, food):
    x,y = snake.coordinates[0]

    if direction == "up":
        y-= space_size
    elif direction == "down":
        y+=space_size
    elif direction == "left":
        x-=space_size
    elif direction == "right":
        x+=space_size

    snake.coordinates.insert(o, (x,y))

    square = canvas.create_rectangle(x,y,x + space_size, y + space_size, fill=snake_color)
    snake.squares.insert(o,square)

    if x== food.coordinates[0] and y == food.coordinates[1]:
        global score

        score+=1

        label.config(text="Score:{}".format(score))
        canvas.delete("food")

        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        windows.after((speed, next_turn, snake, food))

        def change_direction(new_direction):
            global direction

            if new_direction == 'left':
                if direction != 'right':
                    direction=new_direction
            elif new_direction=='right':
                if direction !="left":
                    direction = new_direction
            elif new_direction=='up':
                if direction != 'down':
                    direction = new_direction
            elif new_direction=='down':
                if direction != 'up':
                    direction= new_direction

        

def next_direction(new_direction):
    

def check_collisions():
    pass

def game_over():
    pass

# Create the Tkinter window
window = tk.Tk()
window.title("Snake game")
window.resizable(False, False)


# Create other widgets and set up the game interface here
score = 0
direction = 'down'

label = tk.Label(window, text="Score: {}".format(score), font=('consolas', 40))
label.pack()

# Create a canvas to draw the game on
canvas = tk.Canvas(window, width=game_width, height=game_height, bg=background_color)
canvas.pack()


window.mainloop()
