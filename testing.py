import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
a = []
for i in np.arange(1, 90, 10):
    a += [float(i)] 
v = []
v += [float(input("ներմուծել սկզբնական արագությունը = "))] 
g = 9.8
xmax =  2 * np.cos(np.radians(a)) * np.sin(np.radians(a)) * v*v/g
ymax = (v * np.sin(np.radians(a)))**(2)/(2 * g)
x = np.linspace(0, xmax , 100) 
y = x * np.tan(np.radians(a)) - (g * x**(2))/(2*(np.cos(np.radians(a))*v)**(2))
z = x * np.tan(np.radians(a)) - (g * x**(2))/(2*(np.cos(np.radians(a))*v)**(2))
ax.set_title('Ֆունկցիայի գրաֆիկ, y=v0^2 / 2g - gx^2/2v0^2')
print("S(max) = ",xmax," H(max) =",ymax)
ax = fig.add_subplot(projection = '3d')
ax.set_xlabel('s')
ax.set_ylabel('h')
ax.set_zlabel('Z axis')
ax.plot_surface(x, y, z, color='cyan')
plt.grid(True)
plt.show()
