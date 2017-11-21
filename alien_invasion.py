import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

''' 
	项目入口,主函数.
	负责各种初始化.页面组件绘制



'''
def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("外星人")
	ship = Ship(ai_settings,screen)
	alien = Alien(ai_settings,screen)
	aliens = Group()
	bullets = Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullet(bullets)
		gf.update_aliens(aliens)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()
