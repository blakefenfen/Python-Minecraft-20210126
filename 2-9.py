#2-9

#install
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#getPos
x,y,z = mc.player.getTilePos()

#setSign
mc.setSign(x,y,z+1,63,0,"我愛Minecraft","也愛Python!!")