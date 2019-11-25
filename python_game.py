import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
white = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
green = (34,177,76)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Squares')

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]


SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def set_level(score, SPEED):
	if score < 20:
		SPEED = 5
	elif score < 40:
		SPEED = 8
	elif score < 60:
		SPEED = 12
	else:
		SPEED = 15
	return SPEED				

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					intro = False
				if event.key ==pygame.K_q:
					pygame.quit()
					quit()
					
		gameDisplay.fill(white)
		message_to_screen("Welcome to Squares",green,-100,"large")
		message_to_screen("The more Squares you dogdge the more scores you get",black,-30)
		message_to_screen("If you knock the blue squares you lose",black,-50)
		message_to_screen("Press C to play, P to pause or Q to Quit.",black,180)
		
		pygame.display.update()
		clock.tick(15)					 		
		
#def text_to_button(msg, color, buttonx, buttony, buttonWIDTH, buttonHEIGHT,
#textSurf, textRect = text_objects(msg,color,size)
#text_rect.center = ((buttonx+(buttonWIDTH/2)), buttony+(buttonHEIGHT/2))
#gameDisplay.blit(textSurf, textrect)

	

#def message_to_screen(msg,color, y_displace = 0, size = "small"):
	#textSurf, textRect = text_objects(msg,color,size)
	#textRect.center = (int(display_width / 2), int(display_height / 2)+y_di
	#gameDisplay.blit(textSurf, textRect)
	
def paused():
	
	paused = True
	
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
					
				elif event.key == pygame.K_q:
				 quit()	
				 
		gameDisplay.fill(white)
		message_to_screen("Paused", black,-100,size="large")
		
		message_to_screen("Press C to continue, P to pause or Q to quit.", black, 25)
		pygame.display.update()
		clock.tick(5)
					 
						
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
		
def update_enemy_positions(enemy_list, score):
	for idx, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += SPEED
		else:
			enemy_list.pop(idx)
			score += 1
	return score  		
			
def collision_check(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True
	return False		
					
def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]
	
	e_x = enemy_pos[0]
	e_y = enemy_pos[1]
	
	if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
		if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
			return True
	return False		

while not game_over:
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()
			
		if event.type == pygame.KEYDOWN:
			
			x = player_pos[0]
			y = player_pos[1]
			 
			if event.key == pygame.K_LEFT:
				x -= player_size
			elif event.key == pygame.K_RIGHT:
				x += player_size
				
			elif event.key == pygame.K_p:
				pause()	
				
			player_pos = [x,y]
						
	screen.fill(BACKGROUND_COLOR)
	
	
	drop_enemies(enemy_list)
	score = update_enemy_positions(enemy_list, score)
	
	text = "Score:" + str(score)
	
	label = myFont.render(text, 1, YELLOW)
	screen.blit(label, (WIDTH-200, HEIGHT-40))
	SPEED = set_level(score, SPEED)
	
	if collision_check(enemy_list, player_pos):
		game_over = True
		break
				
	draw_enemies(enemy_list)	 			
	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

#def game_intro():
	#intro = True
	#while intro:
		#for event in pygame.event.get():
			#if event.type == pygame.QUIT:
				#Pygame.quit()
				#quit()
			
			#if event.key == pygame.K_c:
				#intro = False
			#elif event.key == pygame.K_q:
				#pygame.quit()
				#quit()
	
	#gameDisplay.fill(white)
	#message("Welcome to Squares!",green,-100,size="large")
	#message("The objective is to dodge the dropping squares",black,-30
	
	
	#pygame.draw.rect(gameDisplay,green,(150,500,100,50))
	#pygame.draw.rect(gameDisplay,yellow,(350,500,100,50))
	#pygame.draw.rect(gameDisplay,red,(550,500,100,50))
	
	#text_to_button("play", black, 150,500,100,50)
	
						
	
	clock.tick(30)
	
	pygame.display.update()		
