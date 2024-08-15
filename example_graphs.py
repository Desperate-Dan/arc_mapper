from matplotlib import pyplot as plt
import math
from matplotlib.patches import Arc

# Set up plot
fig, ax = plt.subplots(3,2, figsize=(10,15))


# Plot 1
pointA = [15,15]
pointB = [5,5]
offset = 0.6

new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x")


ax[0,0].grid(True)

ax[0,0].scatter(pointA[0],pointA[1])
ax[0,0].scatter(pointB[0],pointB[1])

ax[0,0].scatter(new_point[0],new_point[1], marker='*')

ax[0,0].plot([pointA[0],pointB[0]], [pointA[1],pointB[1]], lw = 2, alpha=0.5, ls='--')

ax[0,0].axis('equal')
ax[0,0].set(xlim=(0, 20), ylim=(0, 20))

ax[0,0].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8))

# Plot 2
new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x",mid=True,flip=True)

ax[0,1].grid(True)

ax[0,1].scatter(pointA[0],pointA[1])
ax[0,1].scatter(pointB[0],pointB[1])

ax[0,1].scatter(new_point[0],new_point[1], marker='*')

ax[0,1].plot([pointA[0],pointB[0]], [pointA[1],pointB[1]], lw = 2, alpha=0.5, ls='--')

ax[0,1].axis('equal')
ax[0,1].set(xlim=(0, 20), ylim=(0, 20))

ax[0,1].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8))




# Plot 3
pointB, pointA = pointA, pointB

new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x")

ax[1,0].grid(True)

ax[1,0].scatter(pointA[0],pointA[1])
ax[1,0].scatter(pointB[0],pointB[1])

ax[1,0].scatter(new_point[0],new_point[1], marker='*')

ax[1,0].plot([pointA[0],pointB[0]], [pointA[1],pointB[1]], lw = 2, alpha=0.5, ls='--')

ax[1,0].axis('equal')
ax[1,0].set(xlim=(0, 20), ylim=(0, 20))

ax[1,0].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8))

# Plot4
ax[1,1].grid(True)

ax[1,1].scatter(pointA[0],pointA[1])
ax[1,1].scatter(pointB[0],pointB[1])

ax[1,1].scatter(new_point[0],new_point[1], marker='*')

ax[1,1].plot([pointA[0],pointB[0]], [pointA[1],pointB[1]], lw = 2, alpha=0.5, ls='--')

ax[1,1].axis('equal')
ax[1,1].set(xlim=(0, 20), ylim=(0, 20))

ax[1,1].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8, color='green'))

pointA, pointB = pointB, pointA
new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x")

ax[1,1].scatter(new_point[0],new_point[1], marker='*')

ax[1,1].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8, color='red'))

# Plot5

pointA, pointB = pointB, pointA

new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x",flip=True)
ax[2,0].grid(True)

ax[2,0].scatter(pointA[0],pointA[1])
ax[2,0].scatter(pointB[0],pointB[1])

ax[2,0].scatter(new_point[0],new_point[1], marker='*')

ax[2,0].plot([pointA[0],pointB[0]], [pointA[1],pointB[1]], lw = 2, alpha=0.5, ls='--')

ax[2,0].axis('equal')
ax[2,0].set(xlim=(0, 20), ylim=(0, 20))

ax[2,0].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8, color='green'))

pointA, pointB = pointB, pointA

new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x",flip=True)

ax[2,0].scatter(new_point[0],new_point[1], marker='*')

ax[2,0].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8, color='red'))

# Plot6

pointA, pointB = pointB, pointA

new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x",invert=True)
ax[2,1].grid(True)

ax[2,1].scatter(pointA[0],pointA[1])
ax[2,1].scatter(pointB[0],pointB[1])

ax[2,1].scatter(new_point[0],new_point[1], marker='*')

ax[2,1].plot([pointA[0],pointB[0]], [pointA[1],pointB[1]], lw = 2, alpha=0.5, ls='--')

ax[2,1].axis('equal')
ax[2,1].set(xlim=(-10, 30), ylim=(-10, 30))

ax[2,1].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8, color='green'))

pointA, pointB = pointB, pointA

new_point, diameter, t1, t2 = circle_mapper(pointA,pointB,offset,"x",invert=True)

ax[2,1].scatter(new_point[0],new_point[1], marker='*')

ax[2,1].add_patch(Arc((new_point[0], new_point[1]), diameter, diameter, theta1=t1, theta2=t2,
                      facecolor='none', lw=2, alpha=0.8, color='red'))

plt.show()
