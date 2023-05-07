

import matplotlib.pyplot as plt
import numpy as nd
import pandas as pd

df=pd.read_csv("python_work/testing/acc_data.txt",delimiter=' ')
df.drop('Unnamed: 4', inplace=True, axis=1)
#df['Angle_X'].fillna(90, inplace=True)
#df['Angle_Z'].fillna(45, inplace=True)

t = []
t=df['Time'].to_numpy()
x = []
x=df['Angle_X'].to_numpy()
y = []
y=df['Angle_Y'].to_numpy()
z = []
z=df['Angle_Z'].to_numpy()




df1=pd.read_csv("python_work/testing/servo_data.txt",delimiter=' ')
df1.drop('Unnamed: 3', inplace=True, axis=1)
t1 = []
t1=df1['Time'].to_numpy()
pos = []
pos=df1['Pos'].to_numpy()



fig, axis = plt.subplots(2, 2, figsize=(25,15))

fig.patch.set_facecolor('white')

axis[0,0].plot(t,x)
axis[0,0].set_title('Acc : Angle_X Vs Time')
axis[0,0].set_xlabel('time (ms)')
axis[0,0].set_ylabel('Angle_X')
axis[0,1].plot(t,y)
axis[0,1].set_title('Acc : Angle_Y Vs Time')
axis[0,1].set_xlabel('time (ms)')
axis[0,1].set_ylabel('Angle_Y')
axis[1,0].plot(t,z)
axis[1,0].set_title('Acc : Angle_Z Vs Time')
axis[1,0].set_xlabel('time (ms)')
axis[1,0].set_ylabel('Angle_Z')
axis[1,1].plot(t1,pos)
axis[1,1].set_title('Servo : Pos Vs Time')
axis[1,1].set_xlabel('time (ms)')
axis[1,1].set_ylabel('Pos')

fig.suptitle('Different measures of servo and acc data Vs time', fontsize=12)


plt.savefig('python_work/testing/dataPlot.png')

plt.show()

