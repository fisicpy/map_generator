import pygame
import config


class Window:
    def __init__(self, name="Map generator", perlin_noise_width=config.perlin_noise_width):
        self.perlin_noise_width = perlin_noise_width
        pygame.init()
        self.surface = pygame.display.set_mode(
            (
                self.perlin_noise_width * config.zoom,
                self.perlin_noise_width * config.zoom
             )
        )
        pygame.display.set_caption("Map generator")
        self.clock = pygame.time.Clock()
        self.map_zoom = config.zoom

    def draw_matrix(self, matrix):
        for line_index, line in enumerate(matrix):
            for pixel_index, pixel in enumerate(line):
                if pixel < 55:
                    color = (3, 58, 100)
                elif 55 <= pixel < 80:
                    color = (0, 90, 159)
                elif 80 <= pixel < 95:
                    color = (7, 151, 200)
                elif 95 <= pixel < 125:
                    color = (0, 167, 224)
                elif 125 <= pixel < 136:
                    color = (38, 179, 227)
                elif 136 <= pixel < 142:
                    color = (255, 235, 150)
                elif 142 <= pixel < 152:
                    color = (240, 217, 123)
                elif 152 <= pixel < 165:
                    color = (79, 224, 119)
                elif 165 <= pixel < 185:
                    color = (47, 200, 90)
                elif 185 <= pixel < 205:
                    color = (25, 177, 68)
                elif pixel >= 205:
                    color = (231, 231, 231)
                else:
                    color = (pixel, pixel, pixel)
                pygame.draw.rect(
                    self.surface,
                    color,
                    (
                        pixel_index * self.map_zoom,
                        line_index * self.map_zoom,
                        self.map_zoom,
                        self.map_zoom
                    )
                )

    def clear(self):
        self.surface.fill((0, 0, 0))

    # noinspection PyMethodMayBeStatic
    def update(self):
        pygame.display.flip()
        self.clock.tick(config.fps)
