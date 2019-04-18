from typing import Tuple
import copy
import pygame
import pygame.font
import sys
import traceback
from pygame.locals import *
from _thread import *
import time
from threading import Thread, Lock

from Client import *

pygame.font.init()
pygame.init()

SCREEN_SIZE = (750, 620)
# screen = pygame.display.set_mode([640,480])
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("中国象棋")
screen.fill([255, 255, 255])

color_RECT = [220, 120, 130]
color_line = [191, 77, 83]
global a
global length
global r_out
a = 50
length = 50  # type: int
global w_pos
global p_pos
w_pos = (a + 11 * length, a + 2.75 * length)
p_pos = (a + 11 * length, a + 7.75 * length)  # type: Tuple[int, float]
global hua
hua = 0

global out
out = 0


def writestate(str, set_pos, screen, color):
    tan = True
    Font = pygame.font.SysFont("SimHei", 32)
    text = Font.render(str, True, color)
    pos = text.get_rect()
    pos.center = set_pos
    if set_pos == p_pos:
        my_rect = [
            a + 9 * length + 3,
            a + 7 * length + 3,
            4 * length - 3,
            1.5 * length - 3,
        ]
        pygame.draw.rect(screen, (255, 255, 255), my_rect, 0)
    else:
        my_rect = [
            a + 9 * length + 3,
            a + 2 * length + 3,
            4 * length - 3,
            1.5 * length - 3,
        ]
        pygame.draw.rect(screen, (255, 255, 255), my_rect, 0)
    screen.blit(text, pos)
    # draw_chessonboard()
    # pygame.display.update()


def writestate1(str, set_pos, screen, color):
    Font = pygame.font.SysFont("SimHei", 32)
    text = Font.render(str, True, color)
    pos = text.get_rect()
    pos.center = set_pos

    # pygame.display.update()
    screen.blit(text, pos)
    # pygame.display.update()
    # draw_chessonboard()


def deaw_feature(screen):
    # print("dwsdsddddddd")
    my_rect = [a + 9 * length, a + 9 * length + 3, 2 * length, length]
    my_rect2 = [a + 11 * length + 3, a + 9 * length + 3, 2 * length, length]
    pygame.draw.rect(screen, (0, 0, 0), my_rect, 1)
    pygame.draw.rect(screen, (0, 0, 0), my_rect2, 1)
    pos = [a + 10 * length, a + 9.5 * length]
    pos1 = [a + 12 * length, a + 9.5 * length]
    writestate1("悔棋", pos, screen, (200, 100, 50))
    writestate1("新局", pos1, screen, (200, 100, 50))


# pygame.display.update()


def draw_aboard():
    rec_length = 8 * length
    rec_width = 9 * length
    position = [a, a]
    my_RECT = [a, a, rec_length, rec_width]
    my_bod = [a - 4, a - 4, rec_length + 8, rec_width + 8]
    pygame.draw.rect(screen, (255, 1, 1), my_bod, 1)
    pygame.draw.rect(screen, color_RECT, my_RECT, 2)
    # pygame.display.flip()

    for i in range(1, 8):
        pygame.draw.line(
            screen, color_line, (a + i * length, a), (a + i * length, a + 4 * length), 2
        )
        pygame.draw.line(
            screen,
            color_line,
            (a + i * length, a + 5 * length),
            (a + i * length, a + 9 * length),
            2,
        )

    for i in range(1, 10):
        pygame.draw.line(
            screen, color_line, (a, i * length + a), (a + 8 * length, i * length + a), 2
        )
    # pygame.display.flip()

    # 士气的路线
    m = 15
    for i in range(1, 2 * length, m):
        pygame.draw.line(
            screen,
            color_line,
            (a + 3 * length + i, a + i),
            (a + 3 * length + i + m / 2, a + i + m / 2),
        )
        pygame.draw.line(
            screen,
            color_line,
            (a + 3 * length + i, a + 7 * length + i),
            (a + 3 * length + i + m / 2, a + 7 * length + i + m / 2),
        )
        pygame.draw.line(
            screen,
            color_line,
            (a + 3 * length + i, a + 2 * length - i),
            (a + 3 * length + i + m / 2, a + 2 * length - i - m / 2),
        )
        pygame.draw.line(
            screen,
            color_line,
            (a + 3 * length + i, a + 9 * length - i),
            (a + 3 * length + i + m / 2, a + 9 * length - i - m / 2),
        )

    color_aaline = [255, 1, 1]
    for i in range(0, 4):
        for j in range(1, 3):
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (a + i * 2 * length + 3, a + j * 3 * length - 15),
                    (a + i * 2 * length + 3, a + j * 3 * length - 3),
                    (a + i * 2 * length + 15, a + j * 3 * length - 3),
                ],
                1,
            )
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (a + i * 2 * length + 3, a + j * 3 * length + 15),
                    (a + i * 2 * length + 3, a + j * 3 * length + 3),
                    (a + i * 2 * length + 15, a + j * 3 * length + 3),
                ],
                1,
            )
    for i in range(1, 5):
        for j in range(1, 3):
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (a + i * 2 * length - 15, a + j * 3 * length - 3),
                    (a + i * 2 * length - 3, a + j * 3 * length - 3),
                    (a + i * 2 * length - 3, a + j * 3 * length - 15),
                ],
                1,
            )
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (a + i * 2 * length - 3, a + j * 3 * length + 15),
                    (a + i * 2 * length - 3, a + j * 3 * length + 3),
                    (a + i * 2 * length - 15, a + j * 3 * length + 3),
                ],
                1,
            )

    # 炮
    for i in range(0, 2):
        for j in range(0, 2):
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (
                        a + length + i * 6 * length + 3,
                        a + 2 * length + j * 5 * length - 15,
                    ),
                    (
                        a + length + i * 6 * length + 3,
                        a + 2 * length + j * 5 * length - 3,
                    ),
                    (
                        a + length + i * 6 * length + 15,
                        a + 2 * length + j * 5 * length - 3,
                    ),
                ],
                1,
            )
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (
                        a + length + i * 6 * length + 3,
                        a + 2 * length + j * 5 * length + 15,
                    ),
                    (
                        a + length + i * 6 * length + 3,
                        a + 2 * length + j * 5 * length + 3,
                    ),
                    (
                        a + length + i * 6 * length + 15,
                        a + 2 * length + j * 5 * length + 3,
                    ),
                ],
                1,
            )
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (
                        a + length + i * 6 * length - 3,
                        a + 2 * length + j * 5 * length - 15,
                    ),
                    (
                        a + length + i * 6 * length - 3,
                        a + 2 * length + j * 5 * length - 3,
                    ),
                    (
                        a + length + i * 6 * length - 15,
                        a + 2 * length + j * 5 * length - 3,
                    ),
                ],
                1,
            )
            pygame.draw.aalines(
                screen,
                color_aaline,
                False,
                [
                    (
                        a + length + i * 6 * length - 3,
                        a + 2 * length + j * 5 * length + 15,
                    ),
                    (
                        a + length + i * 6 * length - 3,
                        a + 2 * length + j * 5 * length + 3,
                    ),
                    (
                        a + length + i * 6 * length - 15,
                        a + 2 * length + j * 5 * length + 3,
                    ),
                ],
                1,
            )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 13 * length, a + 2 * length),
        (a + 13 * length, a + 3.5 * length),
        2,
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 9 * length, a + 2 * length),
        (a + 9 * length, a + 3.5 * length),
        2,
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 13 * length, a + 2 * length),
        (a + 9 * length, a + 2 * length),
        2,
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 9 * length, a + 3.5 * length),
        (a + 13 * length, a + 3.5 * length),
        2,
    )

    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 13 * length, a + 7 * length),
        (a + 13 * length, a + 8.5 * length),
        2,
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 9 * length, a + 7 * length),
        (a + 9 * length, a + 8.5 * length),
        2,
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 13 * length, a + 7 * length),
        (a + 9 * length, a + 7 * length),
        2,
    )
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (a + 9 * length, a + 8.5 * length),
        (a + 13 * length, a + 8.5 * length),
        2,
    )
    # pygame.display.update()
    # pygame.display.flip()

    writestate1("楚河", (a + length + 50, a + 4 * length + 25), screen, (255, 0, 0))
    writestate1("汉界", (a + 5 * length + 50, a + 4 * length + 25), screen, (0, 0, 0))
    deaw_feature(screen)
    # writestate("汉界", (a + 11 * length, a + 2.75 * length), screen,(62, 61, 50))
    global hua
    if hua == 0:
        writestate1("红方3", p_pos, screen, (255, 0, 0))
        hua = hua + 1


def draw_chessonboard():
    global r_out, hua
    print(hua)
    screen.fill([255, 255, 255])
    if out == 6:
        writestate("黑方胜利", w_pos, screen, (0, 0, 0))
    if out == 7:
        writestate("红方胜利", w_pos, screen, (255, 0, 0))
    if out == 0:
        print("122233333333333333333333")
        if hua != 1:
            print(hua)
            writestate("", w_pos, screen, (255, 255, 255))
            print("122233sdffffffffff33333333333")
    else:
        if out == 1:
            writestate("黑方胜利", w_pos, screen, (0, 0, 0))
            print("wwwwwwwwwwwwwwwww")
        if out == 2:
            writestate("红方胜利", w_pos, screen, (255, 0, 0))
            print("eeeeeeeeeeeeeeeeeee")
        if out == 3:
            writestate("黑方将军", w_pos, screen, (0, 0, 0))
            print("dddddddddddddddddddddddd")
        if out == 4:
            writestate("红方将军", w_pos, screen, (255, 0, 0))
            print("1ffffffffffffffffffffff3")

        r_out = out
    #           time.sleep(1)
    draw_aboard()
    # time.sleep(1)
    for chess in red_chess.keys():
        draw_chess(
            screen,
            chess[0],
            red_chess[chess]["color"],
            red_chess[chess]["coordinate"][0],
            red_chess[chess]["coordinate"][1],
        )
    for chess in black_chess.keys():
        draw_chess(
            screen,
            chess[0],
            black_chess[chess]["color"],
            black_chess[chess]["coordinate"][0],
            black_chess[chess]["coordinate"][1],
        )
    # pygame.display.flip()
    # pygame.display.flip()
    # pygame.display.update()
    global position


def draw_chessonboard_w(c1, c2, c3, c4):
    # screen.fill([255,  255, 255])
    #           time.sleep(1)
    # draw_aboard()
    # time.sleep(1)
    for chess in red_chess.keys():
        if chess == c3 or chess == c4:
            draw_chess(
                screen,
                chess[0],
                red_chess[chess]["color"],
                red_chess[chess]["coordinate"][0],
                red_chess[chess]["coordinate"][1],
            )
    for chess in black_chess.keys():
        if chess == c1 or chess == c2:
            draw_chess(
                screen,
                chess[0],
                black_chess[chess]["color"],
                black_chess[chess]["coordinate"][0],
                black_chess[chess]["coordinate"][1],
            )
    # pygame.display.flip()
    # pygame.display.flip()
    # pygame.display.update()
    global position


red_color = (250, 0, 0)
black_color = (0, 0, 0)


def Draw_cir(x, y):
    r = int(a / 2) - 2
    pygame.draw.circle(screen, (12, 12, 0), (x, y), r)
    pygame.draw.circle(screen, (255, 255, 255), (x, y), r - 1)
    pygame.draw.circle(screen, (205, 124, 71), (x, y), r - 3)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), r - 5)
    pygame.draw.circle(screen, (198, 175, 125), (x, y), r - 6)
    # pygame.display.update()
    # pygame.display.flip()


# draw_aboard()


def draw_chess(screen, chess, color, x, y):
    # 画圆
    x = a + x * length
    y = a + y * length
    Draw_cir(x, y)
    Font_chess = pygame.font.SysFont("SimHei", 30)
    if color == "red":
        txt = Font_chess.render(chess, True, red_color)

    else:
        txt = Font_chess.render(chess, True, black_color)
    screen.blit(txt, (x - 15, y - 15))
    # pygame.display.update()


def get_red_chess(pos):
    for chess in red_chess.keys():
        if red_chess[chess]["coordinate"] == pos:
            # print(chess)
            return chess
    return None


def get_black_chess(pos):
    global black_chess
    for chess in black_chess.keys():
        if black_chess[chess]["coordinate"] == pos:
            # print(chess)
            return chess
    return None


# 判断是否将军
def to_win():
    # 红
    # global red_chess, black_chess, position
    global out
    pos_shuai = []
    pos_jiang = []
    for chess in red_chess.keys():
        if red_chess[chess]["coordinate"] == [-2, -2]:
            pass
        if chess == "帅":
            pos_shuai = red_chess[chess]["coordinate"]

    for chess in black_chess.keys():
        if chess == "将":
            pos_jiang = black_chess[chess]["coordinate"]

    flag = 0
    if pos_jiang[0] == pos_shuai[0]:
        for i in range(pos_shuai[1] + 1, pos_jiang[1]):
            if position[i][pos_jiang[0]] != 0:
                flag = flag + 1
    else:
        flag = 1
    if flag == 0:
        if master == 0:
            writestate("黑方胜利1", w_pos, screen, (0, 0, 0))
            out = 1
        else:
            writestate("红方胜利1", w_pos, screen, (255, 0, 0))
            out = 2
    # 红方将军
    for chess in red_chess.keys():

        pos = red_chess[chess]["coordinate"]
        if red_chess[chess]["coordinate"] == [-2, -2]:
            pass
        else:
            if chess[0] == "兵":
                if (abs(pos[0] - pos_jiang[0]) == 1 and pos[1] == pos_jiang[1]) or (
                        pos_jiang[1] - pos[1] == 1 and pos[0] == pos_jiang[0]
                ):
                    writestate("红方将军", w_pos, screen, (255, 0, 0))
                    out = 4
                # print("红方将军")
                else:
                    pass
            if chess[0] == "車":
                xx = 0

                if pos[0] == pos_jiang[0]:
                    if pos[1] < pos_jiang[1]:
                        for i in range(pos[1] + 1, pos_jiang[1]):
                            # print(position[i][pos[0]])
                            if position[i][pos[0]] != 0:
                                # print(position[i][pos[0]])
                                xx = 1
                    if pos[1] > pos_jiang[1]:
                        for i in range(pos_jiang[1] + 1, pos[1]):
                            if position[i][pos[0]] != 0:
                                xx = 1
                elif pos[1] == pos_jiang[1]:
                    if pos[0] < pos_jiang[0]:
                        for i in range(pos[0] + 1, pos_jiang[0]):
                            if position[pos[1]][i] != 0:
                                xx = 1
                    if pos[0] > pos_jiang[0]:
                        for i in range(pos_jiang[0] + 1, pos[0]):
                            if position[pos[1]][i] != 0:
                                xx = 1
                else:
                    xx = 1

                if xx == 0:
                    writestate("红方将军", w_pos, screen, (255, 0, 0))
                    out = 4
                else:
                    pass
            if chess[0] == "马":
                xx = 0
                e_pos = pos_jiang
                s_pos = pos
                if abs(e_pos[0] - s_pos[0]) == 1 and abs(e_pos[1] - s_pos[1]) == 2:
                    if position[int((e_pos[1] + s_pos[1]) / 2)][s_pos[0]] == 0:
                        xx = 0
                    else:
                        xx = 1
                elif abs(e_pos[0] - s_pos[0]) == 2 and abs(e_pos[1] - s_pos[1]) == 1:
                    if position[s_pos[1]][int((e_pos[0] + s_pos[0]) / 2)] == 0:
                        xx = 0
                    else:
                        xx = 1
                else:
                    xx = 1
                if xx == 0:
                    writestate("红方将军", w_pos, screen, (255, 0, 0))
                    out = 4
                else:
                    pass
            if chess[0] == "炮":
                xx = 0

                if pos[0] == pos_jiang[0]:
                    if pos[1] < pos_jiang[1]:
                        for i in range(pos[1] + 1, pos_jiang[1]):
                            # print(position[i][pos[0]])
                            if position[i][pos[0]] != 0:
                                # print(position[i][pos[0]])
                                xx = xx + 1
                    if pos[1] > pos_jiang[1]:
                        for i in range(pos_jiang[1] + 1, pos[1]):
                            if position[i][pos[0]] != 0:
                                xx = xx + 1
                elif pos[1] == pos_jiang[1]:
                    if pos[0] < pos_jiang[0]:
                        for i in range(pos[0] + 1, pos_jiang[0]):
                            if position[pos[1]][i] != 0:
                                xx = xx + 1
                    if pos[0] > pos_jiang[0]:
                        for i in range(pos_jiang[0] + 1, pos[0]):
                            if position[pos[1]][i] != 0:
                                xx = xx + 1
                else:
                    xx = 0

                if xx == 1:
                    writestate("红方将军", w_pos, screen, (255, 0, 0))
                    out = 4
                else:
                    pass
    # 黑方将军
    for chess in black_chess.keys():

        pos = black_chess[chess]["coordinate"]
        if black_chess[chess]["coordinate"] == [-2, -2]:
            pass
        else:
            if chess[0] == "卒":
                if (abs(pos[0] - pos_shuai[0]) == 1 and pos[1] == pos_shuai[1]) or (
                        pos_shuai[1] - pos[1] == -1 and pos[0] == pos_shuai[0]
                ):
                    writestate("黑方将军", w_pos, screen, (0, 0, 0))
                    out = 3
                else:
                    pass
            if chess[0] == "車":
                xx = 0

                if pos[0] == pos_shuai[0]:
                    if pos[1] < pos_shuai[1]:
                        for i in range(pos[1] + 1, pos_shuai[1]):
                            # print(position[i][pos[0]])
                            if position[i][pos[0]] != 0:
                                # print(position[i][pos[0]])
                                xx = 1
                    if pos[1] > pos_shuai[1]:
                        for i in range(pos_shuai[1] + 1, pos[1]):
                            if position[i][pos[0]] != 0:
                                xx = 1
                elif pos[1] == pos_shuai[1]:
                    if pos[0] < pos_shuai[0]:
                        for i in range(pos[0] + 1, pos_shuai[0]):
                            if position[pos[1]][i] != 0:
                                xx = 1
                    if pos[0] > pos_shuai[0]:
                        for i in range(pos_shuai[0] + 1, pos[0]):
                            if position[pos[1]][i] != 0:
                                xx = 1
                else:
                    xx = 1

                if xx == 0:
                    writestate("黑方将军", w_pos, screen, (0, 0, 0))
                    out = 3
                else:
                    pass
            if chess[0] == "马":
                xx = 0
                e_pos = pos_shuai
                s_pos = pos
                if abs(e_pos[0] - s_pos[0]) == 1 and abs(e_pos[1] - s_pos[1]) == 2:
                    if position[int((e_pos[1] + s_pos[1]) / 2)][s_pos[0]] == 0:
                        xx = 0
                    else:
                        xx = 1
                elif abs(e_pos[0] - s_pos[0]) == 2 and abs(e_pos[1] - s_pos[1]) == 1:
                    if position[s_pos[1]][int((e_pos[0] + s_pos[0]) / 2)] == 0:
                        xx = 0
                    else:
                        xx = 1
                else:
                    xx = 1
                if xx == 0:
                    writestate("黑方将军", w_pos, screen, (0, 0, 0))
                    out = 3
                else:
                    pass
            if chess[0] == "炮":
                xx = 0

                if pos[0] == pos_shuai[0]:
                    if pos[1] < pos_shuai[1]:
                        for i in range(pos[1] + 1, pos_shuai[1]):
                            # print(position[i][pos[0]])
                            if position[i][pos[0]] != 0:
                                # print(position[i][pos[0]])
                                xx = xx + 1
                    if pos[1] > pos_shuai[1]:
                        for i in range(pos_shuai[1] + 1, pos[1]):
                            if position[i][pos[0]] != 0:
                                xx = xx + 1
                elif pos[1] == pos_shuai[1]:
                    if pos[0] < pos_shuai[0]:
                        for i in range(pos[0] + 1, pos_shuai[0]):
                            if position[pos[1]][i] != 0:
                                xx = xx + 1
                    if pos[0] > pos_shuai[0]:
                        for i in range(pos_shuai[0] + 1, pos[0]):
                            if position[pos[1]][i] != 0:
                                xx = xx + 1
                else:
                    xx = 0

                if xx == 1:
                    writestate("黑方将军", w_pos, screen, (0, 0, 0))
                    out = 3
                else:
                    pass


def move(p, s_pos, e_pos, chess):
    global out
    if p == 0:  # 红移动
        red_chess[chess]["coordinate"] = e_pos
    if p == 1:  # 黑移动
        black_chess[chess]["coordinate"] = e_pos
    if p == 2:  # 红方吃子
        red_chess[chess]["coordinate"] = e_pos
        chess_1 = get_black_chess(e_pos)
        black_chess[chess_1]["coordinate"] = [-2, -2]
        if chess_1 == "将":
            # draw_chessonboard()
            writestate("红方胜利", w_pos, screen, (255, 0, 0))
            out = 7
            # pygame.display.update()
            # draw_chessonboard()
            # sys.exit()
    if p == 3:  # 黑方吃子
        black_chess[chess]["coordinate"] = e_pos
        chess_1 = get_red_chess(e_pos)
        red_chess[chess_1]["coordinate"] = [-2, -2]
        if chess_1 == "帅":
            writestate("黑方胜利", w_pos, screen, (0, 0, 0))
            # pygame.display.update()
            out = 6
            # draw_chessonboard()
            # ys.exit()
    position[e_pos[1]][e_pos[0]] = position[s_pos[1]][s_pos[0]]
    position[s_pos[1]][s_pos[0]] = 0

    to_win()


def way(people, s_pos, e_pos):
    global master
    if people == 0 or people == 2:  # 红棋
        chess = get_red_chess(s_pos)
        if chess[0] == "帅":
            if e_pos[0] in range(3, 6) and e_pos[1] in range(0, 3):
                if (
                        abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 0
                ) or (abs(s_pos[0] - e_pos[0]) == 0 and abs(s_pos[1] - e_pos[1]) == 1):
                    # print(s_pos, e_pos)

                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0

                    # writestate("移动方式错误！",w_pos,screen,(255,0,0))
            else:

                return 0
                # print("请选择正确的落子点")
                # writestate("请选择正确的落子点", w_pos, screen, (255, 0, 0))
        if chess[0] == "士":
            if e_pos[0] in range(3, 6) and e_pos[1] in range(0, 3):
                if (
                        abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1
                ) or (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1):

                    # print(s_pos, e_pos)
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                return 0
        if chess[0] == "相":
            if e_pos[0] in range(0, 9) and e_pos[1] in range(0, 5):
                if (
                        abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2
                ) and (
                        position[int((e_pos[1] + s_pos[1]) / 2)][
                            int((e_pos[0] + s_pos[0]) / 2)
                        ]
                        == 0
                ):
                    # print(s_pos, e_pos)

                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                return 0
        if chess[0] == "马":
            if abs(e_pos[0] - s_pos[0]) == 1 and abs(e_pos[1] - s_pos[1]) == 2:
                if position[int((e_pos[1] + s_pos[1]) / 2)][s_pos[0]] == 0:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:

                    print("2移动方式错误：别马脚！")
                    return 0
            elif abs(e_pos[0] - s_pos[0]) == 2 and abs(e_pos[1] - s_pos[1]) == 1:
                if position[s_pos[1]][int((e_pos[0] + s_pos[0]) / 2)] == 0:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:

                    print("1移动方式错误：别马脚！")
                    return 0
                    # writestate("移动方式错误！", w_pos, screen, (255, 0, 0))
            else:
                print("3移动方式错误：别马脚！")
                return 0

            # writestate("请选择正确的落子点", w_pos, screen, (255, 0, 0))
        if chess[0] == "車":
            act = 1
            if (s_pos[0] - e_pos[0]) == 0:
                if s_pos[1] < e_pos[1]:
                    for i in range(s_pos[1] + 1, e_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error1")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[1] > e_pos[1]:
                    for i in range(e_pos[1] + 1, s_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error2")
                            act = 0
                            break
                # move(s_pos, e_pos,chess)
            elif (s_pos[1] - e_pos[1]) == 0:
                if s_pos[0] < e_pos[0]:
                    for i in range(s_pos[0] + 1, e_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error3")
                            act = 0
                            break
                    # move(s_pos,e_pos,chess)
                if s_pos[0] > e_pos[0]:
                    for i in range(e_pos[0] + 1, s_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error4")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[0] == e_pos[0]:
                    # print("error5")
                    act = 0
            else:
                act = 0
            if act == 1:
                move(people, s_pos, e_pos, chess)
                return 1
            else:
                return 0
                pass
        if chess[0] == "炮":
            if people == 0:  # 移动
                act = 1
                if (s_pos[0] - e_pos[0]) == 0:
                    if s_pos[1] < e_pos[1]:
                        for i in range(s_pos[1] + 1, e_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                # print("error1")
                                act = 0
                                break
                        # move(s_pos, e_pos,chess)
                    if s_pos[1] > e_pos[1]:
                        for i in range(e_pos[1] + 1, s_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                # print("error2")
                                act = 0
                                break
                    # move(s_pos, e_pos,chess)
                elif (s_pos[1] - e_pos[1]) == 0:
                    if s_pos[0] < e_pos[0]:
                        for i in range(s_pos[0] + 1, e_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error3")
                                act = 0
                                break
                        # move(s_pos,e_pos,chess)
                    if s_pos[0] > e_pos[0]:
                        for i in range(e_pos[0] + 1, s_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error4")
                                act = 0
                                break
                        # move(s_pos, e_pos,chess)
                    if s_pos[0] == e_pos[0]:
                        print("error5")
                        act = 0
                else:
                    act = 0
                if act == 1:
                    move(people, s_pos, e_pos, chess)
                    print("dwsddddddddddddd")
                    return 1
                else:
                    return 0
            else:  # 吃子翻
                act = 0
                if (s_pos[0] - e_pos[0]) == 0:
                    if s_pos[1] < e_pos[1]:
                        for i in range(s_pos[1] + 1, e_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                print("error1")
                                act = act + 1

                        # move(s_pos, e_pos,chess)
                    if s_pos[1] > e_pos[1]:
                        for i in range(e_pos[1] + 1, s_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                print("error2")
                                act = act + 1

                    # move(s_pos, e_pos,chess)
                elif (s_pos[1] - e_pos[1]) == 0:
                    if s_pos[0] < e_pos[0]:
                        for i in range(s_pos[0] + 1, e_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error3")
                                act = act + 1
                        # move(s_pos,e_pos,chess)
                    if s_pos[0] > e_pos[0]:
                        for i in range(e_pos[0] + 1, s_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error4")
                                act = act + 1
                        # move(s_pos, e_pos,chess)
                    if s_pos[0] == e_pos[0]:
                        print("error5")
                        act = 0
                else:
                    # global begin

                    print("请选择正确的落子点")
                    act = 0
                if act == 1:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
        if chess[0] == "兵":
            if s_pos[1] < 5:
                if s_pos[0] == e_pos[0] and e_pos[1] - s_pos[1] == 1:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:

                    print("移动方式错误：兵")
                    print("error1!")
                    return 0
            else:
                if ((s_pos[0] == e_pos[0]) and (e_pos[1] - s_pos[1] == 1)) or (
                        (s_pos[1] - e_pos[1] == 0) and (abs(s_pos[0] - e_pos[0]) == 1)
                ):
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0

    if people == 1 or people == 3:  # 黑棋
        chess = get_black_chess(s_pos)
        if chess[0] == "将":
            if e_pos[0] in range(3, 6) and e_pos[1] in range(7, 10):
                if (
                        abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 0
                ) or (abs(s_pos[0] - e_pos[0]) == 0 and abs(s_pos[1] - e_pos[1]) == 1):
                    print(s_pos, e_pos)

                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                return 0
        if chess[0] == "仕":
            if e_pos[0] in range(3, 6) and e_pos[1] in range(7, 10):
                if (
                        abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1
                ) or (abs(s_pos[0] - e_pos[0]) == 1 and abs(s_pos[1] - e_pos[1]) == 1):

                    print(s_pos, e_pos)
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                return 0
        if chess[0] == "象":
            if e_pos[0] in range(0, 9) and e_pos[1] in range(5, 10):
                if (
                        abs(s_pos[0] - e_pos[0]) == 2 and abs(s_pos[1] - e_pos[1]) == 2
                ) and (
                        position[int((e_pos[1] + s_pos[1]) / 2)][
                            int((e_pos[0] + s_pos[0]) / 2)
                        ]
                        == 0
                ):
                    print(s_pos, e_pos)

                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                return 0
        if chess[0] == "马":
            if abs(e_pos[0] - s_pos[0]) == 1 and abs(e_pos[1] - s_pos[1]) == 2:
                if position[int((e_pos[1] + s_pos[1]) / 2)][s_pos[0]] == 0:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            elif abs(e_pos[0] - s_pos[0]) == 2 and abs(e_pos[1] - s_pos[1]) == 1:
                if position[s_pos[1]][int((e_pos[0] + s_pos[0]) / 2)] == 0:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                return 0
        if chess[0] == "車":
            act = 1
            if (s_pos[0] - e_pos[0]) == 0:
                if s_pos[1] < e_pos[1]:
                    for i in range(s_pos[1] + 1, e_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error1")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[1] > e_pos[1]:
                    for i in range(e_pos[1] + 1, s_pos[1]):
                        if position[i][s_pos[0]] != 0:
                            print("error2")
                            act = 0
                            break
                # move(s_pos, e_pos,chess)
            elif (s_pos[1] - e_pos[1]) == 0:
                if s_pos[0] < e_pos[0]:
                    for i in range(s_pos[0] + 1, e_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error3")
                            act = 0
                            break
                    # move(s_pos,e_pos,chess)
                if s_pos[0] > e_pos[0]:
                    for i in range(e_pos[0] + 1, s_pos[0]):
                        if position[s_pos[1]][i] != 0:
                            print("error4")
                            act = 0
                            break
                    # move(s_pos, e_pos,chess)
                if s_pos[0] == e_pos[0]:
                    print("error5")
                    act = 0
            else:
                # global begin

                print("请选择正确的落子点")
                act = 0
            if act == 1:
                move(people, s_pos, e_pos, chess)
                return 1
            else:
                return 0
        if chess[0] == "炮":
            if people == 1:
                act = 1
                if (s_pos[0] - e_pos[0]) == 0:
                    if s_pos[1] < e_pos[1]:
                        for i in range(s_pos[1] + 1, e_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                print("error1")
                                act = 0
                                break
                        # move(s_pos, e_pos,chess)
                    if s_pos[1] > e_pos[1]:
                        for i in range(e_pos[1] + 1, s_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                print("error2")
                                act = 0
                                break
                    # move(s_pos, e_pos,chess)
                elif (s_pos[1] - e_pos[1]) == 0:
                    if s_pos[0] < e_pos[0]:
                        for i in range(s_pos[0] + 1, e_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error3")
                                act = 0
                                break
                        # move(s_pos,e_pos,chess)
                    if s_pos[0] > e_pos[0]:
                        for i in range(e_pos[0] + 1, s_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error4")
                                act = 0
                                break
                        # move(s_pos, e_pos,chess)
                    if s_pos[0] == e_pos[0]:
                        print("error5")
                        act = 0
                else:
                    print("error6")
                    act = 0
                if act == 1:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                act = 0
                if (s_pos[0] - e_pos[0]) == 0:
                    if s_pos[1] < e_pos[1]:
                        for i in range(s_pos[1] + 1, e_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                print("error1")
                                act = act + 1
                        # move(s_pos, e_pos,chess)
                    if s_pos[1] > e_pos[1]:
                        for i in range(e_pos[1] + 1, s_pos[1]):
                            if position[i][s_pos[0]] != 0:
                                print("error2")
                                act = act + 1
                    # move(s_pos, e_pos,chess)
                elif (s_pos[1] - e_pos[1]) == 0:
                    if s_pos[0] < e_pos[0]:
                        for i in range(s_pos[0] + 1, e_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error3")
                                act = act + 1
                        # move(s_pos,e_pos,chess)
                    if s_pos[0] > e_pos[0]:
                        for i in range(e_pos[0] + 1, s_pos[0]):
                            if position[s_pos[1]][i] != 0:
                                print("error4")
                                act = act + 1
                        # move(s_pos, e_pos,chess)
                    if s_pos[0] == e_pos[0]:
                        print("error5")

                        act = 0
                else:
                    print("error6")
                    act = 0
                if act == 1:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
        if chess[0] == "卒":
            if s_pos[1] > 4:
                if s_pos[0] == e_pos[0] and e_pos[1] - s_pos[1] == -1:
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
            else:
                if ((s_pos[0] == e_pos[0]) and (e_pos[1] - s_pos[1] == -1)) or (
                        (s_pos[1] - e_pos[1] == 0) and (abs(s_pos[0] - e_pos[0]) == 1)
                ):
                    move(people, s_pos, e_pos, chess)
                    return 1
                else:
                    return 0
    dec1 = [1, 1, 1, 1]
    c1 = get_black_chess(s_pos)
    c2 = get_black_chess(e_pos)
    c3 = get_red_chess(s_pos)
    c4 = get_red_chess(e_pos)


def chess_move(position_x, position_y):
    global begin
    global master, start_pos
    if begin == True:  # 选择第一个棋子
        # position_x, position_y = pygame.mouse.get_pos()
        # 鼠标点击的位置在棋盘内
        if (
                (position_x < a + 8 * length + length / 2)
                and (position_y < a + 9 * length + length / 2)
                and (position_x > a - length / 2)
                and (position_y > a - length / 2)
        ):
            x = int((position_x - a + length / 2) / length)
            y = int((position_y - a + length / 2) / length)
            print(x, y, "qi")
            if master == True:  # 红方
                # writestate("红方", p_pos, screen, (255, 0, 0))
                if position[y][x] == 0 or position[y][x] > 7:  # 选择了红棋
                    print("请选择一个红方棋子！！！")
                    master = True
                    # begin = not begin
                else:
                    chess = position[y][x]
                    master = not master
                    print(master)
                    start_pos = [x, y]
                    begin = not begin
            else:  # 黑方
                if position[y][x] == 0 or position[y][x] < 8:
                    # writestate("黑方", p_pos, screen, (0, 0, 0))
                    print("请选择一个黑方棋子！！！")
                    master = False
                # begin = not begin
                else:
                    chess = position[y][x]
                    master = not master
                    start_pos = [x, y]
                    begin = not begin

            # 选在落点
            # begin = not begin

        else:
            print("请选择正确的位置！！！")
            begin = True
            pass

        # 终点
    else:  # 选择落子的位置
        # position_x, position_y = pygame.mouse.get_pos()
        if (
                (position_x < a + 8 * length + length / 2)
                and (position_y < a + 9 * length + length / 2)
                and (position_x > a - length / 2)
                and (position_y > a - length / 2)
        ):
            x = int((position_x - a + length / 2) / length)
            y = int((position_y - a + length / 2) / length)
            print(x, y)
            end_pos = [x, y]
            # begin = not begin
            # print(begin)
            # print("dsd")
            # 由于master已经修改，所以此时的master为相反的
            if position[y][x] == 0:  # 位置为空,移动
                # global start_pos
                if master == False:  # 红
                    # writestate1("红方", p_pos, screen, (255, 0, 0))
                    m = way(0, start_pos, end_pos)
                    draw_chessonboard()
                    print("h1y")
                    print(master)
                    # writestate1("红方", p_pos, screen, (255, 255, 255))
                    if m == 1:
                        begin = True
                        writestate("黑方", p_pos, screen, (0, 0, 0))
                    else:
                        writestate("红方", p_pos, screen, (255, 0, 0))
                else:  # 黑

                    m = way(1, start_pos, end_pos)
                    draw_chessonboard()
                    if m == 1:
                        writestate("红方", p_pos, screen, (255, 0, 0))
                        begin = True
                    else:
                        writestate("黑方", p_pos, screen, (0, 0, 0))

            else:
                if master == False and position[y][x] > 7:  # 红棋吃子
                    m = way(2, start_pos, end_pos)
                    draw_chessonboard()
                    if m == 1:
                        begin = True
                        writestate("黑方", p_pos, screen, (0, 0, 0))
                    else:
                        writestate("红方", p_pos, screen, (255, 0, 0))
                elif master == False and position[y][x] < 8:  # 红棋连续点了两次
                    print("重新选择红棋")
                    begin = False
                    master = False
                    start_pos = end_pos

                else:
                    if master == True and position[y][x] < 8:  # 黑旗吃子
                        m = way(3, start_pos, end_pos)
                        draw_chessonboard()
                        if m == 0:
                            writestate("黑方", p_pos, screen, (0, 0, 0))
                        else:
                            begin = True
                            writestate("红方", p_pos, screen, (255, 0, 0))
                    else:
                        print("重新选择黑棋")
                        begin = False
                        master = True
                        start_pos = end_pos
        else:
            print("请选择正确的位置！！！")
            begin = False
            pass


def main():
    global red_chess
    global black_chess
    print("we")
    global tan
    tan = False
    red_chess = {
        "帅": {"color": "red", "position": [a + 4 * length, a], "coordinate": [4, 0]},
        "士1": {"color": "red", "position": [a + 3 * length, a], "coordinate": [3, 0]},
        "士2": {"color": "red", "position": [a + 5 * length, a], "coordinate": [5, 0]},
        "相1": {"color": "red", "position": [a + 2 * length, a], "coordinate": [2, 0]},
        "相2": {"color": "red", "position": [a + 6 * length, a], "coordinate": [6, 0]},
        "马1": {"color": "red", "position": [a + 1 * length, a], "coordinate": [1, 0]},
        "马2": {"color": "red", "position": [a + 7 * length, a], "coordinate": [7, 0]},
        "車1": {"color": "red", "position": [a + 0 * length, a], "coordinate": [0, 0]},
        "車2": {"color": "red", "position": [a + 8 * length, a], "coordinate": [8, 0]},
        "炮1": {
            "color": "red",
            "position": [a + 1 * length, a + 2 * length],
            "coordinate": [1, 2],
        },
        "炮2": {
            "color": "red",
            "position": [a + 7 * length, a + 2 * length],
            "coordinate": [7, 2],
        },
        "兵1": {
            "color": "red",
            "position": [a + 0 * length, a + 3 * length],
            "coordinate": [0, 3],
        },
        "兵2": {
            "color": "red",
            "position": [a + 2 * length, a + 3 * length],
            "coordinate": [2, 3],
        },
        "兵3": {
            "color": "red",
            "position": [a + 4 * length, a + 3 * length],
            "coordinate": [4, 3],
        },
        "兵4": {
            "color": "red",
            "position": [a + 6 * length, a + 3 * length],
            "coordinate": [6, 3],
        },
        "兵5": {
            "color": "red",
            "position": [a + 8 * length, a + 3 * length],
            "coordinate": [8, 3],
        },
    }
    black_chess = {
        "将": {
            "color": "black",
            "position": [a + 4 * length, a + 9 * length],
            "coordinate": [4, 9],
        },
        "仕1": {
            "color": "black",
            "position": [a + 3 * length, a + 9 * length],
            "coordinate": [3, 9],
        },
        "仕2": {
            "color": "black",
            "position": [a + 5 * length, a + 9 * length],
            "coordinate": [5, 9],
        },
        "象1": {
            "color": "black",
            "position": [a + 2 * length, a + 9 * length],
            "coordinate": [2, 9],
        },
        "象2": {
            "color": "black",
            "position": [a + 6 * length, a + 9 * length],
            "coordinate": [6, 9],
        },
        "马1": {
            "color": "black",
            "position": [a + 1 * length, a + 9 * length],
            "coordinate": [1, 9],
        },
        "马2": {
            "color": "black",
            "position": [a + 7 * length, a + 9 * length],
            "coordinate": [7, 9],
        },
        "車1": {
            "color": "black",
            "position": [a + 0 * length, a + 9 * length],
            "coordinate": [0, 9],
        },
        "車2": {
            "color": "black",
            "position": [a + 8 * length, a + 9 * length],
            "coordinate": [8, 9],
        },
        "炮1": {
            "color": "black",
            "position": [a + 1 * length, a + 7 * length],
            "coordinate": [1, 7],
        },
        "炮2": {
            "color": "black",
            "position": [a + 7 * length, a + 7 * length],
            "coordinate": [7, 7],
        },
        "卒1": {
            "color": "black",
            "position": [a + 0 * length, a + 6 * length],
            "coordinate": [0, 6],
        },
        "卒2": {
            "color": "black",
            "position": [a + 2 * length, a + 6 * length],
            "coordinate": [2, 6],
        },
        "卒3": {
            "color": "black",
            "position": [a + 4 * length, a + 6 * length],
            "coordinate": [4, 6],
        },
        "卒4": {
            "color": "black",
            "position": [a + 6 * length, a + 6 * length],
            "coordinate": [6, 6],
        },
        "卒5": {
            "color": "black",
            "position": [a + 8 * length, a + 6 * length],
            "coordinate": [8, 6],
        },
    }
    red_chess_r = {
        "帅": {"color": "red", "position": [a + 4 * length, a], "coordinate": [4, 0]},
        "士1": {"color": "red", "position": [a + 3 * length, a], "coordinate": [3, 0]},
        "士2": {"color": "red", "position": [a + 5 * length, a], "coordinate": [5, 0]},
        "相1": {"color": "red", "position": [a + 2 * length, a], "coordinate": [2, 0]},
        "相2": {"color": "red", "position": [a + 6 * length, a], "coordinate": [6, 0]},
        "马1": {"color": "red", "position": [a + 1 * length, a], "coordinate": [1, 0]},
        "马2": {"color": "red", "position": [a + 7 * length, a], "coordinate": [7, 0]},
        "車1": {"color": "red", "position": [a + 0 * length, a], "coordinate": [0, 0]},
        "車2": {"color": "red", "position": [a + 8 * length, a], "coordinate": [8, 0]},
        "炮1": {
            "color": "red",
            "position": [a + 1 * length, a + 2 * length],
            "coordinate": [1, 2],
        },
        "炮2": {
            "color": "red",
            "position": [a + 7 * length, a + 2 * length],
            "coordinate": [7, 2],
        },
        "兵1": {
            "color": "red",
            "position": [a + 0 * length, a + 3 * length],
            "coordinate": [0, 3],
        },
        "兵2": {
            "color": "red",
            "position": [a + 2 * length, a + 3 * length],
            "coordinate": [2, 3],
        },
        "兵3": {
            "color": "red",
            "position": [a + 4 * length, a + 3 * length],
            "coordinate": [4, 3],
        },
        "兵4": {
            "color": "red",
            "position": [a + 6 * length, a + 3 * length],
            "coordinate": [6, 3],
        },
        "兵5": {
            "color": "red",
            "position": [a + 8 * length, a + 3 * length],
            "coordinate": [8, 3],
        },
    }
    black_chess_r = {
        "将": {
            "color": "black",
            "position": [a + 4 * length, a + 9 * length],
            "coordinate": [4, 9],
        },
        "仕1": {
            "color": "black",
            "position": [a + 3 * length, a + 9 * length],
            "coordinate": [3, 9],
        },
        "仕2": {
            "color": "black",
            "position": [a + 5 * length, a + 9 * length],
            "coordinate": [5, 9],
        },
        "象1": {
            "color": "black",
            "position": [a + 2 * length, a + 9 * length],
            "coordinate": [2, 9],
        },
        "象2": {
            "color": "black",
            "position": [a + 6 * length, a + 9 * length],
            "coordinate": [6, 9],
        },
        "马1": {
            "color": "black",
            "position": [a + 1 * length, a + 9 * length],
            "coordinate": [1, 9],
        },
        "马2": {
            "color": "black",
            "position": [a + 7 * length, a + 9 * length],
            "coordinate": [7, 9],
        },
        "車1": {
            "color": "black",
            "position": [a + 0 * length, a + 9 * length],
            "coordinate": [0, 9],
        },
        "車2": {
            "color": "black",
            "position": [a + 8 * length, a + 9 * length],
            "coordinate": [8, 9],
        },
        "炮1": {
            "color": "black",
            "position": [a + 1 * length, a + 7 * length],
            "coordinate": [1, 7],
        },
        "炮2": {
            "color": "black",
            "position": [a + 7 * length, a + 7 * length],
            "coordinate": [7, 7],
        },
        "卒1": {
            "color": "black",
            "position": [a + 0 * length, a + 6 * length],
            "coordinate": [0, 6],
        },
        "卒2": {
            "color": "black",
            "position": [a + 2 * length, a + 6 * length],
            "coordinate": [2, 6],
        },
        "卒3": {
            "color": "black",
            "position": [a + 4 * length, a + 6 * length],
            "coordinate": [4, 6],
        },
        "卒4": {
            "color": "black",
            "position": [a + 6 * length, a + 6 * length],
            "coordinate": [6, 6],
        },
        "卒5": {
            "color": "black",
            "position": [a + 8 * length, a + 6 * length],
            "coordinate": [8, 6],
        },
    }
    draw_aboard()
    draw_chessonboard()

    global position
    position = [
        [5, 4, 3, 2, 1, 2, 3, 4, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 6, 0],
        [7, 0, 7, 0, 7, 0, 7, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [14, 0, 14, 0, 14, 0, 14, 0, 14],
        [0, 13, 0, 0, 0, 0, 0, 13, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 11, 10, 9, 8, 9, 10, 11, 12],
    ]
    # position_r = copy.deepcopy(position)
    position_r = [
        [5, 4, 3, 2, 1, 2, 3, 4, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 0, 0, 6, 0],
        [7, 0, 7, 0, 7, 0, 7, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [14, 0, 14, 0, 14, 0, 14, 0, 14],
        [0, 13, 0, 0, 0, 0, 0, 13, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 11, 10, 9, 8, 9, 10, 11, 12],
    ]
    global begin, master
    global r_out
    r_out = 0
    begin = True
    while side == -1:
        pass
    if side == 1:
        master = False
    if side == 0:
        master == True
    global start_pos
    global end_pos
    global chess
    start_pos = (0, 0)
    end_pos = (0, 0)
    chess = 0
    global huinum
    huinum = 0
    # writestate1("红方", p_pos, screen, (255, 0, 0))
    global position_r1, red_chess_r1, black_chess_r1
    global position_r2, red_chess_r2, black_chess_r2
    red_chess_r2 = red_chess
    red_chess_r1 = red_chess
    FPS = 30
    clock = pygame.time.Clock()
    writestate1("红方", p_pos, screen, (255, 0, 0))
    while True:
        global out
        i = 0
        clock.tick(FPS)
        pygame.display.flip()
        out = 0
        if tan == False:
            pygame.display.flip()
            i = 0
        else:
            if i % 2 == 0:
                tan = False
            else:
                i = i + 1
        for event in pygame.event.get():
            # print(pygame.event.__sizeof__())
            if event.type == QUIT:
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                if (
                        pos_x > a + 9 * length - 3
                        and pos_x < a + 11 * length
                        and pos_y > a + 9 * length
                        and pos_y < a + 10 * length
                ):  # 悔棋
                    out = r_out
                    if huinum % 2 == 1:
                        red_chess = red_chess_r1
                        black_chess = black_chess_r1
                        position = position_r1

                        draw_chessonboard()
                        master = not master
                    else:
                        red_chess = red_chess_r2
                        black_chess = black_chess_r2
                        position = position_r2
                        draw_chessonboard()
                        master = not master
                    if master == True:
                        writestate("红方", p_pos, screen, (255, 0, 0))

                    else:
                        writestate("黑方", p_pos, screen, (0, 0, 0))
                if (
                        pos_x > a + 11 * length + 3
                        and pos_x < a + 13 * length + 6
                        and pos_y > a + 9 * length
                        and pos_y < a + 10 * length
                ):  # 新局
                    red_chess = {
                        "帅": {
                            "color": "red",
                            "position": [a + 4 * length, a],
                            "coordinate": [4, 0],
                        },
                        "士1": {
                            "color": "red",
                            "position": [a + 3 * length, a],
                            "coordinate": [3, 0],
                        },
                        "士2": {
                            "color": "red",
                            "position": [a + 5 * length, a],
                            "coordinate": [5, 0],
                        },
                        "相1": {
                            "color": "red",
                            "position": [a + 2 * length, a],
                            "coordinate": [2, 0],
                        },
                        "相2": {
                            "color": "red",
                            "position": [a + 6 * length, a],
                            "coordinate": [6, 0],
                        },
                        "马1": {
                            "color": "red",
                            "position": [a + 1 * length, a],
                            "coordinate": [1, 0],
                        },
                        "马2": {
                            "color": "red",
                            "position": [a + 7 * length, a],
                            "coordinate": [7, 0],
                        },
                        "車1": {
                            "color": "red",
                            "position": [a + 0 * length, a],
                            "coordinate": [0, 0],
                        },
                        "車2": {
                            "color": "red",
                            "position": [a + 8 * length, a],
                            "coordinate": [8, 0],
                        },
                        "炮1": {
                            "color": "red",
                            "position": [a + 1 * length, a + 2 * length],
                            "coordinate": [1, 2],
                        },
                        "炮2": {
                            "color": "red",
                            "position": [a + 7 * length, a + 2 * length],
                            "coordinate": [7, 2],
                        },
                        "兵1": {
                            "color": "red",
                            "position": [a + 0 * length, a + 3 * length],
                            "coordinate": [0, 3],
                        },
                        "兵2": {
                            "color": "red",
                            "position": [a + 2 * length, a + 3 * length],
                            "coordinate": [2, 3],
                        },
                        "兵3": {
                            "color": "red",
                            "position": [a + 4 * length, a + 3 * length],
                            "coordinate": [4, 3],
                        },
                        "兵4": {
                            "color": "red",
                            "position": [a + 6 * length, a + 3 * length],
                            "coordinate": [6, 3],
                        },
                        "兵5": {
                            "color": "red",
                            "position": [a + 8 * length, a + 3 * length],
                            "coordinate": [8, 3],
                        },
                    }
                    black_chess = {
                        "将": {
                            "color": "black",
                            "position": [a + 4 * length, a + 9 * length],
                            "coordinate": [4, 9],
                        },
                        "仕1": {
                            "color": "black",
                            "position": [a + 3 * length, a + 9 * length],
                            "coordinate": [3, 9],
                        },
                        "仕2": {
                            "color": "black",
                            "position": [a + 5 * length, a + 9 * length],
                            "coordinate": [5, 9],
                        },
                        "象1": {
                            "color": "black",
                            "position": [a + 2 * length, a + 9 * length],
                            "coordinate": [2, 9],
                        },
                        "象2": {
                            "color": "black",
                            "position": [a + 6 * length, a + 9 * length],
                            "coordinate": [6, 9],
                        },
                        "马1": {
                            "color": "black",
                            "position": [a + 1 * length, a + 9 * length],
                            "coordinate": [1, 9],
                        },
                        "马2": {
                            "color": "black",
                            "position": [a + 7 * length, a + 9 * length],
                            "coordinate": [7, 9],
                        },
                        "車1": {
                            "color": "black",
                            "position": [a + 0 * length, a + 9 * length],
                            "coordinate": [0, 9],
                        },
                        "車2": {
                            "color": "black",
                            "position": [a + 8 * length, a + 9 * length],
                            "coordinate": [8, 9],
                        },
                        "炮1": {
                            "color": "black",
                            "position": [a + 1 * length, a + 7 * length],
                            "coordinate": [1, 7],
                        },
                        "炮2": {
                            "color": "black",
                            "position": [a + 7 * length, a + 7 * length],
                            "coordinate": [7, 7],
                        },
                        "卒1": {
                            "color": "black",
                            "position": [a + 0 * length, a + 6 * length],
                            "coordinate": [0, 6],
                        },
                        "卒2": {
                            "color": "black",
                            "position": [a + 2 * length, a + 6 * length],
                            "coordinate": [2, 6],
                        },
                        "卒3": {
                            "color": "black",
                            "position": [a + 4 * length, a + 6 * length],
                            "coordinate": [4, 6],
                        },
                        "卒4": {
                            "color": "black",
                            "position": [a + 6 * length, a + 6 * length],
                            "coordinate": [6, 6],
                        },
                        "卒5": {
                            "color": "black",
                            "position": [a + 8 * length, a + 6 * length],
                            "coordinate": [8, 6],
                        },
                    }
                    position = [
                        [5, 4, 3, 2, 1, 2, 3, 4, 5],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 6, 0, 0, 0, 0, 0, 6, 0],
                        [7, 0, 7, 0, 7, 0, 7, 0, 7],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [14, 0, 14, 0, 14, 0, 14, 0, 14],
                        [0, 13, 0, 0, 0, 0, 0, 13, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [12, 11, 10, 9, 8, 9, 10, 11, 12],
                    ]
                    if red_chess != {
                        "帅": {
                            "color": "red",
                            "position": [a + 4 * length, a],
                            "coordinate": [4, 0],
                        },
                        "士1": {
                            "color": "red",
                            "position": [a + 3 * length, a],
                            "coordinate": [3, 0],
                        },
                        "士2": {
                            "color": "red",
                            "position": [a + 5 * length, a],
                            "coordinate": [5, 0],
                        },
                        "相1": {
                            "color": "red",
                            "position": [a + 2 * length, a],
                            "coordinate": [2, 0],
                        },
                        "相2": {
                            "color": "red",
                            "position": [a + 6 * length, a],
                            "coordinate": [6, 0],
                        },
                        "马1": {
                            "color": "red",
                            "position": [a + 1 * length, a],
                            "coordinate": [1, 0],
                        },
                        "马2": {
                            "color": "red",
                            "position": [a + 7 * length, a],
                            "coordinate": [7, 0],
                        },
                        "車1": {
                            "color": "red",
                            "position": [a + 0 * length, a],
                            "coordinate": [0, 0],
                        },
                        "車2": {
                            "color": "red",
                            "position": [a + 8 * length, a],
                            "coordinate": [8, 0],
                        },
                        "炮1": {
                            "color": "red",
                            "position": [a + 1 * length, a + 2 * length],
                            "coordinate": [1, 2],
                        },
                        "炮2": {
                            "color": "red",
                            "position": [a + 7 * length, a + 2 * length],
                            "coordinate": [7, 2],
                        },
                        "兵1": {
                            "color": "red",
                            "position": [a + 0 * length, a + 3 * length],
                            "coordinate": [0, 3],
                        },
                        "兵2": {
                            "color": "red",
                            "position": [a + 2 * length, a + 3 * length],
                            "coordinate": [2, 3],
                        },
                        "兵3": {
                            "color": "red",
                            "position": [a + 4 * length, a + 3 * length],
                            "coordinate": [4, 3],
                        },
                        "兵4": {
                            "color": "red",
                            "position": [a + 6 * length, a + 3 * length],
                            "coordinate": [6, 3],
                        },
                        "兵5": {
                            "color": "red",
                            "position": [a + 8 * length, a + 3 * length],
                            "coordinate": [8, 3],
                        },
                    }:
                        print(red_chess)
                        exit()
                    begin = True
                    master = True
                    draw_chessonboard()
                    writestate("红方", p_pos, screen, (255, 0, 0))
                    out = 5
                    # draw_chessonboard()
                else:
                    chess_move(pos_x, pos_y)
                    if huinum % 2 == 1:
                        position_r1 = copy.deepcopy(position)
                        red_chess_r1 = copy.deepcopy(red_chess)
                        black_chess_r1 = copy.deepcopy(black_chess)

                        huinum = huinum + 1
                    else:
                        position_r2 = copy.deepcopy(position)
                        red_chess_r2 = copy.deepcopy(red_chess)
                        black_chess_r2 = copy.deepcopy(black_chess)

                        huinum = huinum + 1
                    # print(red_chess_r1)
                    # print(red_chess_r2)
                # global position
                # print(position)

        # screen.fill([255, 255, 255])


if __name__ == "__main__":
    try:
        # writestate1("红方", p_pos, screen, (255, 0, 0))
        #start_new_thread( recvie() )
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
