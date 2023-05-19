import matplotlib.pyplot as plt
import numpy as nd
import pandas as pd

#%matplotlib notebook (for jupyter notebook)

df=pd.read_csv("flightSimulatorResults.csv")
#print(df)

t=[]
t=df['Time'].to_numpy()
t=t[::8]

alt=[]
alt=df['Altitude'].to_numpy()
alt=alt[::8]

vel=[]
vel=df['Velocity'].to_numpy()
vel=vel[::8]

acc=[]
acc=df['Acceleration'].to_numpy()
acc=acc[::8]

th=[]
th=df['Thrust'].to_numpy()
th=th[::8]

fig, axis = plt.subplots(2, 2, figsize=(11,7))

axis[0,0].set_xlim(0, 50)
axis[0,0].set_ylim(0, 150)
axis[0,0].set_title('Time Vs Altitude')
axis[0,0].set_xlabel('time (s)')
axis[0,0].set_ylabel('Altitude')

axis[0,1].set_xlim(0, 50)
axis[0,1].set_ylim(-10, 60)
axis[0,1].set_title('Time Vs Velocity')
axis[0,1].set_xlabel('time (s)')
axis[0,1].set_ylabel('Velocity')

axis[1,0].set_xlim(0, 50)
axis[1,0].set_ylim(-15, 40)
axis[1,0].set_title('Time Vs Acceleration')
axis[1,0].set_xlabel('time (s)')
axis[1,0].set_ylabel('Acceleration')

axis[1,1].set_xlim(0, 50)
axis[1,1].set_ylim(0, 25)
axis[1,1].set_title('Time Vs Thrust')
axis[1,1].set_xlabel('time (s)')
axis[1,1].set_ylabel('Thrust')

for i in range(len(t)):
    axis[0,0].plot(t[:i], alt[:i], 'b-')
    axis[0,1].plot(t[:i], vel[:i], 'b-')
    axis[1,0].plot(t[:i], acc[:i], 'b-')
    axis[1,1].plot(t[:i], th[:i], 'b-')
    fig.canvas.draw()
    #plt.savefig("python_work/testing/rtp/plot{i}.png".format(i=i))
    plt.pause(0.000000001)



plt.show()

