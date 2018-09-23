# encoding:utf-8

## 第一部分
print("臭蛋系只烂臭蛋")
print("臭猪系只烂臭猪")
print("爸爸是笨蛋")  #这句是小孩参照以上两句写的


## 第二部分
'''
小孩自己玩的过程中发现a输入了12.01会报错，
于是告诉他int只接受整型数，
要接受有小数点的数，需要把int改成float
'''
a=float(input("a="))
b=int(input("b="))
'''
c/d/e三个输入变量是小孩参照例子加进来的
'''
c=int(input("c="))
d=int(input("d="))
e=int(input("e="))
'''
a-e，每次小孩都可以输入不同的数，如果定义一个不受输入影响的数呢?
于是告诉他像i=12这么定义一个，就不会受影响了
'''
i=12

print("这4个数运算结果是：", (a+b+c)*d)
print("这两个数的差是：",a-b)
print("这两个数的积是:",a*b)
print("这两个数的商是：",a/b)
print("这两个数的余数：",a%b)
print("--->a-b*c+d",a-b*c+d) #这句是小孩参照以上例子写的
print("--->a*b*c*d*i",a*b*c*d*i) #这句是小孩参照以上例子写的

## 第三部分，此部分可根据小孩理解力独立开一课
if(i>a):
    print("i比a大")
if(i<a):
    print("i比a小")
if(i==a):
    print("i等于a")
