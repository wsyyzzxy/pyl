import sys
import pygame
from alien import Alien
from bullet import Bullet

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
	print(len(bullets))
	
def create_fleet(ai_settings,screen,aliens):
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	number_alien_x = get_number_aliens_x(ai_settings,alien_width)
	create_alien(ai_settings,screen,aliens,number_alien_x)
	
def get_number_aliens_x(ai_settings,alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width
	return int(available_space_x/(2 * alien_width))
	
def create_alien(ai_settings,screen,aliens,alien_number):
	for n in range(alien_number):
		alien = Alien(ai_settings,screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * n
		alien.rect.x = alien.x
		aliens.add(alien)
	
	
		
	
