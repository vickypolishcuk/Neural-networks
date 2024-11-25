class NeuralXor:
    def __init__(self):
        self.hidden_weights = [[1, -1], [-1, 1], [1, 1]]  # weights for the hidden layer

    # activation function
    def activate(self, outputP):
        if outputP >= 0.5:
            return 1
        else:
            return 0

    def predict(self, x, y):
        hidden_layer_outputs = []
        for i in range(2):
            hidden_neuron_output = x * self.hidden_weights[i][0] + y * self.hidden_weights[i][1]
            hidden_layer_outputs.append(self.activate(hidden_neuron_output))

        outputP = hidden_layer_outputs[0]*self.hidden_weights[2][0]+hidden_layer_outputs[1]*self.hidden_weights[2][1]
        outputP = self.activate(outputP)
        return outputP

# Create a perceptron object
neural = NeuralXor()

# Testing
x = int(input("Enter first number (0 or 1): "))
y = int(input("Enter second number (0 or 1): "))
outputP = neural.predict(x, y)
print(f"{x} xor {y}: {outputP}")