import pygame

def main():
    pygame.init()
    size = width, height = 200, 200
    screen = pygame.display.set_mode(size)
    hide_count = 0
    font = pygame.font.Font(None, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.WINDOWHIDDEN:
                hide_count += 1

        screen.fill("black")

        num = font.render(str(hide_count), True, "red")
        text= num.get_rect(center=(width // 2, height // 2))
        screen.blit(num, text)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()