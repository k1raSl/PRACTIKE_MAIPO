import pygame
import random
import sys

# Инициализация
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def spawn_food(snake):
    """Создает еду в случайной позиции, не занятой змейкой"""
    while True:
        pos = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
               random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if pos not in snake:
            return pos


def draw_game(snake, food, score):
    """Отрисовывает все элементы игры"""
    screen.fill(BLACK)

    # Рисуем змейку
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Рисуем еду
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Рисуем счет
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()


def game_loop():
    """Основной игровой цикл"""
    # Начальные параметры
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (CELL_SIZE, 0)
    food = spawn_food(snake)
    score = 0
    speed = 10
    running = True

    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # Движение змейки
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Проверка столкновения с едой
        if new_head == food:
            score += 1
            food = spawn_food(snake)
            speed += 0.5
        else:
            snake.pop()

        # Проверка столкновения со стенами или собой
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake[1:]):
            return score

        draw_game(snake, food, score)
        clock.tick(speed)

    return score


def main():
    """Главная функция - запуск игры и экран game over"""
    while True:
        score = game_loop()

        # Экран Game Over
        screen.fill(BLACK)
        game_over_text = font.render("GAME OVER!", True, RED)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        restart_text = font.render("Press SPACE to play again or ESC to quit", True, WHITE)

        screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 50))
        screen.blit(score_text, (WIDTH // 2 - 70, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - 250, HEIGHT // 2 + 50))
        pygame.display.flip()

        # Ожидание выбора
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
cat chapter-1.txt

if __name__ == "__main__":
    main()