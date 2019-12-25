import random
secret = random.randint(1,10)
print('.........我爱鱼c工作室.....')
temp = input("不妨猜一下小甲鱼心里想着那个数字")
guess = int(temp)
i=1
while   guess!= secret and i<=3:
    
    if guess == secret:
        print("你是小甲鱼心里的蛔虫")
        print("猜中也无奖励")
        
    else:
        if guess>secret:
            print("太大了")
            temp=input("请重新输入一次吧")
            guess=int(temp)
        else:
            print("太小了")
            temp=input("请重新输入一次吧")
            guess=int(temp)
        i=i+1
    
print("游戏结束")
