import numpy as np

# Data
# A -> B
# -1 represents missing value

data = np.array([
    [0, 0],
    [0, 1],
    [1, -1],
    [1, 1],
    [0, -1]
])

# Initial probabilities
P_A = np.array([0.5, 0.5])

P_B_A = np.array([
    [0.6, 0.4],   # A = 0
    [0.3, 0.7]    # A = 1
])

# EM Algorithm
for i in range(5):

    countA = np.zeros(2)
    countB = np.zeros((2, 2))

    for row in data:

        A = row[0]
        B = row[1]

        countA[A] += 1

        # Missing value
        if B == -1:

            countB[A][0] += P_B_A[A][0]
            countB[A][1] += P_B_A[A][1]

        else:
            countB[A][B] += 1

    # Update P(A)
    P_A = countA / np.sum(countA)

    # Update P(B|A)
    for A in range(2):

        total = np.sum(countB[A])

        P_B_A[A] = countB[A] / total

# Output
print("Estimated Probability of A")
print(P_A)

print("\nEstimated Conditional Probability P(B|A)")
print(P_B_A)