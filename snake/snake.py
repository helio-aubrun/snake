import pygame
import sys, random
from pygame import mixer

mixer.init()
mixer.music.load("ressources/menu.mp3")
bg = pygame.image.load("ressources/bg.jpg")
bg = pygame.transform.scale(bg,(800,600))

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
        self.pomme_pos_x = random.randrange(110,690,10)
        self.pomme_pos_y = random.randrange(110,590,10)
        self.pomme = 10
        self.clock = pygame.time.Clock()
        self.snake_pos = []
        self.snake_size = 1
        self.start = True
        self.image = pygame.image.load("ressources/logo.jpg")
        self.image_title = pygame.transform.scale(self.image, (400,200))
        self.score = 0
        self.end_screen = True

    def main(self):
        mixer.music.set_volume(0.2)
        mixer.music.play(-1)
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.start = False
            #self.screen.fill((0,0,0))
            self.screen.blit(bg,(0,0))
            self.screen.blit(self.image_title, (220,50,100,50))
            self.mess("mid", "Press Enter",(350,350,200,5), (255,255,255))
            pygame.display.flip()
        while self.in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self.snake_dir_x != -10:
                        self.snake_dir_x = 10
                        self.snake_dir_y = 0
                    elif event.key == pygame.K_LEFT and self.snake_dir_x != 10:
                        self.snake_dir_x = -10
                        self.snake_dir_y = 0
                    elif event.key == pygame.K_DOWN and self.snake_dir_y != -10:
                        self.snake_dir_x = 0
                        self.snake_dir_y = 10
                    elif event.key == pygame.K_UP and self.snake_dir_y != 10:
                        self.snake_dir_x = 0
                        self.snake_dir_y = -10
            if self.snake_pos_x <= 100 or self.snake_pos_x >=690 or self.snake_pos_y <= 100 or self.snake_pos_y >= 590:
                self.affichage()
                self.mess("big", "Score : ",(320,10,100,50), (255,255,255))
                self.mess("big", "{}".format(str(self.score)),(430,10,100,50), (255,255,255))
                self.limites()
                pygame.display.flip()
                self.end()
                self.end_screen = True
            self.mouvement()
            if self.pomme_pos_x == self.snake_pos_x and self.pomme_pos_y == self.snake_pos_y :
                self.pomme_pos_x = random.randrange(110,690,10)
                self.pomme_pos_y = random.randrange(110,590,10)
                self.snake_size+=1
                self.score+=1
            head = []
            head.append(self.snake_pos_x)
            head.append(self.snake_pos_y)
            self.snake_pos.append(head)
            if len(self.snake_pos) > self.snake_size :
                self.snake_pos.pop(0)
            self.affichage()
            self.bite(head)
            self.mess("big", "Score : ",(320,10,100,50), (255,255,255))
            self.mess("big", "{}".format(str(self.score)),(430,10,100,50), (255,255,255))
            self.limites()
            self.clock.tick(20)
            pygame.display.flip()
        
    def limites(self):
        pygame.draw.rect(self.screen,(255,255,255), (100,100,600,500), 3)

    def mouvement(self):
        self.snake_pos_x+=self.snake_dir_x
        self.snake_pos_y+=self.snake_dir_y

    def affichage(self):
        #self.screen.fill((0,0,0))
        self.screen.blit(bg,(0,0))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.snake_pos_x, self.snake_pos_y, self.snake_body, self.snake_body))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.pomme_pos_x, self.pomme_pos_y, self.pomme, self.pomme))
        for parts in self.snake_pos:
            pygame.draw.rect(self.screen, (0,255,0), (parts[0], parts[1], self.snake_body, self.snake_body))

    def bite(self, head):
        for parts in self.snake_pos[:-1]:
            if head == parts :
                self.end()
                self.end_screen = True

    def mess(self, font, mess, rect, color):
        if font == "small":
            font = pygame.font.SysFont("Lato", 20, False)
        elif font == "mid":
            font = pygame.font.SysFont("Lato", 30, False)
        elif font == "big":
            font = pygame.font.SysFont("Lato", 40, False)
        message = font.render(mess, True, color)
        self.screen.blit(message, rect)

    def restart(self):
        self.snake_pos_x = 300
        self.snake_pos_y = 300
        self.snake_dir_x = 0
        self.snake_dir_y = 0
        self.snake_pos = []
        self.snake_size = 1
        self.score = 0
    
    def end(self):
        while self.end_screen:
            self.mess("big","Game Over", (320,200,200,5),(255,255,255))
            pygame.display.flip()
            pygame.time.wait(1000)
            self.mess("mid","Press Enter To Replay", (290,300,200,5),(255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.restart()
                        self.end_screen = False

if __name__ == "__main__":
    pygame.init()
    jeux().main()
    pygame.quit()