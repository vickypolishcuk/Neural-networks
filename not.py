class NeuralNot:
    def __init__(self):
        self.weights = -1.5 # weights generated in a list

    # activation function
    def activate(self, outputP):
        if outputP >= -1:
            return 1
        else:
            return 0

    def predict(self, x):
        outputP = x * self.weights
        outputP = self.activate(outputP)
        return outputP

# Create a perceptron object
neural = NeuralNot()

# Testing
x = int(input("Enter number (0 or 1): "))
outputP = neural.predict(x)
print(f"not {x}: {outputP}")