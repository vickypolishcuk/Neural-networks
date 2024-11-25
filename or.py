class NeuralOr:
    def __init__(self):
        self.weights = [1, 1]  # weights generated in a list

    # activation function
    def activate(self, outputP):
        if outputP >= 0.5:
            return 1
        else:
            return 0

    def predict(self, x, y):
        outputP = x * self.weights[0] + y * self.weights[1]
        outputP = self.activate(outputP)
        return outputP

# Create a perceptron object
neural = NeuralOr()

# Testing
x = int(input("Enter first number (0 or 1): "))
y = int(input("Enter second number (0 or 1): "))
outputP = neural.predict(x, y)
print(f"{x} or {y}: {outputP}")
