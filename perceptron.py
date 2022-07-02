import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
np.random.seed(1)
X, y = datasets.make_blobs(n_samples=200, centers=2, cluster_std=3)
plt.scatter(X[:,0], X[:,1], c=y)
plt.show()
y_true = y[:, np.newaxis]
X_train, X_test, y_train, y_test = train_test_split(X, y_true)
def train(X, y, learning_rate=0.05, n_iters=100):
    n_samples = len(X)
    n_features = len(X[0])
    weights = np.zeros((n_features,1))
    bias = 0
    for i in range(n_iters):
        a = np.dot(X, weights) + bias
        y_predict = step_function(a)
        delta_w = learning_rate * np.dot(X.T, (y - y_predict))
        delta_b = learning_rate * np.sum(y - y_predict)
        weights += delta_w
        bias += delta_b

    return weights, bias
def step_function(x):
    return np.array([1 if elem >= 0 else 0 for elem in x])[:, np.newaxis]
def predict(X, weights, bias):
    a = np.dot(X, weights) + bias
    return step_function(a)
w_trained, b_trained = train(X_train, y_train)
y_p_test = predict(X_test, w_trained, b_trained)
print(f"accuracy = {100 - np.mean(np.abs(y_p_test - y_test)) * 100}%")
slope = - w_trained[0]/w_trained[1]
intercept = - b_trained/w_trained[1]
x_hyperplane = np.linspace(-10,10,10)
y_hyperplane = slope * x_hyperplane + intercept
fig = plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1], c=y)
plt.plot(x_hyperplane, y_hyperplane, '-')
plt.show()