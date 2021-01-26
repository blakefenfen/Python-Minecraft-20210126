#2-8

#install
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#ask
userName = input("請輸入姓名:")
message = input("請輸入發言:")
print("")
print("完成!!")

mc.postToChat("§c§l===============")
mc.postToChat("")
mc.postToChat("§e§l發言人§f§l:§a§l" + userName )
mc.postToChat("§e§l發言內容§f§l:§a§l" + message)
mc.postToChat("")
mc.postToChat("§c§l===============")