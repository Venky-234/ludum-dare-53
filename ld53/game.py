import pygame 
import random
import time


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.SCALED ,vsync=1)

playerScore = 0
pygame.display.set_caption("ludum dare game")

pygame.font.init()

## loading all objects required images for the game
pencil = pygame.image.load("./res/textures/pencil.png")
egg = pygame.image.load("./res/textures/egg.png")
pill = pygame.image.load("./res/textures/pill.png")
carrot = pygame.image.load("./res/textures/carrot.png")
apple = pygame.image.load("./res/textures/apple.png")
tick = pygame.image.load("./res/textures/tick.png")
cross = pygame.image.load("./res/textures/cross.png")
deliverButton = pygame.image.load("./res/textures/deliverButton.png")
pizza = pygame.image.load("./res/textures/pizza.png")
banana = pygame.image.load("./res/textures/banana.png")
shoes = pygame.image.load("./res/textures/shoes.png")
shelfBackground = pygame.image.load("./res/textures/shelf_background.png")

biker = pygame.image.load("./res/textures/biker1.png")
bikerLeft = pygame.transform.rotate(biker, 30.0)
bikerRight = pygame.transform.rotate(biker, -30.0)

white_car = pygame.image.load("./res/textures/white_car.png")
orange_car = pygame.image.load("./res/textures/orange_car.png")
green_car = pygame.image.load("./res/textures/green_car.png")
purple_car = pygame.image.load("./res/textures/purple_car.png")
red_car = pygame.image.load("./res/textures/red_car.png")
blue_car = pygame.image.load("./res/textures/blue_car.png")

cars = [white_car, orange_car, green_car, purple_car, red_car, blue_car]
displayFont = pygame.font.Font("./res/fonts/data-latin.ttf", 100)
displayFont2 = pygame.font.Font("./res/fonts/data-latin.ttf", 50)

startingPage = pygame.image.load("./res/textures/startingPage.png")
instructionsPage = pygame.image.load("./res/textures/instructions.png")

################
### make sure that the order of objects in list_of_all_objects and the strings of string_of_all_objects are the same 
list_of_all_objects = [pencil, egg, pill, carrot, apple, pizza, banana, shoes]
string_of_all_objects = ["pencil", "egg", "pill", "carrot", "apple", "pizza","banana","shoes"]

itemsInShop = []
carsList = []

shelf_rows = 10
shelf_coloumns = 8 

isGameRunning = True
clock = pygame.time.Clock()

randTimer = 0
def render_object(img, cods):
    Xoffset = 100 
    Yoffest = 0 
    screen.blit(img, (cods[0]+10 + Xoffset, cods[1]+10 + Yoffest))
    pygame.draw.rect(
            screen, 
            (163, 121, 36), 
            pygame.Rect(cods[0] + Xoffset, cods[1] + Yoffest, img.get_width() + 20, img.get_height() + 20)
            ,3
            )

    for i in range(1,10):
        pygame.draw.rect(screen, (163, 121, 36),pygame.Rect(30, i*100 - 8,940,15))

    #screen.blit(shelfBackground, (cods[0]+10 + Xoffset, cods[1]+10 + Yoffest))
    

for i in range(shelf_rows):
    itemsInShop.append([])
    for j in range(shelf_coloumns):
        randomIndex = random.randint(0, len(list_of_all_objects)-1) 
        itemsInShop[i].append([list_of_all_objects[randomIndex], randomIndex])

items_collected = []
isMousePressed = False
readyTodeliver = False
isBikeTurning = False
hasPlayerPassed = True
def selectRandomObject():
    randomRow = random.randint(0, shelf_rows - 1)
    randomColoumn = random.randint(0, shelf_coloumns - 1)
    item = itemsInShop[randomRow][randomColoumn]
    
    return [string_of_all_objects[item[1]],item[1]]

randomObject = selectRandomObject()
print(randomObject)
displayText = displayFont.render(randomObject[0],False, (0, 145, 255))

displayTick = False
displayCross = False

startTimer = False
seconds = 0

totalItemsCollected = 0
noOfItemsToBeCollected = 15 

dis_objs_left = displayFont2.render("items left "+ ":"+ str(noOfItemsToBeCollected - totalItemsCollected), 
                                   False ,
                                   (240, 87, 26)
                                   ) 
bikerCods = [SCREEN_WIDTH/2, SCREEN_HEIGHT/2+300]

noOfCars = 10 

prevValue = random.randint(0, 12)

def releaseCar():
    row = random.randint(0, 3)
    leftOrRight = random.randint(0,1)
    leftOrRight = 0
    X = 0
    ## 0 -> left
    ## 1 -> right
    speed = 3 
    if leftOrRight == 0:
        #X = random.randint(-1, 0)*190
        X = 0
        speed = 8 
    else:
        #X = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 1)*190 
        X = SCREEN_WIDTH 
        speed = -5 
    if leftOrRight == 0:
        carTex = pygame.transform.rotate(cars[random.randint(0 ,len(cars)-1)], -90.00) 
    else:
        carTex = pygame.transform.rotate(cars[random.randint(0 ,len(cars)-1)], 90.00) 
    
    return [carTex, row, leftOrRight, X, speed]

#def initCars():
#    row = random.randint()


for i in range(4):
    carsList.append(releaseCar())
    


#for i in range(noOfCars):
#    print(carsList[i])

isStarted = True
while isStarted:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
        if event.type == pygame.KEYDOWN:
            isStarted = False 
    # rgb(255, 224, 161)
    screen.fill((255, 224, 161))
    screen.blit(startingPage, (0,0))
    pygame.display.flip()
isInstructions = True
while isInstructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            isInstructions = False 
    # rgb(255, 224, 161)
    screen.fill((255, 224, 161))
    screen.blit(instructionsPage, (0,0))
    pygame.display.flip()
gameSeconds = 0

gameTimer = time.time()
while isGameRunning:
    gameSeconds = round(time.time() - gameTimer, 1)
    
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
            exit() 
    screen.fill((255, 224, 161))
       ### collision detection with mouse 
    if totalItemsCollected <  noOfItemsToBeCollected:
        screen.blit(displayText, (1100, 160)) 
        
        for i in range(shelf_rows):
            for j in range(shelf_coloumns):
                if mouseX > j*100 + 100 and mouseX < itemsInShop[i][j][0].get_width() + j*100 +100 + 20 \
                and mouseY > i*100 and mouseY < itemsInShop[i][j][0].get_height() + i*100 +20:
                    if pygame.mouse.get_pressed()[0] and isMousePressed == False:
                        items_collected = itemsInShop[i][j]
                        if randomObject[1] == itemsInShop[i][j][1]:
                            displayTick = True
                            randomIndex = random.randint(0, len(list_of_all_objects)-1) 
                            itemsInShop[i][j] = [list_of_all_objects[randomIndex], randomIndex]
                            isMousePressed = True
                            randomObject = selectRandomObject()
                            print(randomObject[0])
                            displayText = displayFont.render(randomObject[0], False, (2, 143, 250))
                            totalItemsCollected += 1
                            dis_objs_left = displayFont2.render("items left "+ ":"+ str(noOfItemsToBeCollected - totalItemsCollected), 
                                   False ,
                                   (240, 87, 26)
                                   ) 

                        else:
                            displayCross = True
                    


                if pygame.mouse.get_pressed()[0] == False:
                    isMousePressed = False

    else:
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        buttonCods = [1100, 160]
        
        if readyTodeliver == False:
            screen.blit(deliverButton, buttonCods)
            if mouseX > buttonCods[0] and mouseX < 150 + buttonCods[0] \
                and mouseY > buttonCods[1] and mouseY < 80 + buttonCods[1]:
                        if pygame.mouse.get_pressed()[0]:
                            readyTodeliver = True   
                            print("delivery")
            
        ##################### 
 ### render all objects with a box   
    if readyTodeliver == False:
        for i in range(shelf_rows):
            for j in range(shelf_coloumns):
                render_object(itemsInShop[i][j][0], (j*100, i*100)) 
################
    if readyTodeliver == False: 
#        screen.blit(displayText, (1100, 160)) 
        screen.blit(dis_objs_left, (1100, 60))
   ### delivary loop 
    if readyTodeliver == True:
        keys = pygame.key.get_pressed()
        bikeSpeed = 10 
        screen.blit(biker, bikerCods)
        if keys[pygame.K_w]:
            bikerCods[1] -= bikeSpeed 

        if keys[pygame.K_a]:
            bikerCods[0] -= bikeSpeed
           # isBikeTurning = True
           # if keys[pygame.K_d]:
           #     screen.blit(biker, bikerCods)
           # else:
           #     screen.blit(bikerLeft, bikerCods)

        if keys[pygame.K_s]:
            bikerCods[1] += bikeSpeed 

        if keys[pygame.K_d]:
            bikerCods[0] += bikeSpeed 
         #   if isBikeTurning == False:
                #screen.blit(bikerRight, bikerCods)
            #isBikeTurning = True

        #if isBikeTurning == False:
        #    screen.blit(biker, bikerCods)
        #isBikeTurning = False
        speed = 3
        for i in range(len(carsList)):
            screen.blit(carsList[i][0],(carsList[i][3],carsList[i][1]*200+ 100))
            carsList[i][3] += carsList[i][4] 
        itemsTobeDeleted = []
        for i in range(0 ,len(carsList)):
            if (carsList[i][3] > SCREEN_WIDTH and carsList[i][2] == 0) or \
                    (carsList[i][3] < 0 and carsList[i][2] == 1):
                            if bool(random.randint(0,1)):
                                itemsTobeDeleted.append(carsList[i])
                            
                            else:
                                carsList[i] = releaseCar() 
        for i in range(len(carsList)):
            if pygame.Rect.colliderect(pygame.Rect(bikerCods[0], bikerCods[1], biker.get_width(), biker.get_height()), pygame.Rect(carsList[i][3], carsList[i][1]*200+100, carsList[i][0].get_width(), carsList[i][0].get_height())):
                print("collision detected")
                isGameRunning = False
                hasPlayerPassed = False

        for i in range(len(itemsTobeDeleted)):
            #print("car deleted")
            carsList.remove(itemsTobeDeleted[i])
        ## has biker reached top of screen ??
        if bikerCods[1] <= 0:
            hasPlayerPassed = True
            isGameRunning = False

        ## to release a car
        if startTimer == False:
            seconds = time.time()
            randTimer = round(random.uniform(0.3, 0.5), 1) 
            startTimer = True

        if time.time() - seconds >= randTimer:
            carsList.append(releaseCar()) 
            #print("car released")
            startTimer = False

####################################################
    if displayTick == True:
        screen.blit(tick, (1100, 300)) 
        displayCross = False
        if startTimer == False:
            seconds = time.time() 
            startTimer = True

        if time.time() - seconds >= 0.5:
            displayTick = False
            startTimer = False
            seconds = 0

    if displayCross == True:
        screen.blit(cross, (1100, 300)) 
        displayTick = False
        if startTimer == False:
            seconds = time.time() 
            startTimer = True

        if time.time() - seconds >= 0.5:
            displayCross = False
            startTimer = False
            seconds = 0
    timeLeftText = displayFont2.render("time left : " + str(round(30 - gameSeconds, 1)), False, (13, 128, 9))
    screen.blit(timeLeftText, (1050, 400))
    
    if gameSeconds >= 30:
        isGameRunning = False

    clock.tick(60)
    pygame.display.flip()

isPlayerDone = True

while isPlayerDone:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlayerDone = False
            exit()
    screen.fill((255, 224, 161))
    if hasPlayerPassed:
        ### calculate playerScore
        playerScore = (30 - gameSeconds) 
        dispScore = displayFont2.render("customer rating : " + str(playerScore), False,(149, 68, 29))
        screen.blit(dispScore, (400, 500))
    
    else:
        dispScore = displayFont2.render("You have lost", False,(149, 68, 29))
        screen.blit(dispScore, (400, 500))
    pygame.display.flip()
