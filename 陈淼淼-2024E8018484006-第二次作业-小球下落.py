#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math #使用平方根的数学计算函数

def fun(n, init_height=100): #定义一个function函数来计算每一次下落后并反弹到最高点所经过的总路程、总时间；定义初始高度为ini_height,并给初始高度赋值为100米
    def get_n_height(n): #定义子函数：计算第n次下落后的反弹到最高点的高度
        return init_height / (2 ** n) #每一次下落反弹的终点都是上一次下落高度的一半：第n次反弹到最高点的高度=初始高度100米/2的n次方
    def get_n_time(height): #定义自变量为第n次下落高度的子函数：计算第n次下落时，经过高度为height所用的时间
        return math.sqrt(height * 2 / 9.8) #调用math平方根计算，使用自由落体运动公式计算时间：自由落体运动时间t=sqrt(2h/g)，重力加速度取9.8m/s2

    distance_total = init_height #定义第n次下落后反弹到最高点的总路程①为distance_total，并对它初始赋值：初始高度100米
    time_total = get_n_time(init_height) #定义第n次下落后反弹到最高点的总时间①为time_total，使用上面定义的函数get_t_n(height)先计算第一次下落100米的时间，并将该值初始赋值给time_total
    for i in range(1, n): #做循环，计算前n-1次下落+反弹上升的路程及时间，除了第一次下落外，之后下落反弹经过的总路程=初始高度100+前n-1次反弹上升高度×2+第n次反弹上升高度
        length = get_n_height(i) * 2 #第i次反弹下落的路程=第i+1次反弹上升的高度，将反弹上升看作自由落体的逆过程，定义length为“前n-1次反弹上升高度×2”
        distance_total += length #总路程②=初始高度+前n-1次反弹上升下降
        time_total += get_n_time(length / 2) * 2 #总时间②=初始高度下落的时间+前n-1次下落/上升所用时间，由于length是2倍的上升路程，所以自变量部分要➗2，又上升可看作自由落体的逆过程，则所用时间相同，需要×2
        
    length = get_n_height(n) #将第n次反弹上升的高度赋值给length
    distance_total += length #总路程③=总路程②+第n次反弹上升的高度

    time_total += get_n_time(length) #总时间③=总时间②+第n次下落时，经过高度为“第n次反弹上升的高度”所用的时间
    print(f'height of n: {get_n_height(n):.2f}') #保留两位小数输出
    print(f'total height: {distance_total:.2f}')
    print(f'total time: {time_total:.2f}')

fun(10)


# In[ ]:




