from time import sleep


def explosion(y, x, game):
    screen = game.lokopizza.screen
    for _ in range(3):
        screen.addstr(y, x, " ")
        screen.refresh()
        # sleep(0.3)
        yield None
    
    oldchar1 = screen.instr(y+1, x+1)
    oldchar2 = screen.instr(y-1, x+1)
    oldchar3 = screen.instr(y-1, x-1)
    oldchar4 = screen.instr(y+1, x-1)
    
    for _ in range(2):
        screen.addstr(y+1, x+1, "*")
        screen.addstr(y-1, x+1, "*")
        screen.addstr(y-1, x-1, "*")
        screen.addstr(y+1, x-1, "*")
        screen.addstr(y, x, " ")
        screen.refresh()
        # sleep(0.2)
        yield None
	
    oldchar11 = screen.instr(y+2, x+2)
    oldchar22 = screen.instr(y-2, x+2)
    oldchar33 = screen.instr(y-2, x-2)
    oldchar44 = screen.instr(y+2, x-2)
    
    screen.addstr(y+2, x+2, "*")
    screen.addstr(y-2, x+2, "*")
    screen.addstr(y-2, x-2, "*")
    screen.addstr(y+2, x-2, "*")
    screen.addstr(y, x, " ")
    screen.refresh()
    # sleep(0.1)
    yield None
    
    screen.addstr(y+1, x+1, oldchar1)
    screen.addstr(y-1, x+1, oldchar2)
    screen.addstr(y-1, x-1, oldchar3)
    screen.addstr(y+1, x-1, oldchar4)
    screen.addstr(y, x, " ")
    screen.refresh()
    # sleep(0.1)
    yield None
    
    screen.addstr(y+2, x+2, oldchar11)
    screen.addstr(y-2, x+2, oldchar22)
    screen.addstr(y-2, x-2, oldchar33)
    screen.addstr(y+2, x-2, oldchar44)
    screen.addstr(y, x, " ")
    screen.refresh()

    for _ in range(20):
        screen.addstr(y, x, " ")
        screen.refresh()
        yield None
