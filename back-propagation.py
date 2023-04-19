import numpy as np

# Define sigmoid function


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define derivative of sigmoid function


def sigmoid_derivative(x):
    return x * (1 - x)


# Define input data and expected output
input_data = np.array([[1, 1, 0], [1, 1, 1], [1, 0, 1], [1, 0, 0], [1, 1, 1]])
expected_output = np.array([[0], [0], [1], [0], [1]])

# Define hyperparameters
epochs = 9000
learning_rate = 0.1

# Define architecture of neural network
input_layer_size = input_data.shape[1]
hidden_layer_size = 4
output_layer_size = 1

# Initialize weights for input layer to hidden layer and hidden layer to output layer
w1 = np.random.uniform(size=(input_layer_size, hidden_layer_size))
w2 = np.random.uniform(size=(hidden_layer_size, output_layer_size))

# Train neural network using backpropagation
for epoch in range(epochs):
    # Forward propagation
    layer1_output = sigmoid(np.dot(input_data, w1))
    layer2_output = sigmoid(np.dot(layer1_output, w2))

    # Backward propagation
    layer2_error = expected_output - layer2_output
    layer2_delta = layer2_error * sigmoid_derivative(layer2_output)
    layer1_error = layer2_delta.dot(w2.T)
    layer1_delta = layer1_error * sigmoid_derivative(layer1_output)

    # Update weights
    w2 += layer1_output.T.dot(layer2_delta) * learning_rate
    w1 += input_data.T.dot(layer1_delta) * learning_rate

# Print final output
print("Final output:")
print(layer2_output)