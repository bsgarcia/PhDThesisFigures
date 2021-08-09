import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

blue = (134/255, 145/255, 191/255)
green = (161/255, 193/255, 129/255)


def u(x, i):
    return x**i


def mu(x, a):
    return np.gradient(u(x, a))


def marginal_utility():
    fig = plt.figure(figsize=(3.9, 3.75))
    ax = fig.add_subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['left'].set_bounds(-0.05, 1.35)
    # ax.spines['bottom'].set_bounds(-0.05, 1.5)
    x = np.linspace(0, 1.5, 300)
    x1 = x[len(x)//3]
    x2 = x[len(x)//3*2]
    ex1 = .18
    ex2 = .6

    dot1 = mu(x, ex1)[len(x) // 3]
    dot2 = mu(x, ex1)[len(x) // 3 * 2]

   # plt.plot(x, x, color='grey', lw=2, ls='--')
    sns.lineplot(x, mu(x, ex1), color=blue, lw=3)
    sns.lineplot(x, mu(x, ex2), color=green, lw=3)

    # import pdb; pdb.set_trace()
    plt.legend(['Water', 'Diamond'])
    # plt.plot([x1, x1], [0, dot1], color='grey', ls='--', alpha=.7)
    # plt.plot([0, x1], [dot1, dot1], color='grey', ls='--', alpha=.7)
    # plt.scatter([x1], [dot1], color='grey', zorder=15, s=70, alpha=.7)

    # plt.plot([x2, x2], [0, mu(x2, ex2)], color='grey', ls='--', alpha=.7)
    # plt.plot([0, x2], [mu(x2, ex2), mu(x2, ex2)], color='grey', ls='--', alpha=.7)
    # plt.scatter([x2], [mu(x2, ex2)], color='grey', zorder=15, s=70, alpha=.7)

    plt.xlim([-.001, max(x)])
    plt.ylim([-.001, max(mu(x, ex2))])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$mu(x)$')

    plt.title('Marginal Utility')
    # plt.show()
    plt.savefig('figs/1.svg')


def expected_utility():
    fig = plt.figure(figsize=(3.9, 3.75))
    ax = fig.add_subplot()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_bounds(-0.05, 1.35)
    ax.spines['bottom'].set_bounds(-0.05, 1.5)
    x = np.linspace(0, 1.5, 300)
    x1 = x[len(x)//3]
    x2 = x[len(x)//3*2]

    ex1 = .18
    ex2 = .6
   # plt.plot(x, x, color='grey', lw=2, ls='--')
    sns.lineplot(x, u(x, ex1), color=blue, lw=3)
    sns.lineplot(x, u(x, ex2), color=green, lw=3)

    plt.legend(['Water', 'Diamond'])
    plt.plot([x1, x1], [0, u(x1, ex1)], color='grey', ls='--', alpha=.7)
    plt.plot([0, x1], [u(x1, ex1), u(x1, ex1)], color='grey', ls='--', alpha=.7)
    plt.scatter([x1], [u(x1, ex1)], color='grey', zorder=15, s=70, alpha=1)
    plt.scatter([x1], [u(x1, ex2)], color='grey', zorder=15, s=70, alpha=1)

    plt.plot([x2, x2], [0, u(x2, ex2)], color='grey', ls='--', alpha=.7)
    plt.plot([0, x2], [u(x2, ex2), u(x2, ex2)], color='grey', ls='--', alpha=.7)
    plt.scatter([x2], [u(x2, ex2)], color='grey', zorder=15, s=70, alpha=1)

    plt.xlim([-.05, max(x)])
    plt.ylim([-.05, 1.35])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')

    # plt.show()
    plt.title('Utility')

    plt.savefig('figs/2.svg')


def main():
    expected_utility()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
