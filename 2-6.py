#2-6

#install
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#getPos
x,y,z=mc.player.getTilePos()

answer = int(input('請問你右邊要放甚麼方塊??'))
mc.setBlock(x+1,y,z,answer)
print('完成!')
mc.postToChat('看看您的右邊!!!')