#! /usr/bin/python3

import random
import termios
import time
import select
import sys
import src.gfx as gfx
import src.window as window

frame_break_s = float(0.08)  # Time to render a single frame.


def frame():  # Frames, logic of rendering:
    global frame_break_s  # Can't be reinitialized.
    window.enemy_x -= 1

    if window.idle(window.enemy_x) == 0:
        gfx.flush_previous_frame()
        if random.randint(0, 4) == 0 and frame_break_s > 0.04:
            frame_break_s -= 0.02  # Increase speed of the game.

        if frame_break_s == 0.08:
            window.score += 1

        elif frame_break_s == 0.06:
            window.score += 2

        else:
            window.score += 3

        window.enemy_x = random.randint(10, (gfx.x_size - window.player_x - 2))
        gfx.flush_previous_frame()


def keypress():  # Keyboard-event.
    key, foo, bar = select.select([sys.stdin], [], [], frame_break_s)
    if key:  # ('Enter' is the best way) is pressed: print with jump.
        return 1  # Any letter but empty and 'Enter' is enough.


window.idle(window.enemy_x)  # Prevent user command history overwriting.
while 1:  # Main game loop.
    if keypress() == 1:
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)  # Flush input buffer.
        gfx.flush_previous_frame()

        if window.anticheat == 2:
            for i in range(2):
                window.idle(window.enemy_x)
                gfx.flush_previous_frame()
            window.anticheat = 0

        for i in range(2):  # Jump width. Must be smaller than player_x.
            gfx.flush_previous_frame()
            window.enemy_x -= 1  # Change enemy position.

            if window.jump(window.enemy_x) == 0:  # Enemy behind a player.
                window.enemy_x = window.enemy_x_reset
            time.sleep(frame_break_s)

    else:
        gfx.flush_previous_frame()
        frame()
