import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

blue = (134 / 255, 145 / 255, 191 / 255)
green = (161 / 255, 193 / 255, 129 / 255)
loss = 1.3


def u(x, i):
    # import pdb;pdb.set_trace()
    return np.array(
        [-loss * (-x[x < 0]) ** i] +
        [x[x >= 0] ** (i + .35)]
    ).flatten()


def wp(x, i):
    return x ** i / ((x ** i + (1 - x) ** i) ** (1 / i))


def pwf():
    fig = plt.figure(figsize=(3.9, 3.75))

    ax = fig.add_subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    # ax.spines['left'].set_bounds(-0.05, 1.35)
    # ax.spines['bottom'].set_bounds(-0.05, 1.5)
    alpha = .6
    x = np.linspace(0, 1, 300)

    y = wp(x, alpha)

    sns.lineplot(x, y, color='black', lw=2.2)
    sns.lineplot(x, x, color='black', ls='--')

    # plt.xlim([-1.5, 1.5])
    # plt.ylim([y.min(), y.max()])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$w(x)$')

    plt.title('Probability Weighting')
    # plt.show()
    plt.savefig('figs/4.svg')


def expected_utility():
    fig = plt.figure(figsize=(3.9, 3.75))
    ax = fig.add_subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # ax.spines['left'].set_bounds(-0.05, 1.35)
    # ax.spines['bottom'].set_bounds(-0.05, 1.5)
    alpha = .4
    x = np.linspace(-1.5, 1.5, 300)
    y = u(x, alpha)

    print(y)
    # plt.plot(x, x, color='grey', lw=2, ls='--')
    #  sns.lineplot(x1, u(x1, ex1), color=blue, lw=3)
    plt.axvline(color='black', lw=1)
    plt.axhline(color='black', lw=1)

    sns.lineplot(x, y, color='black', lw=2.2)

    plt.xlim([-1.5, 1.5])
    plt.ylim([y.min(), y.max()])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')

    plt.title('Utility')

    plt.savefig('figs/3.svg')


def main():
    expected_utility()
    pwf()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
