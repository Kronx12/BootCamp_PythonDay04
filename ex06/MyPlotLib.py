import matplotlib.pyplot as plt
import numpy as np


class MyPlotLib:
    @staticmethod
    def histogram(data, features):
        pass

    @staticmethod
    def density(data, features):
        pass

    @staticmethod
    def pair_plot(data, features):
        pass

    @staticmethod
    def box_plot(data, features):
        fig1, ax1 = plt.subplots()
        ax1.set_title(features)
        ax1.boxplot(data)
        plt.show()


if __name__ == "__main__":
    np.random.seed(19680801)
    spread = np.random.rand(50) * 100
    center = np.ones(25) * 50
    flier_high = np.random.rand(10) * 100 + 100
    flier_low = np.random.rand(10) * -100
    data = np.concatenate((spread, center, flier_high, flier_low))

    MyPlotLib.box_plot(data, ['Test'])