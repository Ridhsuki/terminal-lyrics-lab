#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TrackMaker Lyrics Player
Typing effect parallel dengan custom delay per lirik
Author: Premium Portal 9
"""

import time

CHAR_DELAY = 0.05  

opening_lines = [
    ("", "", 0.3),
    ("怎么办呀", "", 1.0),
    ("Fasshion . Center", "", 0.7)
]

lyrics = [
    ("高峰期的街上堆滿車子", "Gāo fēng qī de jiē shàng duī mǎn chē zi", 0.5),
    ("長長的一隊堵塞 max", "Cháng cháng de yī duì dǔ sè max", 0.7),
    ("House dust 紛飛中", "House dust fēn fēi zhōng", 1.1),
    ("患上了花粉症的 muskmelon", "Huàn shàng le huā fěn zhèng de muskmelon", 3.0)
]

def type_parallel_line(mandarin: str, latin: str):
    """
    Print Mandarin and Latin lines simultaneously per character.
    Previous lines tetap terlihat.
    """
    max_len = max(len(mandarin), len(latin))
    mandarin += ' ' * (max_len - len(mandarin))
    latin += ' ' * (max_len - len(latin))

    for i in range(max_len):
        if i > 0:

            print("\033[F\033[F", end='')
        print(mandarin[:i+1])
        print(latin[:i+1])
        time.sleep(CHAR_DELAY)
    print()  

def display_lyrics_parallel(opening, lyrics_list):
    """
    Display opening lines dan main lyrics dengan parallel typing effect.
    Delay per lirik bisa dikustom.
    """

    for mandarin, latin, delay in opening:
        type_parallel_line(mandarin, latin)
        time.sleep(delay)

    for mandarin, latin, delay in lyrics_list:
        type_parallel_line(mandarin, latin)
        time.sleep(delay)

if __name__ == "__main__":
    display_lyrics_parallel(opening_lines, lyrics)