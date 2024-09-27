import matplotlib.pyplot as plt
import numpy as np


def simple_line_plot():

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()


def line_plot_with_labels() -> None:
    """Plot sine and cosine waves with labels and fill area below sine wave."""
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, label="sin(x)")
    plt.plot(x, y2, label="cos(x)", linestyle="--")
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.fill_between(x, y1, 0, alpha=0.3)
    plt.legend()
    plt.title("Sine and Cosine Waves")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


line_plot_with_labels()
