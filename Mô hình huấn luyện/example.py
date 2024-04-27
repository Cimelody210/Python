from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X= df.drop(column = ["Grade"])
Y = df["Grade"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state = 42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

accurary = model.score(X_test, y_test)
print("Accurary:", accurary)

# kq = 0.9523809523809523