import random
import time

import pygame

pygame.init()

color_1 = (255, 255, 255)  # white color
color_2 = (255, 255, 102)  # yellow color
color_3 = (0, 0, 0)  # black color
color_4 = (213, 200, 80)  # color
color_5 = (0, 355, 0)  # green color
color_6 = (255, 0, 0)  # red color


box_length = 900
box_height = 600

add_caption = pygame.display.set_mode(box_length, box_height)
pygame.display.set_caption("Snake Game")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10
