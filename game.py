import pygame
class Game:
  def __init__(self, screen_w, screen_h):
    super().__init__()
    pygame.init()
    self.screen_w = screen_w
    self.screen_h = screen_h
    size = [screen_w, screen_h]
    self.screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

  def run(self):
    print("run")
    done = False
    clock = pygame.time.Clock()
    while not done:
      done = self.process_events()
      self.display_frame(self.screen)
      clock.tick(60)
    pygame.quit()



  def process_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return True
    return False

  def display_frame(self, screen):
    screen.fill((51, 153, 255))
    pygame.draw.rect(screen, (102, 204, 0), (0, 500, 800, 100))
    pygame.draw.rect(screen, (255, 153, 51), (300, 350, 200, 200))
    pygame.draw.rect(screen, (255, 204, 153), (50, 350, 200, 200))
    pygame.draw.rect(screen, (255, 153, 153), (550, 350, 200, 200))
    pygame.draw.polygon(screen, (0,0,153), [(275,350), (525,350), (400, 225)])
    pygame.draw.polygon(screen, (0,0,153), [(25,350), (275,350), (150, 225)])
    pygame.draw.polygon(screen, (0,0,153), [(525,350), (775,350), (650, 225)])
    pygame.draw.rect(screen, (102, 51, 0), (375, 450, 50, 100))
    pygame.draw.rect(screen, (102, 51, 0), (125, 450, 50, 100))
    pygame.draw.rect(screen, (102, 51, 0), (625, 450, 50, 100))    
    pygame.draw.circle(screen, (255, 255, 0), (100, 100), 50)
    pygame.display.flip()

    
     