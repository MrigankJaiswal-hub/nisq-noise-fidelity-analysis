import matplotlib.pyplot as plt

def plot_curve(x, y, xlabel, ylabel, title):
    plt.figure(figsize=(6,4))
    plt.plot(x, y, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.show()
