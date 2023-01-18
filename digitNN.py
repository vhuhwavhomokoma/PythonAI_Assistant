import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from PIL import Image
import sys

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 600),
            nn.Linear(600, 600),
            nn.Linear(600, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        return self.linear_relu_stack(x)

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using {} device".format(device))
model = NeuralNetwork().to(device)
print(model)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum = 0.5) 

class DigitNeuralNetwork():
 

    def train():
        model.train()
        trainloader = torch.utils.data.DataLoader(torchvision.datasets.MNIST(
        root="data",
            train=True,
            download=True,
            transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor(),torchvision.transforms.Normalize((0.1327,),(0.3104,))
                ])),
            batch_size = 64, shuffle=True)
            
        for batch, (data, target) in enumerate(trainloader):
            output = model(data)
            loss = loss_fn(output, target)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if batch % 100 == 0:
                current = batch * len(data)
                print('[{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(current,len(trainloader.dataset), 100. * batch/len(trainloader), loss.item()))

    def test():  
        testloader = torch.utils.data.DataLoader(torchvision.datasets.MNIST(
        root="data",
        train=False,
            download=True,
            transform=torchvision.transforms.Compose([torchvision.transforms.ToTensor(),torchvision.transforms.Normalize((0.1330,),(0.3110,))
                ])),
            batch_size = 1000, shuffle=True)
        size = len(testloader.dataset)
        model.eval()
        test_loss, correct = 0, 0
        with torch.no_grad():
            for data, target in testloader:
                pred = model(data)
                test_loss += loss_fn(pred, target).item()
                correct += (pred.argmax(1) == target).type(torch.float).sum().item()
        test_loss /= size
        correct /= size
        print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

    for epoch in range(1,5):
        print(f"Epoch {epoch}\n-------------------------------")
        train()
        test()
    print("Done!")
