import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

blue = (134/255, 145/255, 191/255)
green = (161/255, 193/255, 129/255)

def u(x):
    return np.log(x)

def mu(x):
    return np.exp(x)


def bernouilli_expected_utility():
    fig = plt.figure(figsize=(4, 5))
    ax = fig.add_subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    x = np.linspace(1, 7, 50)
    x1 = 2
    x2 = 3
   # plt.plot(x, x, color='grey', lw=2, ls='--')
    sns.lineplot(x, u(x), color=blue, lw=3)
    sns.lineplot(x, u(x)/1.5, color=green, lw=3)
    plt.plot([x1, x1], [0, np.log(x1)], color='black', ls='--', alpha=.7)
    plt.plot([0, x1], [np.log(x1), np.log(x1)], color='black', ls='--', alpha=.7)
    plt.scatter([x1], [np.log(x1)], color='black', zorder=15, s=70, alpha=.7)

    plt.plot([x2, x2], [0, np.log(x2)], color='black', ls='--', alpha=.7)
    plt.plot([0, x2], [np.log(x2), np.log(x2)], color='black', ls='--', alpha=.7)
    plt.scatter([x2], [np.log(x2)], color='black', zorder=15, s=70, alpha=.7)

    plt.xlim([1, 7])
    plt.ylim([0, 3])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')
    #plt.show()
    plt.savefig('bernouilli.svg')


def bernouilli_marginal_utility():
    fig = plt.figure(figsize=(4, 3))
    ax = fig.add_subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    x = np.linspace(1, 6, 50)
    print(x)
    x2 = x[(x<2.1) & (x>1.92)][0]
    x3 = x[x==3]
    print(x2)
   # plt.plot(x, x, color='grey', lw=2, ls='--')
    sns.lineplot(x, mu(x)[::-1], color=blue, lw=3)
    plt.plot([2, 2], [0, mu(x2)], color='black', ls='--', alpha=.7)
    plt.plot([0, 2], [mu(2), mu(x2)], color='black', ls='--', alpha=.7)
    plt.scatter([2], [mu(x2)], color='black', zorder=15, s=70, alpha=.7)

   # plt.plot([3, 3], [0, mu(3)], color='black', ls='--', alpha=.7)
   # plt.plot([0, 3], [mu(3), mu(3)], color='black', ls='--', alpha=.7)
   # plt.scatter([3], [mu(3)], color='black', zorder=15, s=70, alpha=.7)

    plt.xlim([1, 7])
    plt.ylim([0, max(mu(x))])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$mu(x)$')
    plt.show()


def main():
    bernouilli_expected_utility()
    bernouilli_marginal_utility()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
