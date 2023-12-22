import pygame
import random

game_started = False
pygame.init()
screen = pygame.display.set_mode((500,500))
font = pygame.font.SysFont("Serif",25)
with open("words.txt","r") as f:
    words = f.readlines()
edited_words = []
for word in words:
    edited_words.append(word[0:-1])
answer = (random.choice(edited_words))
answer_length = len(answer)
current_answer = ""
for i in range(answer_length):
    current_answer+="_ "
current_answer_image = font.render(current_answer,False,"black")
score = 0
disable_input =False
just_pressed = False
game_over = False
def draw_hangman(score):
    #print(score)
    if score > 0:
        pygame.draw.circle(screen, (50, 0, 0), (150, 140), 40, 3)
    if score > 1:
        pygame.draw.line(screen, pygame.Color("black"), (100, 200), (200, 200), 5)
    if score > 2:
        pygame.draw.line(screen, pygame.Color("black"), (150, 180), (150, 220), 5)
    if score > 3:
        pygame.draw.line(screen, pygame.Color("black"), (150, 220), (80, 300), 5)
    if score > 4:
        pygame.draw.line(screen, pygame.Color("black"), (150, 220), (220, 300), 5)
def draw_noose():
    pygame.draw.line(screen, pygame.Color("black"), (50, 50), (50, 300), 5)
    pygame.draw.line(screen, pygame.Color("black"), (50, 50), (150, 50), 5)
    pygame.draw.line(screen, pygame.Color("black"), (150, 50), (150, 100), 5)
    pygame.draw.line(screen, pygame.Color("black"), (0, 300), (300, 300), 5)
    #print(draw_hangman)

def check_letter(answer,current_answer,score, keys):
    #keys=pygame.key.get_pressed()
    if keys==pygame.K_a:
        if "a" in answer and "a" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("a")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "a"
                current_answer = "".join(current_answer)
        elif "a" in answer and "a" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_b:
        if "b" in answer and "b" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("b")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "b"
                current_answer = "".join(current_answer)
        elif "b" in answer and "b" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_c:
        if "c" in answer and "c" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("c")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "c"
                current_answer = "".join(current_answer)
        elif "c" in answer and "c" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_d:
        if "d" in answer and "d" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("d")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "d"
                current_answer = "".join(current_answer)
        elif "d" in answer and "d" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_e:
        if "e" in answer and "e" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("e")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "e"
                current_answer = "".join(current_answer)
        elif "e" in answer and "e" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_f:
        if "f" in answer and "f" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("f")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "f"
                current_answer = "".join(current_answer)
        elif "f" in answer and "f" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_g:
        if "g" in answer and "g" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("g")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "g"
                current_answer = "".join(current_answer)
        elif "g" in answer and "g"in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_h:
        if "h" in answer and "h" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("h")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "h"
                current_answer = "".join(current_answer)
        elif "h" in answer and "h" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_i:
        if "i" in answer and "i" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("i")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "i"
                current_answer = "".join(current_answer)
        elif "i" in answer and "i" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_j:
        if "j" in answer and "j" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("j")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "j"
                current_answer = "".join(current_answer)
        elif "j" in answer and "j" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_k:
        if "k" in answer and "k" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("k")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "k"
                current_answer = "".join(current_answer)
        elif "k" in answer and "k" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_l:
        if "l" in answer and "l" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("l")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "l"
                current_answer = "".join(current_answer)
        elif "l" in answer and "l" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_m:
        if "m" in answer and "m" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("m")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "m"
                current_answer = "".join(current_answer)
        elif "m" in answer and "m" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_n:
        if "n" in answer and "n" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("n")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "n"
                current_answer = "".join(current_answer)
        elif "n" in answer and "n" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_o:
        if "o" in answer and "o" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("o")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "o"
                current_answer = "".join(current_answer)
        elif "o" in answer and "o" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_p:
        if "p" in answer and "p" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("p")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "p"
                current_answer = "".join(current_answer)
        elif "p" in answer and "p" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_q:
        if "q" in answer and "q" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("q")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "q"
                current_answer = "".join(current_answer)
        elif "q" in answer and "q" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_r:
        if "r" in answer and "r" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("r")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "r"
                current_answer = "".join(current_answer)
        elif "r" in answer and "r" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_s:
        if "s" in answer and "s" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("s")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "s"
                current_answer = "".join(current_answer)
        elif "s" in answer and "s" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_t:
        if "t" in answer and "t" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("t")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "t"
                current_answer = "".join(current_answer)
        elif "t" in answer and "t" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_u:
        if "u" in answer and "u" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("u")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "u"
                current_answer = "".join(current_answer)
        elif "u" in answer and "u" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_v:
        if "v" in answer and "v" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("v")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "v"
                current_answer = "".join(current_answer)
        elif "v" in answer and "v" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_w:
        if "w" in answer and "w" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("w")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "w"
                current_answer = "".join(current_answer)
        elif "w" in answer and "w" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_x:
        if "x" in answer and "x" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("x")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "x"
                current_answer = "".join(current_answer)
        elif "x" in answer and "x" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_y:
        if "y" in answer and "y" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("y")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "y"
                current_answer = "".join(current_answer)
        elif "y" in answer and "y" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_z:
        if "z" in answer and "z" not in current_answer:
            if find_duplicates(answer):
                #this won't work if there is more than one "a" in the string
                a_location = answer.find("z")
                current_answer = list(current_answer)
                current_answer[a_location*2] = "z"
                current_answer = "".join(current_answer)
        elif "z" in answer and "z" in current_answer:
            pass
        else:
            score += 1
    return current_answer,score

def find_duplicates(string):
    duplicates ={}
    for char in string:
        if char in duplicates:
            duplicates[char]+=1
        # never seen the character before
        else:
            duplicates[char]=1
    # remove all characters that don't have duplicates
    for key in duplicates:
        if duplicates[key] < 2:
            del duplicates[key]
    return duplicates
print(find_duplicates("b"))

while True:
    if game_over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    else:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                just_pressed = True
                print(just_pressed)
            if event.type==pygame.KEYUP:
                if just_pressed == True:
                    current_answer, score = check_letter(answer, current_answer, score, event.key)
                    just_pressed = False
                    print(just_pressed)

    screen.fill("blue")
    #screen.blit(answer, (190, 270))
    #print(answer)
    screen.blit(current_answer_image,(200,400))
    draw_hangman(score)
    draw_noose()
    current_answer_image = font.render(current_answer,False,"black")
    font.render(current_answer, False, "black")
    if current_answer.replace(" ",'')==answer:
        win_condition = font.render("You win", False, "black")
        screen.blit(win_condition, (300, 350))
        game_over = True
    if score > 4:
        lose_condition = font.render("You lose", False, "black")
        screen.blit(lose_condition, (300,300))
        game_over = True
    #print(current_answer)
    """
    #if game_started == False:
        #pygame.draw.rect(screen, "black", x_rectangle, 3)
        pygame.draw.rect(screen, "black", o_rectangle, 3)
        pygame.draw.circle(screen, (0, 0, 255), (400, 400), 60, 3)
        drawX(100, 400)
    """









    pygame.display.update()
