import matplotlib.pyplot as plt  #导入matplotlib库
import numpy as np  #导入numpy库
#创建画布并引入axisartist工具。
import mpl_toolkits.axisartist as axisartist
#创建画布
fig = plt.figure(figsize=(12, 6))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
ax.axis[:].set_visible(False)#通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis["x"] = ax.new_floating_axis(0,0)#ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"].set_axisline_style("-|>", size = 2)#给x坐标轴加上箭头
ax.axis['x'].label.set_fontsize(20)
#添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 2)
ax.axis['y'].label.set_fontsize(20)
#设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("left")
#关闭刻度
#ax.set_xticks([])
#ax.set_yticks([])
'''
#label
ax.axis["x"].label.set_text('time')
ax.axis["y"].label.set_text('output')
#文字刻度
ax.set_title('Actuator output changes across time\n', fontsize = 20, fontweight ='bold') 
ax.set_xticks([8,16,40,48])
ax.set_xticklabels(['t1','t1+1','t1+dt-1','t1+dt'])
ax.axis['x'].major_ticklabels.set_fontsize(16)
ax.set_yticks([0.5])
ax.set_yticklabels(['1.0'])
ax.axis['y'].major_ticklabels.set_fontsize(16)
#刻度定制
#ax.tick_params(axis='x',which='major',rotation=45)

#在带箭头的x-y坐标轴背景下，绘制函数图像
#生成x步长为0.1的列表数据
x = np.arange(0,60,0.1)
#生成y

y=[0 for i in range(0, len(x))]
t1=8
dt=40
for i in range(0, len(x)-1):
    if x[i]>t1 and x[i]<=t1+8:
        y[i] = (x[i]-t1)/16
    elif x[i]>t1+8 and x[i]<=t1+dt-8:
        y[i] = 0.5
    elif x[i]>t1+dt-8 and x[i]<t1+dt:
        y[i] = (-x[i]+t1+dt)/16
# min~max=0~1
plt.axvline(x=16, ymin=0, ymax=0.8333,color='black', linestyle='--')
plt.axvline(x=40, ymin=0, ymax=0.8333,color='black', linestyle='--')
plt.axhline(y=0.5, xmin=0.0, xmax=0.666667, color='black', linestyle='--')   

#设置x、y坐标轴的范围
plt.xlim(0,60)
plt.ylim(0, 0.6)
'''
ax.axis["x"].label.set_text('position')
ax.axis["y"].label.set_text('concentration')
#文字刻度
ax.set_title('Ion concentration changes across position\n', fontsize = 20, fontweight ='bold') 
ax.set_xticks([40])
ax.set_xticklabels(['X_pump'])
ax.axis['x'].major_ticklabels.set_fontsize(16)
ax.set_yticks([0.4])
ax.set_yticklabels(['1.0'])
ax.axis['y'].major_ticklabels.set_fontsize(16)
#刻度定制
#ax.tick_params(axis='x',which='major',rotation=45)

#在带箭头的x-y坐标轴背景下，绘制函数图像
#生成x步长为0.1的列表数据
x = np.arange(0,100,0.1)
#生成y
Xpump = 40
A=0.4;
n=1.25;
z=(x-Xpump)/10;
y =  A*(np.exp(-z*z/n));
# min~max=0~1
plt.axvline(x=Xpump, ymin=0, ymax=A/0.6,color='black', linestyle='--')
plt.axhline(y=0.4, xmin=0.0, xmax=Xpump/100, color='black', linestyle='--')   

#设置x、y坐标轴的范围
plt.xlim(0,100)
plt.ylim(0, 0.6)
#绘制图形
plt.plot(x,y, c='b')
plt.show()
