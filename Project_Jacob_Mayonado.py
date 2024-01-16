import pygame
import time
import random
import spritesheet
import os
import sys
#Below is used for handling the paths for any image files when you run the code as an exe file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path=getattr(sys,'_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


pygame.font.init() #initialize font

WIDTH, HEIGHT = 1600,900

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("The Crown of the Slime King")

BG = pygame.transform.scale(pygame.image.load(resource_path("Dungeon1.jpg")), (WIDTH, HEIGHT))#used to take a jpg image that I have in the same directory and put it onto the screen

sprite_sheet_image = pygame.image.load(resource_path('idle.png')).convert_alpha() #convert alpha part is just so that the transparent pixels of the png are actually transperant this loads in the sprite png
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image) #this uses the SpriteSheet class from the spritesheet.py file to create a spritesheet from an image
slimeKing_image = pygame.image.load(resource_path('slimeKingIdle.png')).convert_alpha()
sprite_sheet_slimeKing = spritesheet.SpriteSheet(slimeKing_image)


clock = pygame.time.Clock() #creates the clock object for use in the while run loop
arrow_image = pygame.image.load(resource_path("Arrow.png"))
slimeKing = pygame.image.load(resource_path("SlimeKing.png"))

star_count = 0

PLAYER_VEL = 2 #player movement speed
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 32
STAR_WIDTH = 20
STAR_HEIGHT = 40
STAR_VEL = 3
stars = []
hit = False #for collision with the player and the stars 
star_count += clock.tick(60) #makes it so the while loop only runs a maximum number of 60 times per second




FONT = pygame.font.SysFont("comicsans", 30) #creates the font
BLACK = (0,0,0,0)

elapsed_time = 0

room = 0 #zero is the starting room this number goes up as the player progresses through the dungeon

entrance = pygame.Rect(700,200,200,20) #this draws the entrance to the dungeon

#############################################################################################
#Pretty much all of the below functions are used for printing text to the screen during different points
#############################################################################################

def display_game_start_text():
	text_lines = [
	    "Welcome to my game The Crown of the Slime King",
	    "To continue after reading any text left click, use the arrow keys to move",
	    "To start the game move forward and enter the dungeon"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()



def display_entrance_text():
	text_lines = [
	    "As you enter the dungeon you hear the door lock behind you as a booming voice says:",
	    "To escape the dungeon and prove yourself worthy of the slime kings crown colllect all three keys",
	    "start with the left most door and work clockwise"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def display_attempt_exit_text():
	text_lines = [
	    "To escape the dungeon you must collect all three keys",
	    "The door to the left contains the green key, the door in the middle contains the orange key,",
	    "and the door on the right contains the red key",
	    "Collect all three keys to escape the dungeon and prove yourself worthy of the slime kings crown"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def display_attempt_enter_room2_text():
	text_lines = [
	    "To enter the second room you must first collect the green key",
	    "To get the green key enter the left most room"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def display_attempt_enter_room3_text():
	text_lines = [
	    "To enter the third room you must first collect the orange key",
	    "To get the orange key enter the center room"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def room1_text():
	text_lines = [
	    "Welcome to your first challenge ",
	    "to complete this challenge and gain the green key ",
	    "you must follow the path ahead to the chest but beware of the lava that flows below"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def room2_text():
	text_lines = [
	    "Welcome to your second challenge ",
	    "to complete this challenge and gain the orange key ",
	    "you must avoid the arrows as they fly towards you survive for 20 seconds to gain acccess to the chest"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def room3_text():
	text_lines = [
	    "Welcome to your third and final challenge ",
	    "to complete this challenge and gain the red key",
	    "you must defeat the spirit of the slime kings past", 
	    "To prove yourself worthy and gain acccess to the chest with the final key"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def green_key_collected():
	text_lines = [
	    "Congratulations you collected the green key, two more to go!"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (0, 165, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()


def orange_key_collected():
	text_lines = [
	    "Congratulations you collected the orange key, one more to go!"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (250, 100, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def red_key_collected():
	text_lines = [
	    "Congratulations you collected the red key, you can leave the dunegon now!"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def death_text():
	text_lines = [
	    "YOU DIED!"
	]

	deathFont = pygame.font.SysFont("Cuckoo", 60)

	line_height = deathFont.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = deathFont.render(line, True, (100, 2, 2))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def win_text():
	text_lines = [
	    "YOU WON!"
	]

	deathFont = pygame.font.SysFont("Cuckoo", 60)

	line_height = deathFont.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = deathFont.render(line, True, (0, 255, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()

def combat_instructions():
	text_lines = [
	    "Welcome to your final test defeat the slime king to prove yourself!",
	    "When it is your turn click A to attack, click D to dodge and make it less likely to get hit"
	]


	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y-200))

	pygame.display.flip()

def health_text(player_health, slimeKing_health):
	player_health_text = "PLAYER HEALTH:" + str(player_health)
	slimeKing_health_text = "SLIME KING HEALTH:" + str(slimeKing_health)
	p_health_text = FONT.render(player_health_text,True,(255,255,255))
	sk_health_text = FONT.render(slimeKing_health_text,True,(255,255,255))
	WIN.blit(p_health_text,(400,700))
	WIN.blit(sk_health_text,(900,700))

def player_turn_text():
	text_lines = [
	    "Players Turn"
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y+200))

def slimeKing_turn_text():
	text_lines = [
	    "Slime Kings Turn"
	]


	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y+200))

def miss():
	text_lines = [
	    "Miss!"
	]


	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y+350))

	pygame.display.flip()

def game_finished_text():
	text_lines = [
	    "Thank you for playing my game!",
	    "I hope you enjoyed The Slime Kings Crown",
	    "Congratulations on your new responsibility as the Noble Slime King you've earned it!", 
	]

	line_height = FONT.get_linesize()

	for i, line in enumerate(text_lines):
	    text_surface = FONT.render(line, True, (255, 255, 255), (0, 0, 0))
	    x = WIDTH // 2 - text_surface.get_width() // 2
	    y = HEIGHT // 2 - (len(text_lines) // 2 - i) * line_height
	    WIN.blit(text_surface, (x, y))

	pygame.display.flip()


def main():
	run = True

	#Defining a bunch of boolean statments for various things to check the players location and their "Inventory" meaning which keys they have
	entrance_displayed = False
	enteredDungeon = False
	showAttemptExitText = False
	greenKey = False 
	orangeKey = False
	redKey = False
	inRoom1 = False
	room1text = False
	readStartText = False
	attemptEnterRoom2Text = False
	inRoom2 = False
	room2text = False
	puzzleComplete = False
	attemptEnterRoom3Text = False
	inRoom3 = False
	room3text = False
	room3combat = False
	playerTurn = True
	player_health = 25
	slimeKing_health = 20
	playerAC = 10
	slimeKingAC = 10

	
	star_add_increment = 2000 #something for adding projectiles don't think I am going to use it for the game but following the tutorial
	star_count = 0

	stars = []
	hit = False #for collision with the player and the stars 


	#used to place the players character on the screen and can be updated to adjust where the character is on the screen
	player_x = WIDTH/2 - PLAYER_WIDTH
	player_y = HEIGHT*(3/4) - PLAYER_HEIGHT

	#create animation list
	animation_list = []
	animation_steps = [4,4,4,4]
	action = 0
	last_update = pygame.time.get_ticks()
	animation_cooldown = 100
	frame = 0
	step_counter = 0
	roomnum = 0
	BG = pygame.transform.scale(pygame.image.load(resource_path("Dungeon1.jpg")), (WIDTH, HEIGHT))#used to take a jpg image that I have in the same directory and put it onto the screen
	WIN.blit(BG, (0,0)) #used to draw the image that I have choosen to the screen
	#############################################################################################
	#the below for loop takes each image from the sprite sheet and adds it into a list that has each frame in it
	#############################################################################################
	for animation in animation_steps: #this will repeat for each different animation in the sprite sheet
		temp_img_list = []
		for _ in range(animation): #this adds each type of animation to a temporary list
			temp_img_list.append(sprite_sheet.get_image(step_counter, 32, 32, 1.75,BLACK))
			step_counter += 1
		animation_list.append(temp_img_list) #adds the images from the temporary list to the animation list

	while run:

		#############################################################################################
		#All of the below is used for drawing the arrows that are used in the second room of the dungeon
		#############################################################################################
		star_count += clock.tick(60)
		player_mask = pygame.Rect(player_x,player_y,PLAYER_WIDTH,PLAYER_HEIGHT)

		if star_count > star_add_increment and inRoom2 is True:
			for _ in range(8):
				star_x = random.randint(0, WIDTH - STAR_WIDTH)
				star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
				stars.append(star)

			star_add_increment = max(200, star_add_increment - 50)
			star_count = 0
			
		for star in stars[:]:
			star.y += STAR_VEL
			if star.y > HEIGHT:
				stars.remove(star)
			elif star.y +star.height >= player_y and star.colliderect(player_mask) and inRoom2 and puzzleComplete is False:
				stars.remove(star)
				hit = True
				death_text()
				time.sleep(1)
				player_x = 800
				player_y = 800

		current_time = pygame.time.get_ticks()
		if current_time - last_update >= animation_cooldown: #this loop will basically update the frame every animation cooldown number of miliseconds
			frame += 1
			last_update = current_time
			if frame >= len(animation_list[action]):
				frame = 0

		for event in pygame.event.get():
			if event.type == pygame.QUIT: #allows us to quit out of the screen if the user clicks the x button in the top right of the window
				run = False
				break

		def draw(elapsed_time, stars):

			time_text = FONT.render(f"Time: {round(elapsed_time)}s",1,"white") #creates the text we want to write to the screen
			WIN.blit(time_text,(10,10))

			for star in stars:
				WIN.blit(arrow_image, (star.x,star.y))

		#############################################################################################
		#Event Checker is below check for the user trying to toggle fullscreen or clicking to skip past dialogue
		#############################################################################################
		if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
			# Toggle fullscreen mode
			pygame.display.toggle_fullscreen()
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and entrance_displayed: #used to hide entrance text once the user left clicks
			entrance_displayed = False 
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and showAttemptExitText: #used to hide attempted exit text once the user left clicks
			showAttemptExitText = False 
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and room1text: #used to hide room 1 instruction text once the user left clicks
			room1text = False 
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and readStartText is False: #used to hide room 1 instruction text once the user left clicks
			readStartText = True 
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and attemptEnterRoom2Text: #used to hide room 1 instruction text once the user left clicks
			attemptEnterRoom2Text = False
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and room2text: #used to hide room 1 instruction text once the user left clicks
			room2text = False 
			elapsed_time = 0
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and attemptEnterRoom3Text: #used to hide room 1 instruction text once the user left clicks
			attemptEnterRoom3Text = False
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and room3text: #used to hide room 1 instruction text once the user left clicks
			room3text = False 

		keys = pygame.key.get_pressed()
		#the and statements in these if loops act as boundary conditions so the character cannot go off the screen
		if keys[pygame.K_LEFT] and player_x - PLAYER_VEL >= 0: #allows player to move to the left with the left arrow key
			player_x -= PLAYER_VEL
			action = 2
		if keys[pygame.K_RIGHT] and player_x + PLAYER_VEL + PLAYER_WIDTH < WIDTH: #allows player to move to the right with the right arrow key
			player_x += PLAYER_VEL
			action = 3
		if keys[pygame.K_UP] and player_y - PLAYER_VEL >= 0: #allows player to move up with the up arrow key
			player_y -= PLAYER_VEL
			action = 1
		if keys[pygame.K_DOWN] and player_y + PLAYER_VEL + PLAYER_HEIGHT < HEIGHT: #allows player to move down with the down arrow key
			player_y += PLAYER_VEL
			action = 0

		#############################################################################################
		#All of the below is used to allow the user to enter into different rooms of the dungeon
		#############################################################################################
		
		if entrance.colliderect(player_mask) and enteredDungeon is False:
			BG = pygame.transform.scale(pygame.image.load(resource_path("Dungeon2.jpg")), (WIDTH, HEIGHT))
			player_x = 750
			player_y = 700
			entrance_displayed = True 
			#Below are the locations for the doors in the first area
			exit = pygame.Rect(700,880,100,20)
			door1 = pygame.Rect(0,300,20,100)
			door2 = pygame.Rect(500,0,100,20)
			door3 = pygame.Rect(1580,300,20,100)
			enteredDungeon = True #used to make sure that the entrance text doesn't display again if the user collides with the rectangle because it does not dissapear after first collision
			inDungeon = True #used to make sure that once the user enters other rooms of the dungeon the rectangles for the first three doors no longer can collide with the player

		if enteredDungeon:#using a nested if statment here so I don't get an error saying that the variables for any doors are undefined
			#############################################################################################
			#Collision with exit
			#############################################################################################
			if exit.colliderect(player_mask) and inDungeon:
				if redKey is False: #does not allow the user to exit the dungeon if they do not have the red key
					showAttemptExitText = True
					player_x = 750
					player_y = 700
				else:
					BG.fill(BLACK)
					WIN.blit(BG,(0,0))
					pygame.display.flip()
					game_finished_text()
					time.sleep(10)
					break
					
			#############################################################################################
			#Collision with door 1
			#############################################################################################
			if door1.colliderect(player_mask) and inDungeon and greenKey is False:
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room1.jpg")), (WIDTH, HEIGHT))
				player_x = 1500
				player_y = 410
				inDungeon = False
				inRoom1 = True
				room1text = True
				exitRoom1 = pygame.Rect(1580,400,20,100) #rectangle for the exit to room 1
				#Each of the below are rectangles to act as hazard areas to signify the player falling off of the walk way into the lava
				r1 = pygame.Rect(0,0,300,300)
				r2 = pygame.Rect(300,0,600,400)
				r3 = pygame.Rect(500,400,400,300)
				r4 = pygame.Rect(900,0,700,100)
				r5 = pygame.Rect(1300,100,300,300)
				r6 = pygame.Rect(0,600,300,300)
				r7 = pygame.Rect(300,500,100,400)
				r8 = pygame.Rect(400,800,1200,100)
				r9 = pygame.Rect(1000,200,200,600)
				r10 = pygame.Rect(1200,500,400,300)
				greenkeychest = pygame.Rect(130,420,35,60)
			if door1.colliderect(player_mask) and inDungeon and greenKey is True:
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room1_complete.jpg")), (WIDTH, HEIGHT))
				player_x = 1500
				player_y = 410
				inDungeon = False
				inRoom1 = True
				room1text = True
				exitRoom1 = pygame.Rect(1580,400,20,100) #rectangle for the exit to room 1
				#Each of the below are rectangles to act as hazard areas to signify the player falling off of the walk way into the lava
				r1 = pygame.Rect(0,0,300,300)
				r2 = pygame.Rect(300,0,600,400)
				r3 = pygame.Rect(500,400,400,300)
				r4 = pygame.Rect(900,0,700,100)
				r5 = pygame.Rect(1300,100,300,300)
				r6 = pygame.Rect(0,600,300,300)
				r7 = pygame.Rect(300,500,100,400)
				r8 = pygame.Rect(400,800,1200,100)
				r9 = pygame.Rect(1000,200,200,600)
				r10 = pygame.Rect(1200,500,400,300)
				greenkeychest = pygame.Rect(130,420,35,60)
			#############################################################################################
			#Collision with door 2
			#############################################################################################
			if door2.colliderect(player_mask) and inDungeon and greenKey is True and orangeKey is False:
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room2.jpg")), (WIDTH, HEIGHT))
				player_x = 800
				player_y = 800
				inDungeon = False
				inRoom2 = True
				room2text = True
				wtr_b = pygame.Rect(0,100,1600,600)#sets an area to stop the player from entering into the ware
				wtr_a1 = pygame.Rect(0,100,700,600)#used to create the water boundaries for after the user has survived the space invaders type puzzle and the bride rises
				wtr_a2 = pygame.Rect(900,100,700,600)
				exitroom2 = pygame.Rect(750,880,100,20)
				orangekeychest = pygame.Rect(750,170,100,50)
			if door2.colliderect(player_mask) and inDungeon and orangeKey is True:
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room2_Key_Collected.jpg")), (WIDTH, HEIGHT))
				player_x = 800
				player_y = 800
				inDungeon = False
				inRoom2 = True
				wtr_b = pygame.Rect(0,100,1600,600)#sets an area to stop the player from entering into the ware
				wtr_a1 = pygame.Rect(0,100,700,600)#used to create the water boundaries for after the user has survived the space invaders type puzzle and the bride rises
				wtr_a2 = pygame.Rect(900,100,700,600)
				exitroom2 = pygame.Rect(750,880,100,20)
				orangekeychest = pygame.Rect(750,170,100,50)

			if door2.colliderect(player_mask) and inDungeon and greenKey is False:
				attemptEnterRoom2Text = True
				player_x = 500
				player_y = 20
			#############################################################################################
			#Collision with door 3
			#############################################################################################
			if door3.colliderect(player_mask) and inDungeon and orangeKey is False:
				attemptEnterRoom3Text = True
				player_x = 1300
				player_y = 320
			if door3.colliderect(player_mask) and inDungeon and orangeKey is True:
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room3.jpg")), (WIDTH, HEIGHT))
				player_x = 100
				player_y = 420
				inDungeon = False
				inRoom3 = True
				room3Text = True
				exitroom3 = pygame.Rect(0,400,20,100)
				slimeKingMask = pygame.Rect(1420,420,100,100)


			#############################################################################################
			#inRoom 1 Code
			#############################################################################################
			if inRoom1:
				if exitRoom1.colliderect(player_mask):
					BG = pygame.transform.scale(pygame.image.load(resource_path("Dungeon2.jpg")), (WIDTH, HEIGHT))
					inDungeon = True
					inRoom1 = False
					player_x = 100
					player_y = 310
				if r1.colliderect(player_mask) or r2.colliderect(player_mask) or r3.colliderect(player_mask) or r4.colliderect(player_mask) or r5.colliderect(player_mask) or r6.colliderect(player_mask) or r7.colliderect(player_mask) or r8.colliderect(player_mask) or r9.colliderect(player_mask) or r10.colliderect(player_mask):
					#Displays a death text and resets the character to the beginning of the path if they touch the lava
					death_text()
					time.sleep(1)
					player_x = 1500
					player_y = 410
				if greenkeychest.colliderect(player_mask) and greenKey is False:
					greenKey = True
					green_key_collected()
					time.sleep(1)
					BG = pygame.transform.scale(pygame.image.load(resource_path("Room1_complete.jpg")), (WIDTH, HEIGHT))
			if not inRoom2:
				elapsed_time = 0
			#############################################################################################
			#inRoom 2 Code
			#############################################################################################
			if inRoom2:
				if elapsed_time == 0:
					start_time = time.time() #marks the start time of the game
				if exitroom2.colliderect(player_mask):
					BG = pygame.transform.scale(pygame.image.load(resource_path("Dungeon2.jpg")), (WIDTH, HEIGHT))
					inDungeon = True
					inRoom2 = False
					player_x = 550
					player_y = 50
				if wtr_b.colliderect(player_mask) and puzzleComplete is False:
					hit = True
					death_text()
					time.sleep(1)
					player_x = 800
					player_y = 800
				if room2text is False and elapsed_time >= 20 and orangeKey is False:
					puzzleComplete = True
					BG = pygame.transform.scale(pygame.image.load(resource_path("Room2_Puzzle_Done.jpg")), (WIDTH, HEIGHT))
				if wtr_a1.colliderect(player_mask) and puzzleComplete is True:
					death_text()
					time.sleep(1)
					player_x = 800
					player_y = 800
				if wtr_a2.colliderect(player_mask) and puzzleComplete is True:
					death_text()
					time.sleep(1)
					player_x = 800
					player_y = 800
				if orangekeychest.colliderect(player_mask) and orangeKey is False:
					orangeKey = True
					orange_key_collected()
					time.sleep(1)
					BG = pygame.transform.scale(pygame.image.load(resource_path("Room2_Key_Collected.jpg")), (WIDTH, HEIGHT))
			#############################################################################################
			#inRoom 3 Code
			#############################################################################################
			if inRoom3:
				if exitroom3.colliderect(player_mask):
					BG = pygame.transform.scale(pygame.image.load(resource_path("Dungeon2.jpg")), (WIDTH, HEIGHT))
					inDungeon = True
					inRoom3 = False
					player_x = 1300
					player_y = 320
				if slimeKingMask.colliderect(player_mask):
					room3combat = True
					
					

		
		#############################################################################################
		#All of the below is used for either calling a function that draws text to the screen or draws stars or the character
		#############################################################################################

		WIN.blit(BG, (0,0))
		if readStartText is False:
			display_game_start_text()
		elif entrance_displayed:
			display_entrance_text()
		elif showAttemptExitText:
			display_attempt_exit_text()
		elif room1text:
			room1_text()
		elif room2text:
			room2_text()
		elif room3text:
			room3_text()
		elif attemptEnterRoom2Text:
			display_attempt_enter_room2_text()
		elif attemptEnterRoom3Text:
			display_attempt_enter_room3_text()
		elif room3combat:
			BG.fill(BLACK)
			health_text(player_health,slimeKing_health)
			if playerTurn:
				player_turn_text()
			else:
				slimeKing_turn_text()
			inRoom3 = False
			animation_list_combat = []
			step_counter = 0
			#############################################################################################
			#the below for loop takes each image from the sprite sheet and adds it into a list that has each frame in it
			#############################################################################################
			for animation in animation_steps: #this will repeat for each different animation in the sprite sheet
				temp_img_list = []
				for _ in range(animation): #this adds each type of animation to a temporary list
					temp_img_list.append(sprite_sheet.get_image(step_counter, 32, 32, 10,BLACK))
					step_counter += 1
				animation_list_combat.append(temp_img_list) #adds the images from the temporary list to the animation list

			##############################################################################################
			#Using the below loop to create an animation for the king slime during the final combat
			##############################################################################################
			animation_list2 = []
			animation_steps2 = [4,4,4,4]
			action2 = 0
			step_counter2 = 0
			for animation in animation_steps2: #this will repeat for each different animation in the sprite sheet
				temp_img_list2 = []
				for _ in range(animation): #this adds each type of animation to a temporary list
					temp_img_list2.append(sprite_sheet_slimeKing.get_image(step_counter2, 32, 32, 10,BLACK))
					step_counter2 += 1
				animation_list2.append(temp_img_list2) #adds the images from the temporary list to the animation list
			WIN.blit(animation_list_combat[3][frame],(400,300))
			WIN.blit(animation_list2[2][frame],(900,300))
			combat_instructions()
			if keys[pygame.K_a] and playerTurn:
				toHit = random.randint(1,20)
				if toHit >= slimeKingAC:
					slimeKing_health -= random.randint(1,10)
					time.sleep(1)
				else:
					miss()
					time.sleep(1)
				playerTurn = False
			elif keys[pygame.K_d] and playerTurn:
				playerAC = 15
				print(playerAC)
				playerTurn = False
			elif playerTurn is False:
				toHit = random.randint(1,20)
				if toHit >= playerAC:
					player_health -= random.randint(1,8)
					time.sleep(1)
				else:
					miss()
					time.sleep(1)
				playerAC = 10
				playerTurn = True
			if slimeKing_health <= 0:
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room3.jpg")), (WIDTH, HEIGHT))
				win_text()
				time.sleep(1)
				room3combat = False
				inRoom3 = True
				BG = pygame.transform.scale(pygame.image.load(resource_path("Room3.jpg")), (WIDTH, HEIGHT))
				player_x = 100
				player_y = 420
				redKey = True
				WIN.blit(BG,(0,0))
				pygame.display.flip()
				red_key_collected()
				time.sleep(1)
			if player_health <= 0:
				death_text()
				time.sleep(1)
				player_health = 25
				slimeKing_health = 20





			

		else:
			WIN.blit(animation_list[action][frame], (player_x, player_y))
		if inRoom2 and room2text is False and elapsed_time < 20 and orangeKey is False:
			elapsed_time = time.time() - start_time 
			if hit:
				elapsed_time = 0
				hit = False
			draw(elapsed_time, stars)
		if inRoom3:
			WIN.blit(slimeKing,(1420,420))
		

		pygame.display.update()


	pygame.quit()


main()