import numpy as np

class NeuralNet:
    def __init__(self, na, nb, nc):
        self.w_ab = np.random.rand(nb, na)
        self.b_ab = np.random.rand(nb)
        self.w_bc = np.random.rand(nc, nb)
        self.b_bc = np.random.rand(nc)
        self.grad_b = np.zeros(nb)
        self.grad_c = np.zeros(nc)
    def forward(self, input_data):
        a = input_data
        #
        b = np.dot(self.w_ab, a) + self.b_ab
        b2 = relu(b)
        self.grad_b = relu_grad(b)
        #
        c = np.dot(self.w_bc, b2) + self.b_bc
        c2 = sigmoid(c)
        self.grad_c = sigmoid_grad(c)
        #
        return c2


def relu(x):
    return np.maximum(x, 0)

def relu_grad(x):
    return np.sign(np.maximum(x, 0))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    return np.exp(-x) / ((1 + np.exp(-x)) ** 2)


def main():
    nn = NeuralNet(2, 20, 1)


if __name__ == '__main__':
    main()
