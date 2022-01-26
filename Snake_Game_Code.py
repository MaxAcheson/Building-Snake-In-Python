# Snake Game Code

import curses

# Window Creation
curses.initscr()
window = curses.newwin(20,60,0,0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)


# Snake and Snack
snake = [(4,10),(4,9),(4,8)]
snack = (10,20)

# Game Logic
score = 0

while True:
    event = window.getch()

    for c in snake:
        window.addch(c[0],c[1],'*')
    
    window.addch(snack[0],snack[1],'#')


curses.endwin()
print(f'Final Score = {score}')
