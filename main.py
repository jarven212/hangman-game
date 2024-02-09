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
def find_duplicates(string):
    duplicates ={}
    new_duplicates = {}
    for char in string:
        if char in duplicates:
            duplicates[char]+=1
        # never seen the character before
        else:
            duplicates[char]=1
    # remove all characters that don't have duplicates
    for key in duplicates:
        print(duplicates[key])
        if duplicates[key] >= 2:
            new_duplicates[key] = duplicates[key]
    return new_duplicates
duplicates = find_duplicates(answer)
current_answer_image = font.render(current_answer,False,"black")
score = 0
disable_input =False
just_pressed = False
game_over = False
def draw_hangman(score):
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

def check_letter(answer,current_answer,score, keys):
    duplicates = find_duplicates(answer)
    if keys==pygame.K_a:
        if "a" in answer and "a" not in current_answer:
            # check if there were any duplicates found, if there were none, just find the location once
            if "a" in duplicates.keys():
                a = duplicates["a"]
                old_index=0
                temp=answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("a")
                        current_answer[a_location * 2] = "a"
                        old_index=a_location
                        temp=temp[a_location+1:]
                    else:
                        a_location = temp.find("a")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "a"
                        temp = temp[a_location+1:]
                current_answer = "".join(current_answer)

            else:
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
            if "b" in duplicates.keys():
                a = duplicates["b"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("b")
                        current_answer[a_location * 2] = "b"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("b")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "b"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                b_location = answer.find("b")
                current_answer = list(current_answer)
                current_answer[b_location*2] = "b"
                current_answer = "".join(current_answer)
        elif "b" in answer and "b" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_c:
        if "c" in answer and "c" not in current_answer:
            if "c" in duplicates.keys():
                a = duplicates["c"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("c")
                        current_answer[a_location * 2] = "c"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("c")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "c"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                c_location = answer.find("c")
                current_answer = list(current_answer)
                current_answer[c_location*2] = "c"
                current_answer = "".join(current_answer)
        elif "c" in answer and "c" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_d:
        if "d" in answer and "d" not in current_answer:
            if "d" in duplicates.keys():
                a = duplicates["d"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("d")
                        current_answer[a_location * 2] = "d"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("d")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "d"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                d_location = answer.find("d")
                current_answer = list(current_answer)
                current_answer[d_location*2] = "d"
                current_answer = "".join(current_answer)
        elif "d" in answer and "d" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_e:
        if "e" in answer and "e" not in current_answer:
            if "e" in duplicates.keys():
                a = duplicates["e"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("e")
                        current_answer[a_location * 2] = "e"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("e")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "e"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                e_location = answer.find("e")
                current_answer = list(current_answer)
                current_answer[e_location*2] = "e"
                current_answer = "".join(current_answer)
        elif "e" in answer and "e" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_f:
        if "f" in answer and "f" not in current_answer:
            if "f" in duplicates.keys():
                a = duplicates["f"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("f")
                        current_answer[a_location * 2] = "f"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("f")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "f"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                f_location = answer.find("f")
                current_answer = list(current_answer)
                current_answer[f_location*2] = "f"
                current_answer = "".join(current_answer)
        elif "f" in answer and "f" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_g:
        if "g" in answer and "g" not in current_answer:
            if "g" in duplicates.keys():
                a = duplicates["g"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("g")
                        current_answer[a_location * 2] = "g"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("g")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "g"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                g_location = answer.find("g")
                current_answer = list(current_answer)
                current_answer[g_location*2] = "g"
                current_answer = "".join(current_answer)
        elif "g" in answer and "g"in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_h:
        if "h" in answer and "h" not in current_answer:
            if "h" in duplicates.keys():
                a = duplicates["h"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("h")
                        current_answer[a_location * 2] = "h"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("h")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "h"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                h_location = answer.find("h")
                current_answer = list(current_answer)
                current_answer[h_location*2] = "h"
                current_answer = "".join(current_answer)
        elif "h" in answer and "h" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_i:
        if "i" in answer and "i" not in current_answer:
            if "i" in duplicates.keys():
                a = duplicates["i"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("i")
                        current_answer[a_location * 2] = "i"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("i")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "i"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                i_location = answer.find("i")
                current_answer = list(current_answer)
                current_answer[i_location*2] = "i"
                current_answer = "".join(current_answer)
        elif "i" in answer and "i" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_j:
        if "j" in answer and "j" not in current_answer:
            if "j" in duplicates.keys():
                a = duplicates["j"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("j")
                        current_answer[a_location * 2] = "j"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("j")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "j"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                j_location = answer.find("j")
                current_answer = list(current_answer)
                current_answer[j_location*2] = "j"
                current_answer = "".join(current_answer)
        elif "j" in answer and "j" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_k:
        if "k" in answer and "k" not in current_answer:
            if "k" in duplicates.keys():
                a = duplicates["k"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("k")
                        current_answer[a_location * 2] = "k"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("k")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "k"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                k_location = answer.find("k")
                current_answer = list(current_answer)
                current_answer[k_location*2] = "k"
                current_answer = "".join(current_answer)
        elif "k" in answer and "k" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_l:
        if "l" in answer and "l" not in current_answer:
            if "l" in duplicates.keys():
                a = duplicates["l"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("l")
                        current_answer[a_location * 2] = "l"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("l")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "l"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                l_location = answer.find("l")
                current_answer = list(current_answer)
                current_answer[l_location*2] = "l"
                current_answer = "".join(current_answer)
        elif "l" in answer and "l" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_m:
        if "m" in answer and "m" not in current_answer:
            if "m" in duplicates.keys():
                a = duplicates["m"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("m")
                        current_answer[a_location * 2] = "m"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("m")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "m"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                m_location = answer.find("m")
                current_answer = list(current_answer)
                current_answer[m_location*2] = "m"
                current_answer = "".join(current_answer)
        elif "m" in answer and "m" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_n:
        if "n" in answer and "n" not in current_answer:
            if "n" in duplicates.keys():
                a = duplicates["n"]#key error
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("n")
                        current_answer[a_location * 2] = "n"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("n")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "n"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                n_location = answer.find("n")
                current_answer = list(current_answer)
                current_answer[n_location*2] = "n"
                current_answer = "".join(current_answer)
        elif "n" in answer and "n" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_o:
        if "o" in answer and "o" not in current_answer:
            if "o" in duplicates.keys():
                a = duplicates["o"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("o")
                        current_answer[a_location * 2] = "o"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("o")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "o"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                o_location = answer.find("o")
                current_answer = list(current_answer)
                current_answer[o_location*2] = "o"
                current_answer = "".join(current_answer)
        elif "o" in answer and "o" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_p:
        if "p" in answer and "p" not in current_answer:
            if "p" in duplicates.keys():
                a = duplicates["p"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("p")
                        current_answer[a_location * 2] = "p"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("p")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "p"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                p_location = answer.find("p")
                current_answer = list(current_answer)
                current_answer[p_location*2] = "p"
                current_answer = "".join(current_answer)
        elif "p" in answer and "p" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_q:
        if "q" in answer and "q" not in current_answer:
            if "q" in duplicates.keys():
                a = duplicates["q"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("q")
                        current_answer[a_location * 2] = "q"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("q")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "q"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                q_location = answer.find("q")
                current_answer = list(current_answer)
                current_answer[q_location*2] = "q"
                current_answer = "".join(current_answer)
        elif "q" in answer and "q" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_r:
        if "r" in answer and "r" not in current_answer:
            if "r" in duplicates.keys():
                a = duplicates["r"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("r")
                        current_answer[a_location * 2] = "r"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("r")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "r"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                r_location = answer.find("r")
                current_answer = list(current_answer)
                current_answer[r_location*2] = "r"
                current_answer = "".join(current_answer)
        elif "r" in answer and "r" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_s:
        if "s" in answer and "s" not in current_answer:
            if "s" in duplicates.keys():
                a = duplicates["s"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("s")
                        current_answer[a_location * 2] = "s"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("s")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "s"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                s_location = answer.find("s")
                current_answer = list(current_answer)
                current_answer[s_location*2] = "s"
                current_answer = "".join(current_answer)
        elif "s" in answer and "s" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_t:
        if "t" in answer and "t" not in current_answer:
            if "t" in duplicates.keys():
                a = duplicates["t"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("t")
                        current_answer[a_location * 2] = "t"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("t")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "t"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                t_location = answer.find("t")
                current_answer = list(current_answer)
                current_answer[t_location*2] = "t"
                current_answer = "".join(current_answer)
        elif "t" in answer and "t" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_u:
        if "u" in answer and "u" not in current_answer:
            if "u" in duplicates.keys():
                a = duplicates["u"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("u")
                        current_answer[a_location * 2] = "u"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("u")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "u"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                u_location = answer.find("u")
                current_answer = list(current_answer)
                current_answer[u_location*2] = "u"
                current_answer = "".join(current_answer)
        elif "u" in answer and "u" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_v:
        if "v" in answer and "v" not in current_answer:
            if "v" in duplicates.keys():
                a = duplicates["v"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("v")
                        current_answer[a_location * 2] = "v"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("v")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "v"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                v_location = answer.find("v")
                current_answer = list(current_answer)
                current_answer[v_location*2] = "v"
                current_answer = "".join(current_answer)
        elif "v" in answer and "v" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_w:
        if "w" in answer and "w" not in current_answer:
            if "w" in duplicates.keys():
                a = duplicates["w"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("w")
                        current_answer[a_location * 2] = "w"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("w")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "w"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                w_location = answer.find("w")
                current_answer = list(current_answer)
                current_answer[w_location*2] = "w"
                current_answer = "".join(current_answer)
        elif "w" in answer and "w" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_x:
        if "x" in answer and "x" not in current_answer:
            if "x" in duplicates.keys():
                a = duplicates["x"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("x")
                        current_answer[a_location * 2] = "x"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("x")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "x"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                x_location = answer.find("x")
                current_answer = list(current_answer)
                current_answer[x_location*2] = "x"
                current_answer = "".join(current_answer)
        elif "x" in answer and "x" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_y:
        if "y" in answer and "y" not in current_answer:
            if "y" in duplicates.keys():
                a = duplicates["y"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("y")
                        current_answer[a_location * 2] = "y"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("y")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "y"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                y_location = answer.find("y")
                current_answer = list(current_answer)
                current_answer[y_location*2] = "y"
                current_answer = "".join(current_answer)
        elif "y" in answer and "y" in current_answer:
            pass
        else:
            score += 1
    if keys==pygame.K_z:
        if "z" in answer and "z" not in current_answer:
            if "z" in duplicates.keys():
                a = duplicates["z"]
                old_index = 0
                temp = answer
                current_answer = list(current_answer)
                for i in range(a):
                    if i == 0:
                        a_location = temp.find("z")
                        current_answer[a_location * 2] = "z"
                        old_index = a_location
                        temp = temp[a_location + 1:]
                    else:
                        a_location = temp.find("z")
                        old_index += a_location + 1
                        current_answer[old_index * 2] = "z"
                        temp = temp[a_location + 1:]
                current_answer = "".join(current_answer)
            else:
                #this won't work if there is more than one "a" in the string
                z_location = answer.find("z")
                current_answer = list(current_answer)
                current_answer[z_location*2] = "z"
                current_answer = "".join(current_answer)
        elif "z" in answer and "z" in current_answer:
            pass
        else:
            score += 1
    return current_answer,score

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

    screen.blit(current_answer_image,(200,400))
    draw_hangman(score)
    draw_noose()
    current_answer_image = font.render(current_answer,False,"black")
    font.render(current_answer, False, "black")
    answer_image = font.render(answer, False, "black")
    if current_answer.replace(" ",'')==answer:
        win_condition = font.render("You win", False, "black")
        screen.blit(win_condition, (300, 350))
        game_over = True
    if score > 4:
        lose_condition = font.render("You lose", False, "black")
        screen.blit(lose_condition, (300,300))
        screen.blit(answer_image, (230, 270))
        game_over = True

    pygame.display.update()
