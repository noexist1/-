import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as sps
import pandas as pd


def sample_average(x):
    #vyborochnoe srednee"""
    return np.mean(x)


def sample_variance(x, x_avg):
    #vyborochnaya dispersiya"""
    return sum((x - x_avg) ** 2) / (len(x))


def unb_sample_variance(x, x_avg):
    #nesmestchenaya vyborochnaya dispersiya"""
    return sum((x - x_avg) ** 2) / (len(x) - 1)


def minmax_ord_stats(x):
    #find min and max of order statistics"""
    x = x.sort_values()
    return x.values[0], x.values[-1]


def range_(x_min, x_max):
    #razmah"""
    return x_max - x_min


def median(x):
    #median"""
    if len(x) % 2 == 0:
        mediana = x[int((len(x) + 1) / 2)]
    else:
        mediana = (x[int(len(x) / 2)] + x[int((len(x) / 2) + 1)]) / 2
    return mediana


def empirical_cdf(x):
    #empiric func of distribution through scipy"""
    plt.title("Graph of empyric func of distribution")
    sns.ecdfplot(x)
    plt.show()


def histogram(x):
    #gistogramma otnosit chastot"""
    plt.title("Hyst of relative frequencies ")
    plt.hist(x, histtype='bar', bins=7)
    plt.show()


def kernel_density_estimation(x):
    #yadernaya ocenka
    plt.title("Nuclear estimation of the density function: ")
    plt.xlabel('Sepal length')
    sns.distplot(x, hist=True)
    plt.show()


def conf_int(x, x_avg, v):
    #doveritelnyy interval
    t = 2.6799
    interval = t * (np.sqrt(v) / np.sqrt(len(x) - 1))
    print("99% confidence interval for mat. expectations: [", x_avg - interval, ";", x_avg + interval, "]")

    epsilon = 0.01
    q1 = sps.chi2.ppf(epsilon / 2, len(x) - 1)
    q2 = sps.chi2.ppf(1 - epsilon / 2, len(x) - 1)
    int1 = (len(x) * v) / q2
    int2 = (len(x) * v) / q1
    print("99% confidence interval for variance: [", np.sqrt(int1), ";", np.sqrt(int2), "]")


def is_normal_distribution(x, x_avg, var):
    #check the distribution
    def dn():
        d_plus = 0
        for i, x_1 in enumerate(x):
            d_plus = max(d_plus, (i + 1) / len(x) - sps.norm(loc=x_avg, scale=var).cdf(x_1))

        d_minus = 0
        for i, x_1 in enumerate(x):
            d_minus = max(d_minus, sps.norm(loc=x_avg, scale=var).cdf(x_1) - i / len(x))
        print(d_minus, d_plus)
        return max(d_minus, d_plus)

    def sk():
        return (6 * len(x) * dn() + 1) / (6 * np.sqrt(len(x)))

    if sk() <= 0.9042:
        return "YES"
    else:
        return "NO"


def main():
    df = pd.read_csv("iris.data", delimiter=',')
    df = df[df['class'].isin(['Iris-setosa'])]
    sepal = df['lenght_of_sepal']

    avg = sample_average(sepal)
    print('sample_avg', avg)
    samp_var = sample_variance(sepal, avg)
    print('sample variance:', samp_var)
    unb_samp_var = unb_sample_variance(sepal, avg)
    print('unbiased sample variance:', unb_samp_var)
    min_ord_stat, max_ord_stat = minmax_ord_stats(sepal)
    print('minmax_ord_stats', min_ord_stat, max_ord_stat)
    range = range_(min_ord_stat, max_ord_stat)
    print('range:', range)
    med = median(sepal)
    print('median:', med)
    empirical_cdf(sepal)
    histogram(sepal)
    kernel_density_estimation(sepal)
    conf_int(sepal, avg, samp_var)
    print("Is the distribution normal for 0.05?", is_normal_distribution(sepal, avg, np.sqrt(samp_var)))


if __name__ == '__main__':
    main()