import pygame
import requests
import os

pygame.init()
print(os.listdir())
os.chdir('WEB. Знакомство с API')

WIDTH, HEIGHT = 600, 450
API_KEY = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Карта Австралии")


def get_map():
    url = f'https://static-maps.yandex.ru/1.x/?ll=135.0,-25.0&spn=30.0,30.0&l=map&apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Ошибка при получении карты:", response.status_code)
        return None


def load_marker_image():
    marker = pygame.image.load("Map Marker.png")
    return pygame.transform.scale(marker, (30, 30))


running = True
map_image_data = get_map()
marker_image = load_marker_image()

if map_image_data:
    with open("map_image.png", "wb") as f:
        f.write(map_image_data)

    image = pygame.image.load("map_image.png")


marker_width, marker_height = marker_image.get_size()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (0, 0))

    center_x = WIDTH // 2 - marker_width // 2  
    center_y = HEIGHT // 2 - marker_height // 2  

    screen.blit(marker_image, (center_x, center_y))

    pygame.display.flip()

if os.path.exists("map_image.png"):
    os.remove("map_image.png")

pygame.quit()