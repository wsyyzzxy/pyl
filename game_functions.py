import sys
import pygame

def check_events(ship):
	''' 响应鼠标键盘事件 '''
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit
				#按键类型
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ship)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ship)
				
def check_keyup_events(event,ship):
	print('keyup event.key=> ',event.key)
	if event.key == pygame.K_RIGHT \
	or event.key == pygame.K_LEFT \
	or event.key == pygame.K_UP \
	or event.key == pygame.K_DOWN:
		ship.moving_right = False
		ship.moving_left = False
		ship.moving_up = False
		ship.moving_down = False
def check_keydown_events(event,ship):
	print('keydown event.key=> ',event.key)
	if event.key == pygame.K_RIGHT:					
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
		
def update_screen(ai_settings,screen,ship):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	pygame.display.flip()
	
