#2-4
#install
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

#getPos
x,y,z, = mc.player.getTilePos()

long = 10
kuang = 8
high = 7

block = 169
air = 0

mc.setBlocks(x,y,z,x+long,y+high,z+kuang,block)
mc.setBlocks(x+1,y+1,z+1,x+long-1,y+high-1,z+kuang-1,air)