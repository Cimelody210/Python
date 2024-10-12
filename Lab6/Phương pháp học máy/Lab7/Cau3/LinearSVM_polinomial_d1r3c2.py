import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.datasets import make_moons

# Tạo dữ liệu
X, y = make_moons(noise=0.3, random_state=0)

# Hàm vẽ đường biên quyết định
def decision_boundary_plotting(xx, yy, poly_kernel_svm_clf, title):
    Z = poly_kernel_svm_clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(figsize=(10, 10))
    plt.imshow(
        Z,
        interpolation="nearest",
        extent=(xx.min(), xx.max(), yy.min(), yy.max()),
        aspect="auto",
        origin="lower",
        cmap=plt.cm.PuOr_r,
    )
    contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2, linestyles="dashed")
    plt.scatter(X[:, 0], X[:, 1], s=30, c=y, cmap=plt.cm.Paired, edgecolors="k")
    plt.axis([-3, 3, -3, 3])
    plt.title(title)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

# Tạo lưới để vẽ
xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
np.random.seed(0)

# Tạo mô hình SVM với kernel polynomial
poly_kernel_svm_clf = Pipeline([ ("scaler", StandardScaler()),("svm_clf", SVC(kernel="poly", degree=3, coef0=1, C=5))])

# Huấn luyện
poly_kernel_svm_clf.fit(X, y)
# Vẽ đường biên quyết định
decision_boundary_plotting(xx, yy, poly_kernel_svm_clf, 'SVM classifier using polynomial features d=3, r=1, c=5')