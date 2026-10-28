import pygame

# Initialize Pygame and screen dimensions
pygame.init()
SWIDTH, SHEIGHT = 500, 500

# initialize display
display_surface = pygame.display.set_mode((SWIDTH, SHEIGHT))
pygame.display.set_caption('Adding image and background image')

# load and sacle images
backround_image = pygame.transform.scale(pygame.image.load('backroung 3.jpg').convert(), (SWIDTH, SHEIGHT))
bunny_image = pygame.transform.scale(pygame.image.load('images (6).jpeg').convert_alpha(), (200, 200))
bunny_rect = bunny_image.get_rect(center=(SWIDTH // 2, SHEIGHT // 2 + 110))
text = pygame.font.Font(None, 36).render('Hello World', True,pygame.Color('black'))
text_rect = text.get_rect(center=(SWIDTH // 2, SHEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(backround_image, (0, 0))
        display_surface.blit(bunny_image, bunny_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == '__main__':
    game_loop()