import numpy as np

# Inputs (X) and outputs (y)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

y = np.array([[0],[1],[1],[0]])  # XOR problem

# Initialize weights randomly
np.random.seed(1)
weights = np.random.rand(2,1)

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Training
for i in range(10000):
    inputs = X
    outputs = sigmoid(np.dot(inputs, weights))
    
    error = y - outputs
    adjustments = error * (outputs * (1 - outputs))
    
    weights += np.dot(inputs.T, adjustments)

print("Trained weights:")
print(weights)