import pygame

class Ship():
	def __init__(self,ai_settings,screen):
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.centerX = float(self.rect.centerx)
		self.centerY = float(self.rect.centery)
		
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	
		
		
		
		
		'''         little bird             '''
		self.image2 = pygame.image.load('images/bird.bmp')
		self.rect2 = self.image2.get_rect()
		#self.rect2.centerx = self.screen_rect.centerx/2
		#self.rect2.centery = self.screen_rect.centery/2
		self.rect2.x = self.screen_rect.centerx/2
		self.rect2.y = self.screen_rect.centery/2
	def blitme(self):
		self.screen.blit(self.image,self.rect)
		#self.screen.blit(self.image2,self.rect2)
	def update(self):
		#
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerX += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerX -= self.ai_settings.ship_speed_factor
		if self.moving_up  and self.rect.top > 0:
			self.centerY -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centerY += self.ai_settings.ship_speed_factor
		
		self.rect.centerx = self.centerX
		self.rect.centery = self.centerY
			

