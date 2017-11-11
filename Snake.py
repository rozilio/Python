# Snake Game

# import modules
import sys, random, pygame

# check init errors
Check_err = pygame.init()
if Check_err[1] > 0:
    print("(!) Had {0} init errors".format(Check_err[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfuly initialized!")

# play surface
playSurf = pygame.display.set_mode((720 , 460))
