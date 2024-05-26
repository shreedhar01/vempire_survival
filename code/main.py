from settings import *
from player import Player

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        #grpups
        self.all_sprites = pygame.sprite.Group()

        #sprites
        self.player = Player((400,400), self.all_sprites)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            #event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   self.running = False

            #update
            self.all_sprites.update(dt)

            #draw
            self.display_surface.fill('black')
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()