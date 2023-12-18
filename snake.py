import pygame
import sys, random

class jeux:

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake")
        self.in_game = True
        self.snake_pos_x = 300
        self.snake_pos_y = 300
        self.snake_dir_x = 0
        self.snake_dir_y = 0
        self.snake_body = 10

    def main(self):
        while self.in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.snake_dir_x = 0.1
                        self.snake_dir_y = 0
                    if event.key == pygame.K_LEFT:
                        self.snake_dir_x = -0.1
                        self.snake_dir_y = 0
                    if event.key == pygame.K_DOWN:
                        self.snake_dir_x = 0
                        self.snake_dir_y = 0.1
                    if event.key == pygame.K_UP:
                        self.snake_dir_x = 0
                        self.snake_dir_y = -0.1
            if self.snake_pos_x <= 100 or self.snake_pos_x >=700 or self.snake_pos_y <= 100 or self.snake_pos_y >= 600:
                sys.exit()
            self.snake_pos_x += self.snake_dir_x
            self.snake_pos_y += self.snake_dir_y
            self.screen.fill((0,0,0))
            pygame.draw.rect(self.screen, (0, 255, 0), (self.snake_pos_x, self.snake_pos_y, self.snake_body, self.snake_body))
            self.limites()
            pygame.display.flip()
        
    def limites(self):
        pygame.draw.rect(self.screen,(255,255,255), (100,100,600,500), 3)

if __name__ == "__main__":
    pygame.init()
    jeux().main()
    pygame.quit()