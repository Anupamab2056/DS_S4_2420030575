import matplotlib.pyplot as plt
plt.subplot(2,3,1)
plt.plot(df['sepal length (cm)'],df['petal length (cm)'])
plt.subplot(2,3,2)
plt.plot(df['sepal width (cm)'],df['petal width (cm)'])
plt.subplot(2,3,3)
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'],c='green')
plt.title('subplots')
plt.show()