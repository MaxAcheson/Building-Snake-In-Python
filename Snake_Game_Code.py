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

window.addch(snack[0],snack[1],'#')

# Game Logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    window.addstr(0,2, "Score" + str(score) + ' ')
    window.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # increase speed after score

    prev_key = key
    event = window.getch()
    key = event if event ! = -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # Calculate next coordinates
    y = snake[0][0]
    x = snake[0][0]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        y -= 1
    if key == curses.KEY_RIGHT:
        y += 1

    snake.insert(0, (y,x))

    # Border Collision Mechanics
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break

    # Snake Self Collision Mechanics
    if snake[0] in snake[1:]: break

    if snake[0] == snack:
        score += 1
        food = ()
        while food == ():
            food = ()


    for c in snake:
        window.addch(c[0],c[1],'*')
    
    window.addch(snack[0],snack[1],'#')


curses.endwin()
print(f'Final Score = {score}')
