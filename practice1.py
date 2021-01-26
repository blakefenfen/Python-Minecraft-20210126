#2-5
#install
from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

while True:
    #getPos
    x,y,z, = mc.player.getTilePos()
    
    #random
    
    hm = random.randrange(0,9)
    
    mc.setBlock(x,y,z,38,hm)