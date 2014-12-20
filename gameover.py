from mapread import mapread
from time import sleep
import specialfx
import random
from threading import Thread
from schienen import Schiene

def gameover(game):
	mapread(game, "gameover.txt")
	game.lokopizza.screen.refresh()	
	while(True):
		randy = random.randint(2, 22)
		randx = random.randint(2, 78)
		specialfx.explosion(randy, randx, game)
		char = game.lokopizza.screen.instr(randy, randx, 1)
		game.schienen.append(Schiene(randy, randx, game, char))
