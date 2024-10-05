import pygame
import os
pygame.font.init()

#SCREEN SIZE AND NAME
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACEWAR")

# BASIC INTIALIZES
colour = (0, 102, 0)
fps = 60
vel = 10
bullet_vel = 7
bullets_max = 3

# BULLET HITTING EVENT
red_hit = pygame.USEREVENT + 1
blue_hit = pygame.USEREVENT + 2

#BORDERS OF THE GAME
bord1 = pygame.Rect(0, 0, WIDTH, 7)
bord2 = pygame.Rect(0, HEIGHT-7, WIDTH, 7)
border = pygame.Rect(WIDTH//2 - 2, 0, 4, HEIGHT)

#HEALTH TEXT
health_font = pygame.font.SysFont('helvetica', 30)
winner_font = pygame.font.SysFont('helvetica', 70)

#SPACESHIP(RED) IMPORT
red_spaceship = pygame.image.load(os.path.join('Assets', '1.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (80, 80)), 270)

#SPACESHIP(BLUE) IMPORT
blue_spaceship = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', '2.png')), 90)
blue_spaceship = pygame.transform.scale(blue_spaceship, (80, 80))

# BACKGROUND
bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets', '5.png')), (900, 900))


# ALL OF THE DRAWING PART
def draw(red, blue, red_bullets, blue_bullets, red_health, blue_health):
    WIN.blit(bg, (0,0))
    pygame.draw.rect(WIN, (255, 255, 255), bord1)
    pygame.draw.rect(WIN, (255, 255, 255), bord2)
    pygame.draw.rect(WIN, (0, 0, 0), border)

    red_health_text = health_font.render("Health: " + str(red_health), 1, (173, 216, 230))
    blue_health_text = health_font.render("Health: " + str(blue_health), 1, (173, 216, 230))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(blue_health_text, (10, 10))

    WIN.blit(red_spaceship, (red.x, red.y))
    WIN.blit(blue_spaceship, (blue.x, blue.y))
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)
    for bullet in blue_bullets:
        pygame.draw.rect(WIN, (173, 216, 230), bullet)
    
    pygame.display.update()

# RED SHIP MOVEMENT
def red_spaceship_move(keys_pressed, red):
    if keys_pressed[pygame.K_w] and red.y - vel > 0:
            red.y = red.y - vel #up
    if keys_pressed[pygame.K_s] and red.y + vel + red.height < HEIGHT:
            red.y = red.y + vel #down
    if keys_pressed[pygame.K_a] and red.x - vel > 0:
            red.x = red.x - vel #left
    if keys_pressed[pygame.K_d] and red.x + vel + red.width < border.x:
            red.x = red.x + vel #right


# BLUE HSIP MOVEMENT
def blue_spaceship_move(keys_pressed, blue):
    if keys_pressed[pygame.K_UP] and blue.y - vel > 0:
            blue.y = blue.y - vel #up
    if keys_pressed[pygame.K_DOWN] and blue.y + vel + blue.height < HEIGHT:
            blue.y = blue.y + vel #down
    if keys_pressed[pygame.K_LEFT] and blue.x - vel > border.x + border.width:
            blue.x = blue.x - vel #left
    if keys_pressed[pygame.K_RIGHT] and blue.x + vel + blue.width < WIDTH:
            blue.x = blue.x + vel #right
    
# BULLETS CONCEPTS
def handle_bullets(red_bullets, blue_bullets, red, blue):
    for bullet in red_bullets:
        bullet.x += bullet_vel
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(blue_hit))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)
        

    for bullet in blue_bullets:
        bullet.x -= bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            blue_bullets.remove(bullet)
        elif bullet.x < 0:
            blue_bullets.remove(bullet)

#WINNER TEXT SHOW
def draw_winner(text):
    d_text = winner_font.render(text, 1, (255, 255, 255))
    WIN.blit(d_text, (WIDTH//2 - d_text.get_width()/2, HEIGHT/2 - d_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(4000)

#MAIN METHOD
def main():
    red = pygame.Rect(100, 100, 80, 80)
    blue = pygame.Rect(700, 100, 80, 80)
    
    red_bullets = []
    blue_bullets = []

    red_health = 10
    blue_health = 10


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < bullets_max:
                    bullet = pygame.Rect(red.x + red.width, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(blue_bullets) < bullets_max:
                    bullet = pygame.Rect(blue.x , blue.y + blue.height//2 - 2, 10, 5)
                    blue_bullets.append(bullet)

            if event.type == red_hit:
                blue_health -= 1
            
            if event.type == blue_hit:
                red_health -= 1
        
        winner_text = ""
        if red_health <= 0:
            winner_text = "RED WINS!"
        
        if blue_health <= 0:
            winner_text = "BLUE WINS!"
        
        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        red_spaceship_move(keys_pressed, red)
        blue_spaceship_move(keys_pressed, blue)

        handle_bullets(red_bullets, blue_bullets, red, blue)

        draw(red, blue, red_bullets, blue_bullets, red_health, blue_health)

    main()

if __name__ == "__main__":
    main()