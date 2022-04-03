from re import U
import turtle
import random
import os
os.system('mode con cols=20 lines=2')
turtle.title('兰顿蚂蚁')
turtle.screensize(600,600)
turtle.delay(0)
turtle.bgcolor('white')
turtle.speed(0)
turtle.right(270)
move_date=[]
turtle.pencolor('green')
turtle.up()
turtle.ht()
start_move='0000000000'
move_set=turtle.numinput("模式", "1---默认\n2---随机", 1, minval=1,maxval=2)
move_move=turtle.numinput("步数", "请输入一个大于0的数字：", 11000, minval=1)


def pen_goto(g):
    move_date.append(start_move)
    a=g[0:1]
    b=g[1:5]
    c=g[5:6]
    d=g[6:10]
    if int(a) <= 0:
        move1=0-abs(int(b))
    else :
        move1=abs(int(b))
    if int(c) <= 0:
        move2=0-abs(int(d))
    else :
        move2=abs(int(d))
    turtle.right(90)
    dfr=turtle.heading()
##    print(dfr)
    if dfr == 90 :
        move_x=move1
        move_y=move2+5
    elif dfr == 0:
        move_x=move1+5
        move_y=move2
    elif dfr == 270:
        move_x=move1
        move_y=move2-5
    elif dfr == 180:
        move_x=move1-5
        move_y=move2
##    print(move_x,move_y)
    if move_x <= 0 :
        move3='0'
    else:
        move3='1'
    if move_y <= 0 :
        move4='0'
    else:
        move4='1'
    move5=str('%.f'%abs(move_x)).zfill(4)
    move6=str('%.f'%abs(move_y)).zfill(4)
    k=move3+move5+move4+move6
##    print(k)
    turtle.dot(5,'black')   
    turtle.fd(5)
    return(k)


def pen_goto1(g):
    a=g[0:1]
    b=g[1:5]
    c=g[5:6]
    d=g[6:10]
    e=move_date.index(g)
    del move_date[e]    
    if int(a) <= 0:
        move1=0-abs(int(b))
    else :
        move1=abs(int(b))
    if int(c) <= 0:
        move2=0-abs(int(d))
    else :
        move2=abs(int(d))
    turtle.left(90)
    dfr=turtle.heading()
##    print(dfr)
    if dfr == 90 :
        move_x=move1
        move_y=move2+5
    elif dfr == 0:
        move_x=move1+5
        move_y=move2
    elif dfr == 270:
        move_x=move1
        move_y=move2-5
    elif dfr == 180:
        move_x=move1-5
        move_y=move2
##    print(move_x,move_y)      
    if move_x <= 0 :
        move3='0'
    else:
        move3='1'
    if move_y <= 0 :
        move4='0'
    else:
        move4='1'
    move5=str('%.f'%abs(move_x)).zfill(4)
    move6=str('%.f'%abs(move_y)).zfill(4)
    k=move3+move5+move4+move6 
    turtle.dot(5,'white')    
    turtle.fd(5)    
    return(k)


huiihhygig=0
if move_set == 1 or move_set == None :    
    while move_move > 0 :
    ##    print(move_date)
        if start_move not in move_date :
            start_move=pen_goto(start_move)      
        else:
            start_move=pen_goto1(start_move)
        huiihhygig+= 1 
        move_move -= 1
        print('默认模式：',huiihhygig)

elif move_set == 2 :
    hygt=turtle.numinput("随机点", "生成随机点的范围：\nx(-15---15)\ny(-15---15)\n请输入随机次数：", 5, minval=1)
    turtle.goto(0,0)
    for i in range (0,int(hygt)) :
        z=random.randint(0, 1)
        n=random.randrange(0, 15 , 5)
        if z == 0 :
            x_1=0-abs(n)
        else:
            x_1=abs(n)
        o=random.randint(0, 1)
        p=random.randrange(0, 15 , 5)
        if o == 0 :
            y_1=0-abs(p)
        else :
            y_1=abs(p)
        m=str(z)+str(n).zfill(4)+str(o)+str(p).zfill(4)
        if m not in move_date :
            move_date.append(m)
            turtle.goto(x_1,y_1)
            turtle.dot(5,'black')
    turtle.goto(random.randrange(-15, 15,5),random.randrange(-15, 15,5))
    while move_move > 0 :
    ##    print(move_date)
        if start_move not in move_date :
            start_move=pen_goto(start_move)      
        else:
            start_move=pen_goto1(start_move)
        huiihhygig+= 1 
        move_move -= 1
        print(huiihhygig)

turtle.mainloop()
