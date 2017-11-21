import sys
import pygame
from alien import Alien
from bullet import Bullet

'''
	功能函数集合.
	负责键盘事件监听,以及响应的操作函数
'''
def check_events(ai_settings,screen,ship,bullets):
	''' 响应鼠标键盘事件 '''
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				#按键类型
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event,ai_settings,screen,ship,bullets)
			elif event.type == pygame.KEYUP:
				check_keyup_events(event,ai_settings,screen,ship,bullets)
				
def check_keyup_events(event,ai_settings,screen,ship,bullets):
	print('keyup event.key=> ',event.key)
	if event.key == pygame.K_RIGHT \
	or event.key == pygame.K_LEFT \
	or event.key == pygame.K_UP \
	or event.key == pygame.K_DOWN:
		ship.moving_right = False
		ship.moving_left = False
		ship.moving_up = False
		ship.moving_down = False
	
		
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	#print('keydown event.key=> ',event.key)
	if event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_RIGHT:					
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
		
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullet_alowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)			
		
def update_screen(ai_settings,screen,ship,aliens,bullets):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	aliens.draw(screen)
	pygame.display.flip()

def update_bullet(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print(len(bullets))
	
def get_number_aliens_x(ai_settings, alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (ai_settings.screen_height \
	-(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
		
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	alien = Alien(ai_settings, screen)
	alien_width=alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)
		
def create_fleet(ai_settings,screen,ship,aliens):
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height,
		alien.rect.height)

	# Create the fleet of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number,row_number)
	
def update_aliens(aliens):
	aliens.update()
