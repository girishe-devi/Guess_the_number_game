import numpy as np

# Input and output
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

# Random weights
weights = np.random.rand(2,1)

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Training
for i in range(5000):

    output = sigmoid(np.dot(X, weights))

    error = y - output

    weights += np.dot(X.T, error) * 0.1

# Result
print(output)
