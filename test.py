import numpy as np
from mayavi import mlab

num_points=200j
x, y, z = np.mgrid[-3:1:num_points, -3:1:num_points, -3:1:num_points]

##############################################FIRST WAY

print(f"x.shape={x.shape}")

conditions=[
    x**2 + y**2 - z,        #<=0
    x**2 + y**2 + z**2 -1   #<=0
]

colors=[
    (1, 0, 0),
    (0, 0, 1)
    ]

conditions_processed=[]
for i in range(len(conditions)):
    cond_i=conditions[i]
    for j in range(len(conditions)):
        if (i==j):
            continue
        cond_j=conditions[j]
        cond_i[cond_j>0.0]=None #See https://stackoverflow.com/questions/40461045/mayavi-combining-two-implicit-3d-surfaces

    conditions_processed.append(cond_i)


mlab.figure('First way (smoother surfaces)', bgcolor = (1,1,1))

for i in range(len(conditions_processed)):
    tmp=mlab.contour3d(x,y,z,conditions_processed[i], contours = [0], color=colors[i], opacity=1.0) 

############################################## SECOND WAY

conditions=[
    x**2 + y**2 - z <=0 ,
    x**2 + y**2 + z**2 -1 <=0
]

values=conditions[0]

for cond in conditions:
    values=values*cond

values=1.0*( ~(values) )

mlab.figure('Second way', bgcolor = (1,1,1))
obj = mlab.contour3d(values, contours=[1e-6], transparent=True)

##############################################

mlab.show()