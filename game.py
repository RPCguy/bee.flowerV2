import pgzrun
import random

score=0
game_over=False

TITLE="BumbleGameV1"
HEIGHT=500
WIDTH=600

bee=Actor("bee")
bee.pos=(100,100)

flower=Actor("flower")
flower.pos=(200,50)

def draw():
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score: "+str(score),color="black",topleft=(10,10))

    if game_over==True:
        screen.fill("#FF595E")
        screen.draw.text("Time Is Up! :() Your Score Is: "+str(score),color="#FFCA3A",midtop=(300,10),fontsize=40)

def place_flower():
    flower.x = random.randint(60,540)
    flower.y = random.randint(60,460)


def time_up():
    global game_over
    game_over=True

def update():
    global score
    if keyboard.left:
        bee.x -=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        place_flower()
        score+=10

clock.schedule(time_up,40.1)
        
pgzrun.go()