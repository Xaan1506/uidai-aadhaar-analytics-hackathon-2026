import matplotlib.pyplot as plt


def quick_line(x, y, title: str = None):
    plt.figure()
    plt.plot(x, y)
    if title:
        plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    return plt
