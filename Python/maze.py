import readchar, os, random


POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
NUM_OF_MAP_OBJECTS = 11

obstacle_definition = """\
###########################
                            # 
#   ##########  #### #    ### 
#         ###        ###    # 
#   ##### ### ##     ###    # 
#       # ### #    #####    # 
#     # # ### #     ######### 
#  ##   # ### # #     # ##### 
#   #   # ### # ####     
    #   # ### # ####    ##### 
  # #   # ##             
#       #  ## #     # # ##### 
#   ### #  ## #         ##### 
#  ####   ### # # # #         
#  ##########################\
"""

my_position = [0, 1]
tail_length = 0
tail = []
map_objects = []

end_game = False
died = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]


# Main loop
while not end_game:

    os.system("cls")
    # Generate random objects on the map
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = ([random.randint(0, MAP_WIDTH - 1) , random.randint(0, MAP_HEIGHT -1)])

        if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            map_objects.append(new_position)

    # Draw Map

    print("+" + "-" * MAP_WIDTH * 2 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object
            
            for tail_place in tail:
                if tail_place[POS_X] == coordinate_x and tail_place[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_place

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"
                
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_length +=1

                if tail_in_cell:
                    died = True
                    end_game = True
            
            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 2 + "+")

    #print("La cola {}".format(tail))

    #print(my_position )
    # Ask user where he wants to move
    #direction = input("¿Donde te quieres mover? [WASD]: ")

    direction = readchar.readchar()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]
        
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]
        
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
        
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
        
    elif direction == "q":
        end_game = True
    
    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

    os.system("cls")

if died:
    print("Has muerto!")