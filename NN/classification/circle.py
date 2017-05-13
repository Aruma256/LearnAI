import numpy as np

class NeuralNet:
    def __init__(self, na, nb, nc, eta):
        self.a = np.zeros(na)
        self.b = np.zeros(nb)
        self.c = np.zeros(nc)
        self.w_ab = np.random.rand(nb, na) - 0.5
        self.b_ab = np.random.rand(nb) - 0.5
        self.w_bc = np.random.rand(nc, nb) - 0.5
        self.b_bc = np.random.rand(nc) - 0.5
        self.grad_b = np.zeros(nb)
        self.grad_c = np.zeros(nc)
        self.eta = eta
    def forward(self, input_data):
        self.a = input_data
        #
        self.b = np.dot(self.w_ab, self.a) + self.b_ab
        b2 = relu(self.b)
        #
        self.c = np.dot(self.w_bc, b2) + self.b_bc
        c2 = sigmoid(self.c)
        #
        self.grad_b = relu_grad(self.b)
        self.grad_c = sigmoid_grad(self.c)
        #
        return c2[0]
    def backward(self, d):
        c2_delta = d
        c_delta = self.grad_c * c2_delta
        b2_delta = self.w_bc.T.dot(c_delta)
        b_delta = self.grad_b * b2_delta
        #
        self.w_bc -= self.eta * np.outer(c_delta, self.b)
        self.b_bc -= self.eta * c_delta
        self.w_ab -= self.eta * np.outer(b_delta, self.a)
        self.b_ab -= self.eta * b_delta

def relu(x):
    return np.maximum(x, 0)

def relu_grad(x):
    return np.sign(np.maximum(x, 0))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_grad(x):
    return np.exp(-x) / ((1 + np.exp(-x)) ** 2)

def gen_data(N):
    data = []
    for _ in range(N):
        input_data = np.random.rand(2) * 4 - 2
        label = np.sqrt(np.sum(input_data ** 2)) < 1
        data.append((input_data, label))
    return data

def test(test_data, nn):
    c = 0
    for data in test_data:
        if data[1] == (nn.forward(data[0]) > 0.5):
            c += 1
    return c / len(test_data)

def main():
    nn = NeuralNet(2, 20, 1, 0.1)
    test_data = gen_data(1000)
    print(test(test_data, nn))
    for i in range(10):
        for data in gen_data(1000):
            o = nn.forward(data[0])
            nn.backward(o - data[1])
        print(test(test_data, nn))


if __name__ == '__main__':
    main()
