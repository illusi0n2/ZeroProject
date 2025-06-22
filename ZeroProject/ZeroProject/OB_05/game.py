import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки игры
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()


# Класс для змейки
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]  # Теперь тело - список координат
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == "RIGHT":
            new_head = (head_x + BLOCK_SIZE, head_y)
        elif self.direction == "LEFT":
            new_head = (head_x - BLOCK_SIZE, head_y)
        elif self.direction == "UP":
            new_head = (head_x, head_y - BLOCK_SIZE)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + BLOCK_SIZE)

        self.body.insert(0, new_head)  # Добавляем новую голову
        self.body.pop()  # Удаляем хвост

    def change_direction(self, new_direction):
        if (
                (new_direction == "RIGHT" and self.direction != "LEFT") or
                (new_direction == "LEFT" and self.direction != "RIGHT") or
                (new_direction == "UP" and self.direction != "DOWN") or
                (new_direction == "DOWN" and self.direction != "UP")
        ):
            self.direction = new_direction

    def grow(self):
        self.body.append(self.body[-1])  # Добавляем новый сегмент

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, GREEN, (x, y, BLOCK_SIZE, BLOCK_SIZE))


# Функция для генерации еды
def generate_food():
    while True:
        x = random.randrange(0, WIDTH, BLOCK_SIZE)
        y = random.randrange(0, HEIGHT, BLOCK_SIZE)
        if (x, y) not in snake.body:
            return (x, y)

# Функция отображения счета
def show_score(score):
    font = pygame.font.Font(None, 20)
    text = font.render(f"Счет: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Функция для отрисовки экрана конца игры

# Создание змейки и еды
snake = Snake()
food = generate_food()
score = 0
# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")

    # Движение змейки
    snake.move()

    # Проверка столкновения со стенами и собой
    head_x, head_y = snake.body[0]
    if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            snake.body[0] in snake.body[1:] # Вот тут происходит ошибка
    ):
        running = False

    # Проверка столкновения с едой
    if snake.body[0] == food:
        snake.grow()  # Увеличиваем змейку
        food = generate_food() # Генерируем новую еду
        score += 1 #Увеличиваем общий счет
    # Отрисовка
    screen.fill(BLACK)
    snake.draw(screen)
    show_score(score)
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(FPS)

pygame.quit()

sys.exit()