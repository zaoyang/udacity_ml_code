import numpy as np
import matplotlib.pylab as plt
from sklearn import svm, datasets


# doesn't work
# works well in complicated domain
# doesn't with large data
# doesn't work very well with a lot of noise.
iris = datasets.load_iris()

# training set X, and target label y
X = iris.data[:,:2]
y = iris.target

h = .02 # step size in mesh

# create SVM
C = 100 # More intricate fit and get more points correct vs exact/smooth boundary

# linear kernel
clf = svm.SVC(kernel='rbf', C=C).fit(X,y)



# mesh to plot
x_min, y_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[: 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min,y_max,h),
                     np.arange(y_min,y_max,h))

title = ['SVC with linear kernel']

plt.subplot(2, 2, 1)
plt.subplots_adjust(wspace=0.4, hspace=0.4)

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# put the result into a color plot
Z = Z.reshape(xx.shape)
plt.contourf(xx,yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.title(title)

plt.show()