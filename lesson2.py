from random import randint


a = randint(1, 6)
print("魔法球里面的魔法数字已经生成...你猜是多少？")
#print("魔法球里面的数是:",a)
'''
告诉小孩随机数就像一个魔法球，
在有结果之前你永远不知道它是什么。
刚开始可以打开print语句输出魔法数字，
让小孩心算之后输入一个b，控制最后的输出结果（做魔法师）
'''
b = int(input("随便输入一个数:"))

face = (a+b)%6

print("Python老师想今天让你做这件事情:")
if face == 1:
	result = '弹首你最喜欢的曲子'
elif face == 2:
	result = '帮👩洗碗'
elif face == 3:
	result = '给臭蛋换尿片'
elif face == 4:
	result = '可以喝冰箱里面任何的饮料'
elif face == 5:
	result = '叫👨讲个笑话'
else:
	result = '可以约小伙伴到花园踢⚽'
print(result)
print("魔法数字是%d，你输入了%d，最后你要做的是事项%d (a+b)/6=余数是%d" % (a,b,face,face))
