import os
import random
def forked():
  bomb = True
  randonum = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  while(bomb == True):
    random1 = random.choice(randonum)
    random2 = random.choice(randonum)
    random3 = random.choice(randonum)
    os.system("clear")
    directory = "⚫" + str(random1) +  str(random2) +  str(random3)
    os.system("mkdir " + directory)
    os.system("clear")
    print("")