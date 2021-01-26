#2-7

#install
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#getPos
x,y,z=mc.player.getTilePos()

try:
    answer = int(input('請問你右邊要放甚麼方塊??'))
    mc.setBlock(x+1,y,z,answer)
    print('完成!')
    mc.postToChat('看看您右邊!!!')
    
except:
    print("只能輸入數字!!!!!!!")