import sys
import pygame
from pygame.locals import *
from draw import *
from utils import *
from levels import levels as level_select
from gamelogic import *
from levels import *
from algorithms import *
import tracemalloc

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 800
screen = pygame.display.set_mode((width, height))

screen_width, screen_height = screen.get_size()

class GameState:
    MAIN_MENU = "main_menu"
    OPTIONS_MENU = "options_menu"
    CREDITS_SCREEN = "credits_screen"
    PLAYING = "Interface"



# Variáveis para o menu principal
button_start_width = 400
button_start_height = 100
x_button_start = (screen_width - button_start_width) // 2
y_button_start = ((screen_height - button_start_height) // 2) - 50

button_options_width = 400
button_options_height = 100
x_button_options = (screen_width - button_options_width) // 2
y_button_options = ((screen_height - button_options_height) // 2) + 75

button_quit_width = 400
button_quit_height = 100
x_button_quit = (screen_width - button_quit_width) // 2
y_button_quit = ((screen_height - button_quit_height) // 2) + 200

button_start = Button(x_button_start, y_button_start, button_start_width, button_start_height, "Start - AI", (125, 0, 150), (255, 255, 255), 60)
# button_options = Button(x_button_options, y_button_options, button_options_width, button_options_height, "Options", (0, 80, 255), (255, 255, 255), 60)
button_quit = Button(x_button_quit, y_button_quit, button_quit_width, button_quit_height, "Quit", (255, 40, 100), (255, 255, 255), 60)

# Variáveis para o menu de opções
button_controls_width = 400
button_controls_height = 100
x_button_controls = (screen_width - button_controls_width) // 2
y_button_controls = ((screen_height - button_controls_height) // 2) - 50

button_credits_width = 400
button_credits_height = 100
x_button_credits = (screen_width - button_credits_width) // 2
y_button_credits = ((screen_height - button_credits_height) // 2) + 75

button_return_width = 400
button_return_height = 100
x_button_return = (screen_width - button_return_width) // 2
y_button_return = ((screen_height - button_return_height) // 2) + 200

#button_controls = Button(x_button_controls, y_button_controls, button_controls_width, button_controls_height, "Controls", (0, 80, 255), (0, 0, 0), 60)
#button_credits = Button(x_button_credits, y_button_credits, button_credits_width, button_credits_height, "Credits", (0, 80, 255), (255, 255, 255), 60)
#button_return = Button(x_button_return, y_button_return, button_return_width, button_return_height, "Return", (0, 80, 255), (255, 255, 255), 60)






def main_menu_loop(screen):
    draw_main_menu(screen)
    #checkbox = CheckBox(50,screen_height-200,100,100,(255,255,255),(0,255,0),(255,0,0),10)
    #checkbox.draw(screen)
    current_state = GameState.MAIN_MENU
    #Reaproveitado do botao opcoes
    button_start.draw(screen)
    button_play_human = Button((screen_width - button_options_width) // 2, y_button_options, 400, 100, "Start - Human", (0, 80, 255), (255, 255, 255), 60)
    button_play_human.draw(screen)
    button_quit.draw(screen)
    while True:
    # Draw Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_start.is_clicked(pygame.mouse.get_pos()):
                    current_state = GameState.PLAYING
                #elif checkbox.is_clicked(screen,pygame.mouse.get_pos()):
                    #print("yes")
                    """if current_state == GameState.PLAYING:
                        # Lógica do jogo
                        # Você pode usar level_1["initial_state"] e level_1["objective_state"] para configurar o estado inicial e objetivo do nível

                        # Exemplo:
                        current_level: Dict[str, List[List[str]]] = beginner_1  # Escolha o nível atual
                        initial_state = current_level["initial_state"]
                        objective_state = current_level["objective_state"]
                        game = Game(initial_state, objective_state)
                        game.run(screen, screen_width, screen_height)"""

                #elif button_options.is_clicked(pygame.mouse.get_pos()):
                #    current_state = GameState.OPTIONS_MENU
                    # Adicione outros elementos do menu de opções conforme necessário
                    # Exemplo: Botões para ajustar configurações
                    
                elif button_play_human.is_clicked(pygame.mouse.get_pos()):
                    level_menu_human_loop(screen)
                elif button_quit.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        if current_state == GameState.OPTIONS_MENU:
            options_menu(screen)

        elif current_state == GameState.CREDITS_SCREEN:
            draw_credits_screen(screen, screen_width)
            
        elif current_state == GameState.PLAYING:
            level_menu_loop(screen)

        """elif current_state == GameState.MAIN_MENU:
            draw_main_menu(screen)
            button_start.draw(screen)
            button_play_human.draw(screen)
            button_quit.draw(screen)"""
            # Voltar para o menu principal ao clicar na tela de créditos

        pygame.display.flip()
        fpsClock.tick(fps)

def level_human_loop(screen,level):
    draw_menu_settings(screen)
    write_on_text(screen,"Tip:",(255,255,255),100,200,100)
    checkbox = CheckBox(200,150,100,100,(255,255,255),(128,128,128),(0,0,0),10)
    checkbox.draw(screen)
    #button_continue = Button()

def level_menu_human_loop(screen):
    draw_level_select_menu(screen)
    min_y = 30 + 140
    min_x = 30 + ((screen_width-30-300)/4)
    x_increment = ((screen_width-30-300)/4)
    y_increment = (screen_height - min_y - 30-300)/4 
    x = min_x
    levels = [0]*9
    for i in range(0,3):
        if i == 0:
            write_on_text(screen,"Easy",(255,255,255),x+50,min_y-20,50)
        elif i == 1:
            write_on_text(screen,"Medium",(255,255,255),x+50,min_y-20,50)
        elif i == 2:
            write_on_text(screen,"Hard",(255,255,255),x+50,min_y-20,50)
        y = min_y
        for j in range(1,4):
            levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
            levels[j+(i*3)-1].draw(screen)
            y+=y_increment+100
        x += x_increment+100
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if levels[0].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Beginner"][0]["initial_state"],level_select["Beginner"][0]["objective_state"]))
                elif levels[1].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Beginner"][1]["initial_state"],level_select["Beginner"][1]["objective_state"]))
                elif levels[2].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Beginner"][2]["initial_state"],level_select["Beginner"][2]["objective_state"]))
                elif levels[3].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Amateur"][0]["initial_state"],level_select["Amateur"][0]["objective_state"]))
                elif levels[4].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Amateur"][1]["initial_state"],level_select["Amateur"][1]["objective_state"]))
                elif levels[5].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Amateur"][2]["initial_state"],level_select["Amateur"][2]["objective_state"]))
                elif levels[6].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Expert"][0]["initial_state"],level_select["Expert"][0]["objective_state"]))
                elif levels[7].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Expert"][1]["initial_state"],level_select["Expert"][1]["objective_state"]))
                elif levels[8].is_clicked(pygame.mouse.get_pos()):
                    level_human_loop(screen,Cogito(level_select["Expert"][2]["initial_state"],level_select["Expert"][2]["objective_state"]))
            """elif event.type == VIDEORESIZE or event.type == VIDEOEXPOSE:

                ## TODO: NAO FUNCIONA, perguntar ao prof se deve suportar isto
                draw_level_select_menu(screen)
                print("hellyeah")
                screen_width_new, screen_height_new = screen.get_size()
                min_y = 30 + 140
                min_x = 30 + ((screen_width_new-30-300)/4)
                x_increment = ((screen_width_new-30-300)/4)
                y_increment = (screen_height_new - min_y - 30-300)/4 
                x = min_x
                for i in range(0,3):
                    y = min_y
                    for j in range(1,4):
                        levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
                        levels[j+(i*3)-1].draw(screen)
                        y+=y_increment+100
                    x += x_increment+100"""
        pygame.display.flip()
        fpsClock.tick(fps)

def options_menu(screen):
    draw_options_menu(screen)
    current_state = GameState.OPTIONS_MENU

    while True:
    # Draw Main Menu
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                    current_state = GameState.CREDITS_SCREEN
            if current_state == GameState.CREDITS_SCREEN:
                draw_credits_screen(screen, screen_width)
def level_menu_loop(screen):
    draw_level_select_menu(screen)
    min_y = 30 + 140
    min_x = 30 + ((screen_width-30-300)/4)
    x_increment = ((screen_width-30-300)/4)
    y_increment = (screen_height - min_y - 30-300)/4 
    x = min_x
    levels = [0]*9
    for i in range(0,3):
        if i == 0:
            write_on_text(screen,"Easy",(255,255,255),x+50,min_y-20,50)
        elif i == 1:
            write_on_text(screen,"Medium",(255,255,255),x+50,min_y-20,50)
        elif i == 2:
            write_on_text(screen,"Hard",(255,255,255),x+50,min_y-20,50)
        y = min_y
        for j in range(1,4):
            levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
            levels[j+(i*3)-1].draw(screen)
            y+=y_increment+100
        x += x_increment+100
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if levels[0].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Beginner"][0]["initial_state"],level_select["Beginner"][0]["objective_state"]))
                elif levels[1].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Beginner"][1]["initial_state"],level_select["Beginner"][1]["objective_state"]))
                elif levels[2].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Beginner"][2]["initial_state"],level_select["Beginner"][2]["objective_state"]))
                elif levels[3].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Amateur"][0]["initial_state"],level_select["Amateur"][0]["objective_state"]))
                elif levels[4].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Amateur"][1]["initial_state"],level_select["Amateur"][1]["objective_state"]))
                elif levels[5].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Amateur"][2]["initial_state"],level_select["Amateur"][2]["objective_state"]))
                elif levels[6].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Expert"][0]["initial_state"],level_select["Expert"][0]["objective_state"]))
                elif levels[7].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Expert"][1]["initial_state"],level_select["Expert"][1]["objective_state"]))
                elif levels[8].is_clicked(pygame.mouse.get_pos()):
                    level_loop(screen,Cogito(level_select["Expert"][2]["initial_state"],level_select["Expert"][2]["objective_state"]))
            """elif event.type == VIDEORESIZE or event.type == VIDEOEXPOSE:

                ## TODO: NAO FUNCIONA, perguntar ao prof se deve suportar isto
                draw_level_select_menu(screen)
                print("hellyeah")
                screen_width_new, screen_height_new = screen.get_size()
                min_y = 30 + 140
                min_x = 30 + ((screen_width_new-30-300)/4)
                x_increment = ((screen_width_new-30-300)/4)
                y_increment = (screen_height_new - min_y - 30-300)/4 
                x = min_x
                for i in range(0,3):
                    y = min_y
                    for j in range(1,4):
                        levels[j+(i*3)-1] = Button(x, y, 100, 100, str(j+(i*3)), (0,0,0), (255, 255, 255), 80)
                        levels[j+(i*3)-1].draw(screen)
                        y+=y_increment+100
                    x += x_increment+100"""
        pygame.display.flip()
        fpsClock.tick(fps)

def level_loop(screen,level):
    draw_level_menu(screen)
    button_bfs = Button(50, 200, 110, 100, "BFS", (125, 125, 125), (255, 255, 255), 80)
    button_bfs.draw(screen)
    button_ids = Button(50, 420, 400, 70, "Iterative Deepening Search", (125, 125, 125), (255, 255, 255), 40)
    button_ids.draw(screen)
    button_greedy = Button(50, 500, 320, 100, "Greedy Search", (125, 125, 125), (255, 255, 255), 60)
    button_greedy.draw(screen)
    button_a_star = Button(50, 610, 320, 100, "A* Search", (125, 125, 125), (255, 255, 255), 80)
    button_a_star.draw(screen)
    draw_board_initial(screen,level.board,200,200,800,100)
    draw_arrow(screen, (900, 350), (900, 450))
    draw_board_initial(screen, level.final_board, 200,200,800,500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_bfs.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,"BFS",level)
                elif button_ids.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,"IDS",level)
                elif button_greedy.is_clicked(pygame.mouse.get_pos()):
                    heuristic_choice_loop(screen,"GreedySearch",level)
                elif button_a_star.is_clicked(pygame.mouse.get_pos()):
                    heuristic_choice_loop(screen,"A_Star_Search",level)
        pygame.display.flip()
        fpsClock.tick(fps)
                
def calculating_loop(screen,algorithm,level,heuristic=""):
    draw_calculating_screen(screen)
    tracemalloc.start()
    start = time.time()
    if algorithm=="BFS":
        start_snapshot = tracemalloc.take_snapshot()
        goale = breadth_first_search(level,check_win,get_moves)
        goal = goale.state.move_history
        end_snapshot = tracemalloc.take_snapshot()
    elif algorithm=="IDS":
        start_snapshot = tracemalloc.take_snapshot()
        goale = iterative_deepening_search(level,check_win,get_moves)
        goal = goale.state.move_history
        end_snapshot = tracemalloc.take_snapshot()
    elif algorithm=="GreedySearch":
        if heuristic=="h1":
            start_snapshot = tracemalloc.take_snapshot()
            goal = greedy_search(level,h1)
            end_snapshot = tracemalloc.take_snapshot()
        elif heuristic=="h2":
            start_snapshot = tracemalloc.take_snapshot()
            goal = greedy_search(level,h2)
            end_snapshot = tracemalloc.take_snapshot()
    elif algorithm=="A_Star_Search":
        if heuristic=="h1":
            start_snapshot = tracemalloc.take_snapshot()
            goal = a_star_search(level,h1)
            end_snapshot = tracemalloc.take_snapshot()
        elif heuristic=="h2":
            start_snapshot = tracemalloc.take_snapshot()
            goal = a_star_search(level,h2)
            end_snapshot = tracemalloc.take_snapshot()
    end = time.time()
    time_total = end-start
    # Calculate the memory difference
    memory_diff = end_snapshot.compare_to(start_snapshot, 'filename')
    total_memory_usage = sum(stat.size for stat in memory_diff)
    total_memory_usage_kb = total_memory_usage/1024
    results_loop(screen,time_total,total_memory_usage_kb,goal)

def results_loop(screen,time_total,memory_total_kb,result):
    draw_results_menu(screen,time_total,memory_total_kb,result)
    button_main = Button((screen_width/3)-100, 500, 200, 100, "Main Menu", (255, 0, 0), (255, 255, 255), 50)
    button_main.draw(screen)
    button_step = Button(((screen_width/3)*2)-100, 500, 200, 100, "See Steps", (0, 255, 0), (255, 255, 255), 50)
    button_step.draw(screen)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_main.is_clicked(pygame.mouse.get_pos()):
                    main_menu_loop(screen)
                elif button_step.is_clicked(pygame.mouse.get_pos()):
                    steps_loop(screen,result)
        pygame.display.flip()
        fpsClock.tick(fps)

def steps_loop(screen,result):
    draw_steps_menu(screen)
    button_main = Button(0, screen_height-100, 200, 100, "Main Menu", (255, 0, 0), (255, 255, 255), 50)
    button_main.draw(screen)
    draw_board_initial(screen,result[0],400,400,(screen_width/2)-200,(screen_height/2)-150)
    write_on_text(screen,"Step number:",(255,255,255),screen_width/2-50,200,50)
    write_on_text(screen,"1",(255,255,255),screen_width/2+100,200,65)
    button_before = Button(screen_width/2 - 200, (screen_height/2)-150+420, 150, 80, "BEFORE", (0, 128, 128), (255, 255, 255), 50)
    button_before.draw(screen)
    button_next = Button(screen_width/2 + 50, (screen_height/2)-150+420, 150, 80, "NEXT", (54, 1, 63), (255, 255, 255), 50)
    button_next.draw(screen)
    pygame.display.flip()
    index = 0
    step_show = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:   
                if button_main.is_clicked(pygame.mouse.get_pos()):
                    main_menu_loop(screen)
                elif button_next.is_clicked(pygame.mouse.get_pos()) and index!=(len(result)-1):
                    draw_board_change(screen,result[index],result[index+1],400,400,(screen_width/2)-200,(screen_height/2)-150)
                    index += 1
                    step_show += 1
                    pygame.draw.rect(screen,(0,0,0),(screen_width/2+65,150,100,90))
                    write_on_text(screen,str(step_show),(255,255,255),screen_width/2+100,200,65)
                    pygame.display.flip()
                elif button_before.is_clicked(pygame.mouse.get_pos()) and index!=0:
                    draw_board_change(screen,result[index],result[index-1],400,400,(screen_width/2)-200,(screen_height/2)-150)
                    index -= 1
                    step_show -= 1
                    pygame.draw.rect(screen,(0,0,0),(screen_width/2+65,150,100,90))
                    write_on_text(screen,str(step_show),(255,255,255),screen_width/2+100,200,65)
                    pygame.display.flip()
                    #pygame.draw.rect(screen, (51, 153, 255), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)))
        pygame.display.flip()
        fpsClock.tick(fps)
    #raw_arrow(screen, (900, 350), (900, 450))
    #draw_board_initial(screen, level.final_board, 200,200,800,500)

def heuristic_choice_loop(screen,algorithm,level):
    button_incorrect, button_manhattan = draw_heuristic_choice_screen(screen)
    heuristic_chosen = None

    while heuristic_chosen is None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if button_incorrect.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,algorithm,level,"h1")
                elif button_manhattan.is_clicked(pygame.mouse.get_pos()):
                    calculating_loop(screen,algorithm,level,"h2")

        pygame.display.flip()
        fpsClock.tick(fps)




main_menu_loop(screen) 