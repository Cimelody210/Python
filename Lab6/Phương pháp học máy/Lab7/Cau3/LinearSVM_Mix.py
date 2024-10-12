import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, LinearSVC, SVR
from sklearn.model_selection import train_test_split

X, y =  make_moons(noise=0.3, random_state=0)

xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
np.random.seed(0)

LINE12 = Pipeline([
    ("scaler", StandardScaler()),
    ("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))
    ])
rbf_kernel_svm_clf = Pipeline([("scaler", StandardScaler()), ("svm_clf", SVC(kernel="rbf", gamma=5, C=0.001))])
poly_kernel_svm_clf = Pipeline([("scaler", StandardScaler()),  ("svm_clf", SVC(kernel="poly", degree=10, coef0=10, C=5)) ])
line15 = Pipeline([("scaler", StandardScaler()), ("svm_clf", SVC(kernel="rbf", gamma=0.1, C=0.001))])

LINE12.fit(X, y)
poly_kernel_svm_clf.fit(X, y)
rbf_kernel_svm_clf.fit(X, y)
line15.fit(X, y)

def decision_boundary_plotting(xx, yy,poly_kernel_svm_clf ,title):
    Z = poly_kernel_svm_clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(6,6))
    plt.imshow(
        Z,
        interpolation="nearest",
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        cmap=plt.cm.PuOr_r,
    )
    contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2, linestyles="dashed")
    plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired, edgecolors="k")
    plt.axis([-3, 3, -3, 3])
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

decision_boundary_plotting(xx, yy,LINE12 ,'SVM classifier using polynomial features d=3, r=1,c=5')
decision_boundary_plotting(xx, yy, rbf_kernel_svm_clf ,'SVM classifier using RBF Kernel features γ=5, C=0.001')
decision_boundary_plotting(xx, yy, poly_kernel_svm_clf ,'In[11]: SVM classifier using polynomial features d=10, r=10,c=5')
decision_boundary_plotting(xx, yy, line15 ,'In[15]: SVM classifier using RBF Kernel features γ=10.1, C=0.001')
