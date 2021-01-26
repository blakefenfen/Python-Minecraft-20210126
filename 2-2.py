#2-2

#install
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#getPos
x,y,z = mc.player.getTilePos()

#setBlock 
mc.setBlock(x,y,z+2,7) #前2
mc.setBlock(x,y,z-2,7) #後2
mc.setBlock(x-2,y,z,7) #左2
mc.setBlock(x+2,y,z,7) #右2
mc.setBlock(x,y-1,z,7) #下
mc.setBlock(x-1,y,z+1,7) #前左2
mc.setBlock(x+1,y,z+1,7) #前右2
mc.setBlock(x-1,y,z-1,7) #後左2
mc.setBlock(x+1,y,z-1,7) #後右2