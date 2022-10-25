import numpy as np
import matplotlib.pyplot as plt

def f(n, r, primary):
 return primary * (1 + r/100)**n


x = np.linspace(1,99)
primary = 100
r = 5
y = f(x,r,primary)
ax1 = plt.plot(x,y) 

print(type(ax1))
print(ax1)
plt.show()

#============================================

y1 = np.array([1.0,2.0,3.0,4.0,5.0])
y2 = np.array([1.2,1.6,3.1,4.2,4.8])
y3 = np.array([3.2,1.1,2.0,3.9,2.5])

fig,ax2 = plt.subplots()
print(type(ax2)) #
print(type(fig)) # fig representa a figura background
lines = ax2.plot(y1,'o-',y2,'x--',y3,'*-.')
ax2.set_title("Plot of the data y1,y2, and y3")
ax2.set_xlabel("x axis label")
ax2.set_ylabel("y axis label")
ax2.legend(("data y1","data y2","data y3"))
plt.show()

#==============================================================#

#plot1


x1 = np.array([0,1,2,3])
y2 = np.array([3,8,1,10])

fig,ax3 = plt.subplots(2,2)
ax3.set_title("Plot of the data y2")
ax3.set_xlabel("x axis label")
ax3.set_ylabel("y axis label")
ax3.legend(("data y2"))

plt.subplot(2,2,3)
plt.plot(x1,y2)
plt.title("SALES")

#plot2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(2,2,2)
plt.plot(x1,y2)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

plt.savefig("figure.1.png")