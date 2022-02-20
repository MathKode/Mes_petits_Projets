#Coded by BiMathAx
from moviepy.editor import *
from PIL import Image
import pygame

pygame.init()
clock = pygame.time.Clock()
FPS = 20

name=str(input("Nom du fichier video avec extension : "))
pas=float(input("Pas (duré en seconde entre 2 image virgule avec un .) : "))
print("--------\nSqueeze P to change of picture,\n L to going back (last picture),\n S to save the point of cursor,\n Q to quit\n--------")
#Load
try:
    clip1 = VideoFileClip(name)
except:
    exit("Nom de vidéo INVALIDE")
width = clip1.w
height = clip1.h
print("Resizing...",end="\r")
while width > 750 or height > 650:
    clip1 = clip1.resize(0.9)
    width = clip1.w
    height = clip1.h
print(" "*11,end="\r")
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tracking Manuel")

class curseur:
    def __init__(self):
        self.rect1 = pygame.Rect(0,15,35,5)
        self.rect2 = pygame.Rect(15,0,5,35)
        self.speed = 3
    def move(self,move_ls):
        self.rect1.x += self.speed * move_ls[0]
        self.rect1.y += self.speed * move_ls[1]
        self.rect2.x += self.speed * move_ls[0]
        self.rect2.y += self.speed * move_ls[1]
    def show(self,screen):
        pygame.draw.rect(screen,(0,0,0),self.rect1)
        pygame.draw.rect(screen,(0,0,0),self.rect2)

def load_picture(time, video):
    print("LOADING BACKGROUND...",end="\r")
    frame=video.get_frame(time)
    image = Image.fromarray(frame)
    image.save("Background-TRACKING.png")
    img = pygame.image.load("Background-TRACKING.png")
    print("                     ",end="\r")
    return img

ls=[]
game=True
player=curseur()
time = 0
image=load_picture(time,clip1)
move_ls=[0,0]
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move_ls[1]=1
            if event.key == pygame.K_UP:
                move_ls[1]=-1
            if event.key == pygame.K_RIGHT:
                move_ls[0]=1
            if event.key == pygame.K_LEFT:
                move_ls[0]=-1
            if event.key == pygame.K_p:
                time+=pas
                image=load_picture(time,clip1)
            if event.key == pygame.K_l:
                time-=pas
                image=load_picture(time,clip1)
            if event.key == pygame.K_s:
                x=player.rect1.x + 17
                y=player.rect1.y + 2
                y=height-y
                print(f"Point n°{len(ls)+1}: ",x,y)
                ls.append([str(len(ls)+1),str(x),str(y)])
            if event.key == pygame.K_q:
                file=open("Result-TRACKING.csv","w")
                file.write("Point;X (abscisse);Y (ordonné)")
                for i in ls:
                    file.write(";".join(ls))
                file.close
                print("----- END -----\n\nResult save in Result-TRACKING.csv")
                game=False
        if event.type == pygame.KEYUP:
            move_ls=[0,0]
    player.move(move_ls)
    player.show(screen)
    pygame.display.flip()
    screen.blit(image,(0,0))
    clock.tick(FPS)
    
        
