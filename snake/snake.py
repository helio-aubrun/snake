import pygame
import sys, random
from pygame import mixer
import os

mixer.init()
mixer.music.load("ressources/menu.mp3")
button_sound = mixer.Sound("ressources/button.mp3")
death_sound = mixer.Sound("ressources/hit.mp3")
growth_sound1 = mixer.Sound("ressources/growth_sound1.mp3")
growth_sound2 = mixer.Sound("ressources/growth_sound2.mp3")
bg = pygame.image.load("ressources/bg.jpg")
bg = pygame.transform.scale(bg,(800,600))
chemin_fichier = os.path.join("ressources", "best_score.txt")
if not os.path.exists(chemin_fichier):
    with open(chemin_fichier, 'w') as fichier:
        fichier.write("0")

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
        self.volume1 = pygame.image.load("ressources/volume1.png")
        self.volume2 = pygame.image.load("ressources/volume2.png")
        self.volume3 = pygame.image.load("ressources/volume3.png")
        self.plus = pygame.image.load("ressources/plus.png")
        self.minus = pygame.image.load("ressources/minus.png")
        self.image_title = pygame.transform.scale(self.image, (400,200))
        self.volume3 = pygame.transform.scale(self.volume3, (75,50))
        self.volume2 = pygame.transform.scale(self.volume2, (75,50))
        self.volume1 = pygame.transform.scale(self.volume1, (75,50))
        self.plus = pygame.transform.scale(self.plus, (30,30))
        self.minus = pygame.transform.scale(self.minus, (30,30))
        self.volume = pygame.image.load("ressources/volume.png")
        self.volume = pygame.transform.scale(self.volume, (75,50))
        self.score = 0
        self.end_screen = True
        self.paused = False

    def main(self):
        with open("ressources/best_score.txt", "r") as fichier_best:
            self.score_best = int(fichier_best.read())
        self.sound=0.3
        self.sound_click = 3
        mixer.music.set_volume(self.sound)
        mixer.music.play(-1)
        while self.start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        button_sound.play()
                        self.start = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if 18 <= y <= 45 :
                        if 91 <= x <=118 and self.sound < 0.3:
                            self.sound_click = self.sound_click + 1
                            self.sound = self.sound_click / 10
                            mixer.music.set_volume(self.sound)
                            mixer.Sound.set_volume(button_sound, self.sound)
                            mixer.Sound.set_volume(death_sound, self.sound)
                            mixer.Sound.set_volume(growth_sound1, self.sound)
                            mixer.Sound.set_volume(growth_sound2, self.sound)
                        elif 127 <= x <= 153 and self.sound > 0.0:
                            self.sound_click = self.sound_click - 1
                            self.sound = self.sound_click / 10
                            mixer.music.set_volume(self.sound)
                            mixer.Sound.set_volume(button_sound, self.sound)
                            mixer.Sound.set_volume(death_sound, self.sound)
                            mixer.Sound.set_volume(growth_sound1, self.sound)
                            mixer.Sound.set_volume(growth_sound2, self.sound)
                    elif 340 <= y <= 380 and 332 <= x <= 476:
                        button_sound.play()
                        self.start = False            
            self.screen.blit(bg,(0,0))
            if self.sound == 0.3:
                self.screen.blit(self.volume, (10,10))
                self.screen.blit(self.volume1, (10,10))
                self.screen.blit(self.volume2, (10,10))
                self.screen.blit(self.volume3, (10,10))
            elif self.sound == 0.2:
                self.screen.blit(self.volume, (10,10))
                self.screen.blit(self.volume1, (10,10))
                self.screen.blit(self.volume2, (10,10))
            elif self.sound == 0.1:
                self.screen.blit(self.volume, (10,10))
                self.screen.blit(self.volume1, (10,10))
            elif self.sound == 0.0:
                self.screen.blit(self.volume, (10,10))
            self.screen.blit(self.plus,(90,18))
            self.screen.blit(self.minus,(125,18))
            self.screen.blit(self.image_title, (220,50,100,50))
            self.mess("mid", "Press Enter",(350,350,200,5), (255,255,255))
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(330,340,150,40),5)
            pygame.display.flip()
        while self.in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
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
                    elif event.key == pygame.K_ESCAPE:
                        button_sound.play()
                        self.paused = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = event.pos
                    if 5 <= x <= 87 and 8 <= y <= 43:
                        button_sound.play()
                        self.paused = True
            if self.snake_pos_x <= 100 or self.snake_pos_x >=690 or self.snake_pos_y <= 100 or self.snake_pos_y >= 590:
                death_sound.play()
                self.affichage()
                self.mess("big", "Score : ",(320,10,100,50), (255,255,255))
                self.mess("big", "{}".format(str(self.score)),(430,12,100,50), (255,255,255))
                self.mess("big", "Best Score : ",(300,50,100,50),(255,255,255))
                self.mess("big", "{}".format(str(self.score_best)),(480,52,100,50), (255,255,255))
                self.limites()
                pygame.display.flip()
                self.end()
                self.end_screen = True
            self.mouvement()
            if self.pomme_pos_x == self.snake_pos_x and self.pomme_pos_y == self.snake_pos_y :
                growth_sound = random.choice([growth_sound1, growth_sound2])
                growth_sound.play()
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
            self.mess("big", "Score : ",(320,10,100,50), (255,255,255))
            self.mess("big", "{}".format(str(self.score)),(430,12,100,50), (255,255,255))
            self.mess("big", "Best Score : ",(300,50,100,50),(255,255,255))
            self.mess("big", "{}".format(str(self.score_best)),(480,52,100,50), (255,255,255))
            self.limites()
            self.bite(head)
            self.mess("mid", "Echap", (15,15,100,50), (255,255,255))
            pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(5,5,85,40),5)
            if self.score > self.score_best:
                moving_sprites.draw(self.screen)
                moving_sprites.update()
            pygame.display.flip()
            if self.paused:
                overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
                overlay.fill((0,0,0,160))
                self.screen.blit(overlay, (0, 0))
                pygame.display.flip()
                rectangle = pygame.Rect(315,340,160,70)
                while self.paused:
                    self.mess("big", "Continue",(325,145,100,50),(255,255,255))
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(315,135,150,50), 5)
                    self.mess("big", "Restart", (340,250,100,50),(255,255,255))
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(325,240,130,50),5)
                    self.screen.fill((0,0,0), rectangle)
                    if self.sound == 0.0:
                        self.screen.blit(self.volume, (325,350))
                    elif self.sound == 0.1:
                        self.screen.blit(self.volume, (325,350))
                        self.screen.blit(self.volume1, (325, 350))
                    elif self.sound == 0.2:
                        self.screen.blit(self.volume, (325,350))
                        self.screen.blit(self.volume1, (325, 350))
                        self.screen.blit(self.volume2, (325,350))
                    elif self.sound == 0.3:
                        self.screen.blit(self.volume, (325,350))
                        self.screen.blit(self.volume1, (325, 350))
                        self.screen.blit(self.volume2, (325,350))
                        self.screen.blit(self.volume3, (325,350))
                    self.screen.blit(self.plus,(405,358))
                    self.screen.blit(self.minus,(440,358))
                    pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(315,340,160,70),5)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            x,y = event.pos
                            print(x,y)
                            if 136 <= y <= 183 and 315 <= x <= 463:
                                button_sound.play()
                                self.paused = False
                            elif 240 <= y <= 287 and 325 <= x <= 450:
                                button_sound.play()
                                self.restart()
                                self.paused = False
                            elif 358 <= y <= 388:
                                if 406 <= x <= 433 and self.sound < 0.3:
                                    self.sound_click = self.sound_click + 1
                                    self.sound = self.sound_click / 10
                                    mixer.music.set_volume(self.sound)
                                    mixer.Sound.set_volume(button_sound, self.sound)
                                    mixer.Sound.set_volume(death_sound, self.sound)
                                    mixer.Sound.set_volume(growth_sound1, self.sound)
                                    mixer.Sound.set_volume(growth_sound2, self.sound)
                                elif 442 <= x <= 468 and self.sound > 0.0:
                                    self.sound_click = self.sound_click - 1
                                    self.sound = self.sound_click / 10
                                    mixer.music.set_volume(self.sound)
                                    mixer.Sound.set_volume(button_sound, self.sound)
                                    mixer.Sound.set_volume(death_sound, self.sound)
                                    mixer.Sound.set_volume(growth_sound1, self.sound)
                                    mixer.Sound.set_volume(growth_sound2, self.sound)
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                button_sound.play()
                                self.paused = False
            self.clock.tick(20)
        
    def limites(self):
        pygame.draw.rect(self.screen,(255,255,255), (100,100,600,500), 3)

    def mouvement(self):
        self.snake_pos_x+=self.snake_dir_x
        self.snake_pos_y+=self.snake_dir_y

    def affichage(self):
        self.screen.blit(bg,(0,0))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.snake_pos_x, self.snake_pos_y, self.snake_body, self.snake_body))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.pomme_pos_x, self.pomme_pos_y, self.pomme, self.pomme))
        for parts in self.snake_pos:
            pygame.draw.rect(self.screen, (0,255,0), (parts[0], parts[1], self.snake_body, self.snake_body))

    def bite(self, head):
        for parts in self.snake_pos[:-1]:
            if head == parts :
                death_sound.play()
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
            if self.score > self.score_best:
                self.mess("mid", "New Best Score : ",(300, 250,200,5),(255,255,255))
                self.mess("mid", "{}".format(str(self.score)),(480,250,100,50), (255,255,255))
                f = open("ressources/best_score.txt", "w")
                f.write(str(self.score))
                f.close()
                with open("ressources/best_score.txt", "r") as fichier_best:
                    self.score_best = int(fichier_best.read())
            self.mess("mid","Press Enter To Replay", (290,300,200,5),(255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        button_sound.play()
                        self.restart()
                        self.end_screen = False

class player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        twinkle=pygame.image.load("ressources/twinkle1.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle2.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle3.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle4.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle5.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle6.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle7.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle8.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle9.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle10.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle11.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle12.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle13.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle14.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle15.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle16.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle17.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle18.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle19.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle20.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle21.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        twinkle=pygame.image.load("ressources/twinkle22.gif")
        twinkle=pygame.transform.scale(twinkle,(150,100))
        self.sprites.append(twinkle)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    
    def update (self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

moving_sprites = pygame.sprite.Group()
players = player(320,3)
moving_sprites.add(players)
if __name__ == "__main__":
    pygame.init()
    jeux().main()
    pygame.quit()