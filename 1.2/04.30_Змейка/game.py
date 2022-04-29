import random
import pygame
from tkinter import *
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
SPACE_SIZE = 25
SNAKE_LENGTH = 3    
SPEED = 100
COLOR_BODY = '#0f1ab2'
COLOR_HEAD = '#24ffc4'
FOOD_COLOR = 'red'
BACKGROUND_COLOR = 'black'
pygame.init()



class Snake:
    pygame.mixer.music.load("da882ce11f7c88f.mp3")
    pygame.mixer.music.play(loops=0, start=0.0,fade_ms = 0)
    def __init__(self):
        self.snake_length = SNAKE_LENGTH
        self.coord = [[0, 0]] * 3
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR_BODY)
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH/SPACE_SIZE) -
                           1) * SPACE_SIZE   
        y = random.randint(0, (WINDOW_HEIGHT/SPACE_SIZE) -
                           1) * SPACE_SIZE   

        self.coord = [x, y]

        canvas.create_rectangle(x, y, x + SPACE_SIZE,
                                y + SPACE_SIZE, fill=FOOD_COLOR)


def move(snake, food):
    for x, y in snake.coord:
        square = canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR_BODY)

    x, y = snake.coord[0]

    if (direction == 'down'):
        y += SPACE_SIZE
    elif (direction == 'up'):
        y -= SPACE_SIZE
    elif (direction == 'left'):
        x -= SPACE_SIZE
    elif (direction == 'right'):
        x += SPACE_SIZE

    snake.coord.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=COLOR_HEAD)
    snake.squares.insert(0, square)
    if (x == food.coord[0] and y == food.coord[1]):
        global score

        score += 1

        label_score.config(text='Счёт: {}'.format(score))
        canvas.delete('food')

        food = Food()
    else:
        x, y = snake.coord[-1]
        square = canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=BACKGROUND_COLOR)

        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if (check_collisions(snake)):
        game_over()
    else:
        window.after(SPEED, move, snake, food)


def change_direction(new_dir):
    global direction

    if (new_dir == 'down'):
        if (direction != 'up'):
            direction = new_dir
    elif (new_dir == 'up'):
        if (direction != 'down'):
            direction = new_dir
    if (new_dir == 'left'):
        if (direction != 'right'):
            direction = new_dir
    if (new_dir == 'right'):
        if (direction != 'left'):
            direction = new_dir


def check_collisions(snake):
    x, y = snake.coord[0]

    if (x < 0 or x >= WINDOW_WIDTH):
        return True
    elif (y < 0 or y >= WINDOW_HEIGHT):
        return True

    for snake_length in snake.coord[1:]:
        if (x == snake_length[0] and y == snake_length[1]):
            return True


def game_over():
    
    pygame.mixer.music.load("zvuk-urona-v-majnkraft.mp3")
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('', 50), text='Игра Окончена!', fill='red')
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('', 50), text='\n\nПопробуйте ещё раз', fill='blue')



window = Tk()
window.title('Змейка')
window.resizable(False, False)

score = 0
direction = 'down'

label_score = Label(window, text='Счёт: {}'.format(score), font=('', 40))
label_score.pack()

canvas = Canvas(window, height=WINDOW_HEIGHT,
                width=WINDOW_WIDTH, bg=BACKGROUND_COLOR)
canvas.pack()

window.geometry('1200x800')

window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))

snake = Snake()
food = Food()

move(snake, food)

window.mainloop()
