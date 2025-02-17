import pygame
import requests
import io
import os

pygame.init()
WIDTH, HEIGHT = 600, 450
API_KEY = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def get_map():
    url = f'https://static-maps.yandex.ru/1.x/?ll=135.0,-25.0&spn=30.0,30.0&l=map&apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Ошибка при получении карты:", response.status_code)
        return None

running = True
map_image_data = get_map()

if map_image_data:
    with open("map_image.png", "wb") as f:
        f.write(map_image_data)

image = pygame.image.load("map_image.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (0, 0))
    pygame.display.flip()

if os.path.exists("map_image.png"):
    os.remove("map_image.png")

pygame.quit()
