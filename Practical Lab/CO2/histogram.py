import matplotlib.pyplot as plt
ages=[2,4,5,6,24,56,23,76,32,22,4,66,818,90,34,23,67,22,68,90,33]
range=(0,100)
bins=10
plt.hist(ages,bins,range,color='green',histtype='bar',rwidth=0.8)
plt.xlabel('age')
plt.ylabel('No. of people')
plt.title('My histogram')
plt.show()