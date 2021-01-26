#2-1

#install
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#getPos
x,y,z = mc.player.getTilePos()

#setBlock

mc.setBlock(x,y,z+1,7) #前
mc.setBlock(x,y,z-1,7) #後
mc.setBlock(x-1,y,z,7) #左
mc.setBlock(x+1,y,z,7) #右
mc.setBlock(x,y-1,z,7) #下
mc.setBlock(x-1,y,z+1,7) #前左
mc.setBlock(x+1,y,z+1,7) #前右
mc.setBlock(x-1,y,z-1,7) #後左
mc.setBlock(x+1,y,z-1,7) #後右
