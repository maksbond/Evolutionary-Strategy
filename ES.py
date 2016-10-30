import math
from numpy.random import normal
import random
import numpy as np
from matplotlib import pylab as plt

class ES:
    num_best = 4
    sigma = 0.5

    #constructor
    def __init__(self, func, num_iter=10000, min_range=-10.0, max_range=10.0, size_of_pop=20):
        self.f = func
        self.num_iter = num_iter
        self.min_range = min_range
        self.max_range = max_range
        self.size_of_pop = size_of_pop
        self.x = np.array([float(_) for _ in range(size_of_pop)])

    #init array
    def generate(self):
        for _ in range(self.size_of_pop):
            self.x[_] = (self.max_range - self.min_range) * random.random() + self.min_range
        self.x = np.array(sorted(self.x, key=lambda a: self.f(a), reverse=True))
        print(self.x)

    #start find max of function
    def start(self):
        self.generate()
        for _ in range(self.num_iter):
            self.x_old = self.x[:self.size_of_pop]
            self.best = self.x[:self.num_best]
            self.x = np.array(list())
            for i in range(int(self.size_of_pop / self.num_best)):
                self.x = np.append(self.x, [self.best[j] + normal(0, self.sigma**2) for j in range(self.num_best)])
            if _  != self.num_iter - 1:
                self.x = np.append(self.x, self.x_old)
            self.x = np.array(sorted(self.x, key=lambda a: self.f(a), reverse=True))

    # draw graph of function
    def draw_graph(self, rangey=[-10, 10], name="graph", title="-x^2+1", xlabel="x",
                   ylabel="y", point_x=None, point_y=None):
        plt.ion()
        x = np.arange(self.min_range, self.max_range + 0.1, 0.1)
        y = np.array(self.f(x))
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.axis([self.min_range, self.max_range, rangey[0], rangey[1]])

        if point_x != None and point_y != None:
            plt.scatter(point_x, point_y, color="red")
        plt.savefig(name + ".png")
        plt.ioff()
        plt.show()

    def print(self):
        x = sum(self.x) / self.size_of_pop
        y = self.f(x)
        print(self.x)
        print(x, y)
        self.draw_graph(point_x=x, point_y=y)