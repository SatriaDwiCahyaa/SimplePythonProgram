"""
Tic Tac Toe Game
Author: Satria Dwi Cahya
Purpose: 
"""
# Modul untuk memberikan warna pada teks
import os
from termcolor import colored

def clear_screen():
    os.system('cls')


clear_screen()

# Nilai konstan untuk mempermudah
X = 'x'
O = 'O'

# Template untuk papan
board = [   
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


# Menampilkan tanda merah untuk X dan hijau untuk O
def cell(mark):
     
    if mark == X:
        color = 'red'
    else:
        color = 'green'
    
    return colored(mark, color)

# Menampilkan papan
def print_board():
    line = '---+---+---'
    print(line)
    for row in board:
        print(f' {cell(row[0])} | {cell(row[1])} | {cell(row[2])}') 
        print(line) 

# Menentukan pemenang dengan memeriksa setiap bagian: baris, kolom, dan diagonal.
def check_winner():
    print()

# Untuk memvalidasi bahwa papan sudah terisi penuh
def is_full():
    print()

# User input koordnidat papan dan mengatasi eror jika inputan user diluar nilai 
def get_position():
    print()

# Menentukan siapa yang akan bermain serta pemanggilan get_position untuk inputan row dan kolom, dan memvalidasi jika tempat sudah terisi
def get_move():
    print()

# Pemanggilan fungsi dengan Menampilkan papan, user bermain; dan menentukan pemenang, dan stop permainan jika papan penuh
def main():
    print()

