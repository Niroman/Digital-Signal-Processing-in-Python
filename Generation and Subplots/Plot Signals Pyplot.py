from matplotlib import pyplot as plt
from matplotlib import style

style.use('dark_background') #Change the background
x=[1,2,3,4,5,6]
y=[6,5,4,3,2,1]

y1=[1,2,3,4,5,6]
x1=[1,1,1,1,1,1]

plt.plot(x,y,label = 'Line One')
plt.plot(x1,y1,label = 'Line One')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Chart")

plt.legend()
plt.show()