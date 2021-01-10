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
    screen.fill((255, 255, 255))
    color = (0, 0, 0)
    center = (self.screen_w/2, self.screen_h/2)
    radius = 10
    pygame.draw.circle(screen, color, (0, 0), radius)
    pygame.draw.circle(screen, color, (800, 600), radius)
    pygame.draw.circle(screen, color, center, radius)
    pygame.display.flip()

    
     