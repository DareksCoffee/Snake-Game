import pygame
import random

def startgame(screen, height, width, clock):
    ## GLOBAL GAME VARIABLES ##

    running = True  

    ## Grid variables ##
    grid_size = 20     #
    show_grid = False  # Flag to control the visibility of the grid
    ####################

    ## Fruit variables ##
    fruit_width = 25    #
    fruit_height = 25   #
    #####################

    ## Snake variables ##
    snake_size = 1
    snake_width = 35
    snake_height = 35
    snake_x = width // 2 - snake_width // 2
    snake_y = height // 2 - snake_height // 2
    speed_x = grid_size
    speed_y = 0
    snake_segments = [(snake_x, snake_y)]
    ######################

    ## Score variable ##
    score = 0          #
    ####################

    def generate_fruit():
        """
        function generate_fruit()

        Parameters:
        None

        returns 
        fruit_x, fruit_y
        """
        grid_cells_x = width // grid_size
        grid_cells_y = height // grid_size

        ## Generate random positions for the fruit within the grid ##
        fruit_x = random.randint(0, grid_cells_x - 1) * grid_size   #
        fruit_y = random.randint(0, grid_cells_y - 1) * grid_size   #
        #############################################################

        return fruit_x, fruit_y # Returns the variable fruit_x and fruit_y

    def reset_game():
        nonlocal snake_x, snake_y, speed_x, speed_y, snake_segments, snake_size, score
        snake_x = width // 2 - snake_width // 2
        snake_y = height // 2 - snake_height // 2
        speed_x = grid_size
        speed_y = 0
        snake_segments = [(snake_x, snake_y)]
        snake_size = 1
        score = 0

    ## Initialize the initial position of the fruit ##
    fruit_x, fruit_y = generate_fruit()              #
    ##################################################
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # Set running to False to exit the while loop

            ## Check for key press events ##
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    show_grid = not show_grid
            #################################

        ## Handle key events for controlling snake movement ##
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and speed_x == 0:
            speed_x = -grid_size
            speed_y = 0
        elif keys[pygame.K_RIGHT] and speed_x == 0:
            speed_x = grid_size
            speed_y = 0
        elif keys[pygame.K_UP] and speed_y == 0:
            speed_x = 0
            speed_y = -grid_size
        elif keys[pygame.K_DOWN] and speed_y == 0:
            speed_x = 0
            speed_y = grid_size
        ######################################################

        ## Update snake position ##
        snake_x += speed_x
        snake_y += speed_y
        ###########################

        ## Wrap snake's position to the opposite wall if it goes out of the screen ##
        snake_x = snake_x % width
        snake_y = snake_y % height
        #############################################################################

        ## Check if snake collided with itself ##
        if (snake_x, snake_y) in snake_segments[1:]:
            reset_game()
        #########################################

        ## Check if snake has reached the fruit ##
        if (
            snake_x < fruit_x + fruit_width
            and snake_x + snake_width > fruit_x
            and snake_y < fruit_y + fruit_height
            and snake_y + snake_height > fruit_y
        ):
            ## Generate a new position for the fruit ##
            fruit_x, fruit_y = generate_fruit()       #
            ###########################################

            ## Increase the size of the snake ##
            snake_size += 1                    #
            ####################################

            ## Increase the score ##
            score += 1             #
            ########################

        ## Add the current head position to the list of snake segments ##
        snake_segments.append((snake_x, snake_y))

        ## Trim the snake_segments list if it exceeds the size ##
        if len(snake_segments) > snake_size:
            snake_segments.pop(0)

        ## Clear the screen ##
        screen.fill((7, 7, 7)) # NOTE: The argument for fill() is an RGB tuple, where each value represents the intensity of red, green, and blue (from 0 to 255).

        ## Draw the grid if enabled ##
        if show_grid:
            for x in range(0, width, grid_size):
                pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, height))
            for y in range(0, height, grid_size):
                pygame.draw.line(screen, (50, 50, 50), (0, y), (width, y))
        ###############################

        ## Draw the fruit ##
        pygame.draw.rect(screen, (255, 0, 0), [fruit_x, fruit_y, fruit_width, fruit_height])

        ## Draw the snake segments ##
        for segment in snake_segments:
            pygame.draw.rect(screen, (255, 255, 255), [segment[0], segment[1], snake_width, snake_height])
        #############################

        ## Draw the score ##
        font = pygame.font.Font(None, 36)
        text = font.render("Score: {}".format(score), True, (255, 255, 255))
        screen.blit(text, (10, 10))
        ####################

        ## Update the display ##
        pygame.display.flip()
        ####################

        ## Set the frames per second (FPS) ##
        clock.tick(10)                      #
        #####################################

    pygame.quit() # Close the window when the while loop has ended #






###########################################################
#  Hello there!                                           #
#  Thank you for exploring this little game project. I    #
#  hope you found it both enjoyable and educational.      #
#  I've strived to keep the code clear and accessible for #
#  everyone. If you've gained insights or had fun, please #
#  consider leaving a star in the repository. Your support#
#  means a lot!                                           #
#                                                         #
#  Enjoy!                                                 #
#                                                         #
#  - TMA.                                                 #
#                                                         #
###########################################################