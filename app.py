import random

import pygame

pygame.init()

# Define colors
color_1 = (255, 255, 255)  # White (used for pause symbol)
color_2 = (255, 255, 102)  # Yellow (snake and text)
color_3 = (0, 0, 0)  # Black (unused here)
color_4 = (213, 200, 80)  # Unused in UI
color_5 = (255, 165, 0)  # Orange (food)
color_6 = (255, 0, 0)  # Red (pause button and game over)
color_bg = (40, 50, 60)  # Dark gray (background)
color_grid = (60, 70, 80)  # Light gray (grid lines)

# Window dimensions
box_length = 900
box_height = 600
header_height = 50

add_caption = pygame.display.set_mode((box_length, box_height))
pygame.display.set_caption("Snake Game")

# Game settings
snake_block = 10
snake_speed = 10
timer = pygame.time.Clock()

# Fonts
display_style = pygame.font.SysFont("arial", 30, "bold")
score_font = pygame.font.SysFont("arial", 40, "bold")
footer_font = pygame.font.SysFont("arial", 12, "bold")

# Footer text
footer_text = footer_font.render(
    "Build with 💙 by the Edd Gachira ©2025", True, color_2
)
footer_rect = footer_text.get_rect(center=(box_length // 2, box_height - 20))

# Pause button rectangle (top-right corner)
# pause_button_rect = pygame.Rect(box_length - 50, 10, 40, 40)


def draw_background():
    """Draw dark gray background with grid lines."""
    add_caption.fill(color_bg)
    for x in range(0, box_length, snake_block):
        pygame.draw.line(add_caption, color_grid, (x, 0), (x, box_height))
    for y in range(0, box_height, snake_block):
        pygame.draw.line(add_caption, color_grid, (0, y), (box_length, y))

    pygame.draw.line(
        add_caption, color_3, (0, header_height), (box_length, header_height), 2
    )


def draw_snake(snake_block, list_snake):
    """Draw snake as yellow circles."""
    for x in list_snake:
        pygame.draw.circle(
            add_caption,
            color_2,
            (x[0] + snake_block // 2, x[1] + snake_block // 2),
            snake_block // 2,
        )


def draw_food(foodx_pos, foody_pos):
    """Draw food as an orange circle."""
    pygame.draw.circle(
        add_caption,
        color_5,
        (foodx_pos + snake_block // 2, foody_pos + snake_block // 2),
        snake_block // 2,
    )


def draw_score(score):
    """Display live score in top-right corner."""
    value = score_font.render(f"Score: {score}", True, color_2)
    add_caption.blit(value, [box_length - 200, 10])


# def draw_pause_button():
#     """Draw red pause button with white pause symbol."""
#     pygame.draw.circle(add_caption, color_6, pause_button_rect.center, 20)
#     pygame.draw.rect(
#         add_caption,
#         color_1,
#         (pause_button_rect.centerx - 5, pause_button_rect.centery - 10, 3, 20),
#     )
#     pygame.draw.rect(
#         add_caption,
#         color_1,
#         (pause_button_rect.centerx + 5, pause_button_rect.centery - 10, 3, 20),
#     )


def final_score(score):
    """Display final score on game over."""
    value = score_font.render(
        f"Enjoy the snake game ---- Your score is: {score}", True, color_2
    )
    add_caption.blit(value, [10, 10])


def display_msg(msg, color):
    """Display message on game over screen."""
    mssg = display_style.render(msg, True, color)
    add_caption.blit(mssg, [box_length / 6, box_height / 3])


def game_start():
    game_over = False
    game_close = False
    paused = False

    value_x1 = box_length / 2
    value_y1 = box_height / 2
    new_x1 = 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, box_length - snake_block, 10))
    foody_pos = round(random.randrange(header_height, box_height - snake_block, 10))

    while not game_over:
        while game_close:
            add_caption.fill(color_6)
            display_msg("You lost! Press C to play again or Q to quit.", color_4)
            final_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        return game_start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and new_x1 != snake_block:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT and new_x1 != -snake_block:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP and new_y1 != snake_block:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN and new_y1 != -snake_block:
                    new_y1 = snake_block
                    new_x1 = 0
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if pause_button_rect.collidepoint(event.pos):
            #         paused = not paused

        if not paused:
            if (
                value_x1 >= box_length
                or value_x1 < 0
                or value_y1 >= box_height
                or value_y1 < 0
                or value_y1 < header_height
            ):
                game_close = True

            value_x1 += new_x1
            value_y1 += new_y1

            snake_head = [value_x1, value_y1]
            list_snake.append(snake_head)

            if len(list_snake) > snake_len:
                del list_snake[0]

            for x in list_snake[:-1]:
                if x == snake_head:
                    game_close = True

            if value_x1 == foodx_pos and value_y1 == foody_pos:
                foodx_pos = round(random.randrange(0, box_length - snake_block, 10))
                foody_pos = round(random.randrange(0, box_height - snake_block, 10))
                snake_len += 1

        # Draw everything
        draw_background()
        draw_food(foodx_pos, foody_pos)
        draw_snake(snake_block, list_snake)
        draw_score(snake_len - 1)
        # draw_pause_button()
        add_caption.blit(footer_text, footer_rect)

        pygame.display.update()
        timer.tick(snake_speed)

    pygame.quit()
    quit()


game_start()
