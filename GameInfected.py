import pygame
from math import *
                   #Prints the Highscores
files = open('Score.txt','r+')
for line in files:
    if line=='':
        continue
    fbeat=eval(line)
    if str(fbeat[0])=='highscore':
        highscore=fbeat
    if str(fbeat[0])=='name':
        highscoren=fbeat
highscore=highscore[1::]
highscoren=highscoren[1::]
print('\n--------------------HIGHSCORES-----------------------')
x=1
for i in range(len(highscoren)):
    print(str(i+1)+'.\t'+str(highscore[x-2])+'\t'+str(highscoren[x-2]))
    x-=1
    if i==9:
        break
print('\n----------------------------------------------------')
              #updating and printing score function
def scoreupdate(username,score,t):
    files = open('Score.txt','r+')    #opens the file
    for line in files:
        if line=='':
            continue
        fbeat=eval(line)
        if str(fbeat[0])=='highscore':
            highscore=fbeat             #stores a highscore as a list
        if str(fbeat[0])=='name':
            highscoren=fbeat            #stores their name as a list
        if str(fbeat[0])==username:
            ScoreBoard=fbeat          #stores current user score as a list
    if not(t):
        ScoreBoard.append(score)
        highscore.append(score)
    highscore=highscore[1::]
    highscoren=highscoren[1::]
    highscore=sorted(highscore)
    if not(t):
        pos=highscore.index(score)
        highscoren.insert(pos,username)
    ScoreBoard=ScoreBoard[1::]
    HS1=[]
    HS2=[]
    SB=[]
    if t:
        print('\n----------------------------------------------------\n')
        print(username+' Last 10 scores:')
    x=0
    for i in ScoreBoard[::-1]:          #for loop pinting last 10 scores of the user
        SB.insert(0,i)
        x+=1
        if t:
            print (str(x)+'. ',i)
        if x==10:
            break
    if t:
        print('\n----------------------------------------------------')
        print('\n--------------------HIGHSCORE-----------------------')
    x=1
    for i in range(len(highscoren)):      #for loop printing top 10 scores
        HS1.insert(0,highscore[x-2])
        HS2.insert(0,highscoren[x-2])
        if t:
            print(str(i+1)+'.\t\t'+str(highscore[x-2])+'\t\t'+str(highscoren[x-2]))
        x-=1
        if i==9:
            break
    if t:
        print('\n----------------------------------------------------')
    files = open('Score.txt','r+')
    files.read()
    HS1.insert(0,'highscore')
    HS2.insert(0,'name')
    SB.insert(0,username)                    #saves the updated userscore and highscore in the file(Score.txt)
    files.write('\n'+str(HS1))
    files.write('\n'+str(HS2))
    files.write('\n'+str(SB))
    files.close()
    if t:
        print('\nHope you enjoyed the Game, INFECTED!, Bye:)')
        n=input('\n----------------------------------------------------\n')
def login():
    filep = open('password.txt','r+')         #opens file
    lu=0
    x=True
    username = input('Enter username: ')
    for line in filep:
        lu+=1
        usp=eval(line)
        if usp[0]==username:                #checks if the username is present in the username list
            password = input('Enter password: ')
            if usp[1]==password:             #checks if the password matches the password for the username given
                x=False
                print('\nLogged in successfully!\nPlay Infected \n')
                break
    if x:                                #if any of the info given is not matching
        print('\ninvalid information\n')
        x=input('Do you want to sign up or try login again?(s/l) :')   
        if x=='s' or x=='S':
            signup()                     #asks to login or signup
        else:
            login()
    return (username)
countvalue=0
        #Sign up Function
def signup():
    x=False
    filep = open('password.txt','r+')       #opens file with user-pass
    files = open('Score.txt','r+')      #opens file with userscore, highscore
    newUser = input('\nChoose new username: ')
    for line in filep:
        usp=eval(line)                   #checks if the username given is taken by anyone else before
        if usp[0]==newUser:
            x=True
    if not(x):
        newPass = input('Enter new password: ')
        filep.read()
        files.read()
        filep.write('\n["'+str(newUser)+'","'+str(newPass)+'"]')     #adds the user-pass list to file(password)
        files.write("\n"+"['"+str(newUser)+"',]")                     #adds a list for  user last 10 scores
        print('\nLogin to your new account\n')
        filep.close()
        files.close()
        username=login()
        return(username)          #returns scores
    else:
        print('Username not available')
        signup()                #if username is already taken, them again signup function
loop=True
while loop:
    n=input('\nLogin or Sign up to play Infected(L/S) :')     #asks if to login or signup
    if n.lower()=='l':
        username=login()
        loop=False
    elif n.lower()=='s':
        username=signup()
        loop=False
pygame.init()
win=pygame.display.set_mode((852,481))   #Initiation of Pygame
pygame.display.set_caption('Infected')
print('Enjoy :)')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
fbg = pygame.image.load('fbg.jpg')                                #defining all  imgaes
char = pygame.image.load('standing.png')
heart = pygame.image.load('heart.png')
heartt= pygame.transform.scale(heart, (64,64))
bulletr = pygame.image.load('bulletr.png')
bulletl = pygame.image.load('bulletl.png')
bulletr= pygame.transform.scale(bulletr, (16,16))
bulletl= pygame.transform.scale(bulletl, (16,16))
clock=pygame.time.Clock()
backg=pygame.image.load('backg5.jpg')
backfg=pygame.image.load('backfg5.jpg')
backg5= pygame.transform.scale(backg, (852,600))
backfg5= pygame.transform.scale(backfg, (852,600))  #scaling the background
backg=pygame.image.load('backg3.jpg')
backfg=pygame.image.load('backfg3.jpg')
backg3= pygame.transform.scale(backg, (852,481))
backfg3= pygame.transform.scale(backfg, (852,481))
backg=pygame.image.load('backg4.jpg')
backfg=pygame.image.load('backfg4.jpg')
backg4= pygame.transform.scale(backg, (852,481))
backfg4= pygame.transform.scale(backfg, (852,481))



start=False
scorelevel=100
NGame=0
sl=0
sdelay=0
c=0
g=450           #Variables
t=425
score=0
gt=240
gy=0
cb=6
level=0
on=0
mac=0
tr=0
lt=0
shoot=False
shootpro=False
invert=0
Pause=False





class player(object):
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.vel = 0
        self.t = 1
        self.jh =20                        #Defining Features of the man
        self.isspace=False
        self.right=False
        self.left=False
        self.height=height                 
        self.width=width               
        self.walkCount=0
        self.facing=1
        self.hitbox=(self.x+17,self.y+12,29,52)
        self.hit1=False
        self.health=3
    def draw(self,win):       #draw function
        if self.walkCount==27:
            self.walkCount=0
        if self.right:
            self.facing=1
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))   #updating the pic of the man also moving the man to right
            self.walkCount+=1
        elif self.left:
            self.facing=-1
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))    #updating the pic of the man also moving the man to right
            self.walkCount+=1
        else:
            win.blit(char,(self.x,self.y))
        self.hitbox=(self.x+25,self.y+12,16,52)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)    #box around the man to check if it have hit the goblin
    def hit(self):
        global c
        global g
        self.health-=1
        c+=g
class projectile(object):
    def __init__(self,x,y,radius,colour,facing):
        if facing<0:
            self.x=x-16
        else:
            self.x=x
        self.y=y-5
        self.radius=radius         #Defining the features of the bullet
        self.colour=colour
        self.facing=facing
        self.vel=8*facing
    def draw(self,win):
        if self.facing>0:
            win.blit(bulletr,(self.x,self.y))#right  #updates and draws the bullet
        else:
            win.blit(bulletl,(self.x,self.y))#left
class projectilep(object):
    def __init__(self,x,y,radius,colour,facing,level):
        self.facing=facing
        self.x=x
        self.y=y
        self.radius=radius          #Defining the features of the bulletpro
        self.colour=colour        
        self.vel=7*facing
        self.life=8*(level//2)  
    def draw(self,win):
        pygame.draw.circle(win,(self.colour),(self.x,self.y),self.radius) #update and draws the bullet
class enemy():          #defining features of the goblin
    #goblin images
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width      #goblin charecteristics
        self.vel = 1.5
        self.walkCount=0
        self.health=10
        self.hitbox=(self.x+26,self.y+10,20,50)
    def draw(self,win):
        self.move()    
        if self.walkCount==33:
            self.walkCount=0
        if pos-self.x>=0:
            win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        else:
            win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        #pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        self.hitbox=(self.x+26,self.y+10,20,50)
        pygame.draw.rect(win,(255,0,0),(self.hitbox[0]-6,self.hitbox[1]-20,50,10))
        pygame.draw.rect(win,(0,128,0),(self.hitbox[0]-6,self.hitbox[1]-20,50- 5*(10-self.health),10))
    def move(self):
        global pos
        if pos-self.x>=0:
            self.x+=self.vel
        else:
            self.x-=self.vel
font = pygame.font.SysFont('comicsans',30,True)
man= player(400,64,64,64)   #defining man
goblins=[]       #list of the goblin
ground=350-man.vel
run=True
bullets=[]
pro=[]
clock=pygame.time.Clock()

def gameWin():   #Function which prints the screen
    global gy, on, tr, lt
    d=c//850
    if NGame%4==0:              #if statement for different background
        if d%2==0:
            win.blit(bg,(c-d*850,0))
            win.blit(fbg,(c-(d-1)*850,0))
            win.blit(fbg,(c-(d+1)*850,0))
        else:
            win.blit(fbg,(c-d*850,0))
            win.blit(bg,(c-(d-1)*850,0))
            win.blit(bg,(c-(d+1)*850,0))
    elif NGame%4==1:
        if d%2==0:
            win.blit(backg5,(c-d*850,-120))
            win.blit(backfg5,(c-(d-1)*850,-120))
            win.blit(backfg5,(c-(d+1)*850,-120))
        else:
            win.blit(backfg5,(c-d*850,-120))
            win.blit(backfg5,(c-(d-1)*850,-120))
            win.blit(backg5,(c-(d+1)*850,-120))
    elif NGame%4==3:
        if d%2==0:
            win.blit(backg3,(c-d*850,0))
            win.blit(backfg3,(c-(d-1)*850,0))
            win.blit(backfg3,(c-(d+1)*850,0))
        else:
            win.blit(backfg3,(c-d*850,0))
            win.blit(backg3,(c-(d-1)*850,0))
            win.blit(backg3,(c-(d+1)*850,0))
    else:
        if d%2==0:
            win.blit(backg4,(c-d*850,0))
            win.blit(backfg4,(c-(d-1)*850,0))
            win.blit(backfg4,(c-(d+1)*850,0))
        else:
            win.blit(backfg4,(c-d*850,0))
            win.blit(backg4,(c-(d-1)*850,0))
            win.blit(backg4,(c-(d+1)*850,0))
    font6 = pygame.font.SysFont('ariel',70,False)
    if NGame%4!=1:
        text19=font6.render('Level '+str(level),1,(20,20,20))
        text=font.render('Score =' + str(score),1,(0,0,0))
    else:
        text19=font6.render('Level '+str(level),1,(200,120,200))
        text=font.render('Score =' + str(score),1,(200,120,200))
    win.blit(text19,((340,50)))
    win.blit(text,(360,10))
    if not(start):
        win.blit(text6,(20,140))
        win.blit(text7,(20,160))
        win.blit(text8,(20,180))
        win.blit(text9,(20,200))
        win.blit(text10,(20,220))
        win.blit(text11,(230,100))
    hd=0
    for i in range(man.health):
        win.blit(heartt,(25+hd,25))
        hd+=70
    if man.hit1 and man.health>0:
        gy+=1
        font1 = pygame.font.SysFont('ariel',50,True)
        text1=font1.render('Score -'+str(xyz),1,(128,0,0))
        win.blit(text1,(330,181))
        if gy==75:
            man.hit1=False
            gy=0
    man.draw(win)
    if lt>0:
        font6 = pygame.font.SysFont('ariel',90,False)
        text19=font6.render('Level '+str(level),1,(100,100,100))
        win.blit(text19,((320,180)))
        lt-=1
    for goblin in goblins:
        goblin.x-=man.vel       #moves the goblin
        goblin.draw(win)        #prints the goblin
    for bullet in bullets:
        bullet.draw(win)         #prints the bullet
    for bullet in pro:
        bullet.draw(win)         #prints the bulletpro
    if shootpro:
        font5 = pygame.font.SysFont('ariel',32,True)
        text5=font5.render('Press 2',1,(120,120,200))
        win.blit(text5,(645,70))
    pygame.draw.rect(win,(0,255,0),(600,25,200,35))  #green bar
    pygame.draw.rect(win,(0,0,255),(600,25,mac*(200/(250+level*40)),35))    #blue bar
    pygame.display.update()     #updates the sceen
    #Main Loop
while run:
    if scorelevel<=score:      #Increases level with score
        if log(score//50)/log(2)==level+1:
            scorelevel*=2
            level+=1
            lt=25
    keys=pygame.key.get_pressed()
    if not(start):  #prints the starting screen
        font6 = pygame.font.SysFont('ariel',25,False)
        font7 = pygame.font.SysFont('ariel',45,False)
        text11=font7.render('Press 1 to Start The Game',1,(0,0,0))
        text6=font6.render('d or -> to move RIGHT',1,(0,0,0))
        text7=font6.render('a or <- to move LEFT',1,(0,0,0))
        text8=font6.render('w or ^ to JUMP',1,(0,0,0))
        text9=font6.render('Space bar to SHOOT',1,(0,0,0))
        text10=font6.render('0 to PAUSE',1,(0,0,0))
        if keys[pygame.K_1]:
            c=0
            start=True
    if keys[pygame.K_0] and start: #pauses the game
        Pause=True
    while Pause:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_1]:
            Pause=False
        font7 = pygame.font.SysFont('ariel',45,False)
        text11=font7.render('Press 1 to Start The Game',1,(0,0,0))
        win.blit(text11,(230,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Pause=False
                run=False
    if man.health==0:   #if the man loses all 3 lives
        NGame+=1
        font1 = pygame.font.SysFont('ariel',75,True)
        font2 = pygame.font.SysFont('ariel',50,True)
        text1=font1.render('Game Over',1,(200,0,0))
        text2=font2.render('Score = '+str(score),1,(50,50,50))
        win.blit(text1,(240,170))
        win.blit(text2,(285,240))
        pygame.display.update()
        scoreupdate(username,score,False)
    while man.health==0:   #while loop when life is zero
        keys=pygame.key.get_pressed()
        font3 = pygame.font.SysFont('ariel',38,False)
        text3=font3.render('Press 1 To Play Again',1,(0,0,0))
        win.blit(text3,(270,300))
        pygame.display.update()
        if keys[pygame.K_1]:
            c=0
            score=0
            mac=0
            shootpro=False
            scorelevel=100       #restarts the game
            level=0
            gt=230
            bullets=[]
            pro=[]
            goblins=[]
            man.health=3
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                man.health=1
                run=False
    if gt-level*20==240 and start: #prints Goblin in a specific interval of time
        if len(goblins)/(level+1)>40:
            scalar=15
        else:
            scalar=1.5
        for i in range(int(level*scalar)+2):    #number of goblin increases with level
            a=t/abs(t)
            goblins.append(enemy(man.x+t+i*18*a,355,64,64))
            t*=-1
        gt=0
    elif not(start):
        start=False
    else:
        gt+=1
    pos=man.x
    if sl>=0:
        sl+=1
        if sl>1:
            sl=0
    clock.tick(45)
    for event in pygame.event.get():   #Quits the game when its closed
        if event.type==pygame.QUIT:
            run=False
    for bullet in pro:
        if -6000<bullet.x<6000:     
            bullet.x+=bullet.vel-man.vel     #While loop which check moves the bulletpro
        else:
            pro.pop(pro.index(bullet))        
        for goblin in goblins:
            if bullet.life<0:
                pro.pop(pro.index(bullet))
                break
            if goblin.hitbox[0]<bullet.x<goblin.hitbox[0]+goblin.hitbox[2] and goblin.hitbox[1]<bullet.y<goblin.hitbox[1]+goblin.hitbox[3]:
                score+=goblin.health               #checks if it hits any goblin
                mac+=goblin.health
                bullet.life=bullet.life-1
                goblins.pop(goblins.index(goblin))
                break
    for bullet in bullets:
        if 0<bullet.x<850:
            bullet.x+=bullet.vel-man.vel             #While loop which check moves the bullet
        else:
            bullets.pop(bullets.index(bullet))
            break
        for goblin in goblins:
            if goblin.hitbox[0]<bullet.x<goblin.hitbox[0]+goblin.hitbox[2] and goblin.hitbox[1]<bullet.y<goblin.hitbox[1]+goblin.hitbox[3]:
                score+=1
                mac+=1                                #checks if it hits any goblin
                goblin.health-=1
                bullets.pop(bullets.index(bullet))
                if goblin.health<=0:
                    goblins.pop(goblins.index(goblin))
                break
    for goblin in goblins:
        if (goblin.hitbox[0]<man.hitbox[0]+man.hitbox[2]<goblin.hitbox[0]+goblin.hitbox[2] or man.hitbox[0]<goblin.hitbox[0]+goblin.hitbox[2]<man.hitbox[0]+man.hitbox[2]) and goblin.hitbox[1]<man.hitbox[1]+man.hitbox[3]<goblin.hitbox[1]+goblin.hitbox[3]:
            man.hit()
            man.hit1=True               #Checks if the man and goblin colide
            xyz=len(goblins)
            score-=len(goblins)
            goblins=[]
            c=0
            break
    if man.y<ground:
        man.y+=1*man.t       #Artifical gravity
        man.t+=1              #Accelerates the player if its above the ground
    if man.y>ground:
        if man.jh>2:
            man.jh*=.6
            man.t=1
            man.isspace=True
        else:
            man.jh=20
            man.y=ground
            man.t=1
            man.isspace=False
    if keys[pygame.K_SPACE]and sl==0:
        if len(bullets)<5 :                 #Shoots the bullet if space bar is pressed
            if sdelay==0:
                bullets.append(projectile(man.x+man.width//2,man.y+man.height//2+3,3,(0,0,0),man.facing))
                sl=1
                sdelay=2
            else:
                sdelay-=1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:   #moves the player to left if 'a' or LEFT key is pressed
        man.vel=-5
        c-=man.vel

        man.right=False
        man.left=True
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:     #moves the player to right if 'd' or LEFT key is pressed
        man.vel=5
        c-=man.vel
        man.right=True
        man.left=False
    else:
        man.walkCount=0
        man.vel=0
    if keys[pygame.K_w] or keys[pygame.K_UP]:    #Jumps if w or Up is pressed
        man.isspace=True

    
    if mac>250+level*40:
        mac=250+level*40
    if mac==250+level*40:        #if cindition for shooting the bulletpro if the bar is filled
        shootpro=True
    if shootpro and keys[pygame.K_2]:
        pro.append(projectilep(man.x+man.width//2,man.y+man.height//2+3,8,(0,0,0),man.facing,level))
        shootpro=False
        mac=0
    if man.isspace:
        man.y-=man.jh    
    gameWin()
pygame.quit()
scoreupdate(username,score,True)
