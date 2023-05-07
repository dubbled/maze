import pygame 

# maze game
game_map = [
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2],
]

SIZE = 500 
SCALE = 50
global cursor_position
cursor_position = (0, 0)

def update_cursor(dX = 0, dY = 0):
    global cursor_position
    x, y = cursor_position

    if dX < 0 and x == 0 or dX > 0 and x == len(game_map[0]) - 1:
        return
    
    if dY < 0 and y == 0 or dY > 0 and y == len(game_map) - 1:
        return
    
    new_cursor_position = (x + dX, y + dY)
    newX, newY = new_cursor_position

    at_location = game_map[newY][newX]
    if at_location == 2:
        pygame.quit()
    elif game_map[newY][newX]:
        print('warn wall')
        return

    global cursor, screen
    screen.blit(blank, (x * SCALE, y * SCALE))

    cursor_position = new_cursor_position
    print(f'updated cursor {cursor_position} {dX} {dY}')


    x, y = cursor_position
    screen.blit(cursor, (x * SCALE, y * SCALE))

    if game_map[y][x] == 2:
        pygame.quit()



def move(direction):
    if direction == 'n':
        update_cursor(0, -1) 
    if direction == 's':
        update_cursor(0, 1)
    if direction == 'e':
        update_cursor(1, 0)
    if direction == 'w':
        update_cursor(-1, 0)

# main
pygame.init()

tile_dimensions = ((SIZE, SIZE))
scale_dimensions = ((SCALE, SCALE))
screen = pygame.display.set_mode(tile_dimensions)
running = True

screen.fill('purple')

not_blank = pygame.Surface(scale_dimensions)
not_blank.fill((0,0,0)) # black 
blank = pygame.Surface(scale_dimensions)
blank.fill((255, 255, 255)) # white

# build map 
for row in range(len(game_map)):
    for col in range(len(game_map[row])):
        valid = game_map[row][col] == 1
        position = (col * SCALE, row * SCALE)

        if valid:
            screen.blit(not_blank, position)
        else:
            screen.blit(blank, position)

# build cursor
cursor = pygame.Surface(scale_dimensions)
cursor.fill((0, 255, 150))

screen.blit(cursor, cursor_position)

goal = pygame.Surface(scale_dimensions)
goal.fill((150, 0, 255))

screen.blit(goal, (((len(game_map[0])-1) * SCALE, (len(game_map)-1) * SCALE)))

# display
pygame.display.flip()

clock = pygame.time.Clock()

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_UP]:
        move('n')
    elif keys[pygame.K_DOWN]:
        move('s')
    elif keys[pygame.K_LEFT]:
        move('w')
    elif keys[pygame.K_RIGHT]:
        move('e')

    clock.tick(20)
    pygame.display.flip()

pygame.quit()
