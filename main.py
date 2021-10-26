from perlin_noise import PerlinNoise
import pygame
import window
from map_convertor import MapConvertor
import time

seed = int(time.time())

window = window.Window()

noise = PerlinNoise(octaves=7, seed=seed)

gray_map = MapConvertor.noise_to_gray_map(noise, window.perlin_noise_width)


if __name__ == "__main__":
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        window.clear()
        x, y = pygame.mouse.get_pos()
        new_x = int(x / window.map_zoom)
        new_y = int(x / window.map_zoom)
        print(gray_map[new_y][new_x])

        window.draw_matrix(gray_map)

        window.update()
