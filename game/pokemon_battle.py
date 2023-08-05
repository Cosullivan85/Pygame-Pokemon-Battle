import pygame

pygame.init()
pygame.font.init()
print(pygame.font.get_fonts())

# create the game window
game_width = 960
game_height = 720
FPS = 30
size = (game_width, game_height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pokemon Battle")
clock = pygame.time.Clock()
font = pygame.font.SysFont("cascadia", 48)

# define colors
black = (0, 0, 0)
gold = (218, 165, 32)
grey = (200, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

# Images
titleImg = pygame.image.load("data/img/Pokémon_logo.svg")


def displayTitleImage():
    # Centre the tile image on the screen
    screen.blit(
        titleImg,
        (
            (game_width / 2) - (titleImg.get_width() / 2),
            (game_height / 2) - (titleImg.get_height() / 2),
        ),
    )
    introText = font.render("Press any Key", True, black)
    screen.blit(
        introText,
        (
            (game_width / 2) - (introText.get_width() / 2),
            (game_height / 2) - (introText.get_height() / 2) + 150,
        ),
    )


# Intial Game state
game_status = "intro"

while game_status != "quit":
    # 1 Process input/events
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = "quit"

        # detect keypress
        if event.type == pygame.KEYDOWN:
            if game_status == "intro":
                game_status = "select_pokemon"

    # 2 Draw/render
    if game_status == "intro":
        screen.fill(white)
        displayTitleImage()

    if game_status == "select_pokemon":
        screen.fill(white)

    pygame.display.flip()

pygame.quit()
