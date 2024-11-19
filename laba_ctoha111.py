import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import kstest, expon, norm, gumbel_r, probplot
from scipy.stats import chisquare
from scipy.stats import chisquare
import sns as sns

# Фіксуємо генератор випадкових чисел для повторюваності
np.random.seed(33)

# Генерація вибірок
rand_exp = np.random.exponential(scale=1, size=10000)  # Експоненційний розподіл
rand_norm = np.random.normal(loc=0, scale=2, size=10000)  # Нормальний розподіл
rand_extreme = 1 - gumbel_r.rvs(loc=0, scale=1, size=10000)  # Розподіл екстремальних значень

# Генерація вибірок
samples = {
    "exp": np.random.exponential(scale=1, size=10000),   # Експоненційний розподіл
    "norm": np.random.normal(loc=0, scale=2, size=10000),  # Нормальний розподіл
    "extreme": 1 - gumbel_r.rvs(loc=0, scale=1, size=10000)  # Розподіл екстремальних значень
}

# Теоретичні розподіли та їх параметри
distributions = {
    "exp": ("expon", (0, 1)),  # Параметри експоненційного розподілу
    "norm": ("norm", (0, 2)),  # Параметри нормального розподілу
    "extreme": ("gumbel_r", (0, 1))  # Параметри розподілу Гумбеля
}

# Функція для виконання KS-тесту
def perform_ks_test(sample, dist_name, dist_params):
    result = kstest(sample, dist_name, args=dist_params)
    return {"statistic": result.statistic, "p_value": result.pvalue}

# Проведення тестів
results = {}
for key, sample in samples.items():
    dist_name, dist_params = distributions[key]
    # Для вибірки extreme перетворюємо назад у вигляд розподілу Гумбеля
    if key == "extreme":
        sample = -sample + 1
    results[key] = perform_ks_test(sample, dist_name, dist_params)

# Виведення результатів
print("Результати тесту Колмогорова-Смирнова:")
for key, result in results.items():
    print(f"\n{key.capitalize()} розподіл:")
    print(f"Statistic: {result['statistic']:.4f}, p-value: {result['p_value']:.4f}")

from scipy.stats import cramervonmises

# Функція для виконання тесту Крамера-Мізеса
def perform_cvm_test(sample, dist_name, dist_params):
    result = cramervonmises(sample, dist_name, args=dist_params)
    return {"statistic": result.statistic, "p_value": result.pvalue}

# Проведення тестів для кожної вибірки
cvm_results = {}
for key, sample in samples.items():
    dist_name, dist_params = distributions[key]
    # Для вибірки extreme перетворюємо назад у вигляд розподілу Гумбеля
    if key == "extreme":
        sample = -sample + 1
    cvm_results[key] = perform_cvm_test(sample, dist_name, dist_params)

# Виведення результатів
print("\nРезультати критерію Крамера-Мізеса (ω²):")
for key, result in cvm_results.items():
    print(f"\n{key.capitalize()} розподіл:")
    print(f"Statistic: {result['statistic']:.4f}, p-value: {result['p_value']:.4f}")

print("==============")

# Функція для виконання χ² тесту
def perform_chi2_test(data, dist, params, bins=100):
    # Створення гістограми для вибірки
    observed, edges = np.histogram(data, bins=bins)

    # Розрахунок теоретичних частот
    cdf_values = dist.cdf(edges, *params)
    expected = len(data) * np.diff(cdf_values)

    # Узгодження очікуваних частот із сумою спостережуваних
    expected *= observed.sum() / expected.sum()

    # Проведення χ² тесту
    chi2_stat, p_value = chisquare(f_obs=observed, f_exp=expected)
    return {"statistic": chi2_stat, "p_value": p_value}


# Проведення тестів для кожної вибірки
chi2_results = {}
for key, sample in samples.items():
    dist_name, dist_params = distributions[key]
    # Для extreme розподілу застосовуємо відповідне перетворення
    if key == "extreme":
        sample = -sample + 1
    chi2_results[key] = perform_chi2_test(sample, globals()[dist_name], dist_params)

# Виведення результатів
print("\nРезультати χ² тесту:")
for key, result in chi2_results.items():
    print(f"\n{key.capitalize()} розподіл:")
    print(f"Statistic: {result['statistic']:.4f}, p-value: {result['p_value']:.4f}")

print("==============")


# Функція для виконання χ² тесту
def perform_chi2_test(data, dist, params, bins=100):
    # Створення гістограми для вибірки
    observed, edges = np.histogram(data, bins=bins)

    # Розрахунок теоретичних частот
    cdf_values = dist.cdf(edges, *params)
    expected = len(data) * np.diff(cdf_values)

    # Узгодження очікуваних частот із сумою спостережуваних
    expected *= observed.sum() / expected.sum()

    # Проведення χ² тесту
    chi2_stat, p_value = chisquare(f_obs=observed, f_exp=expected)
    return {"statistic": chi2_stat, "p_value": p_value}


# Проведення тестів для кожної вибірки
chi2_results = {}
for key, sample in samples.items():
    dist_name, dist_params = distributions[key]
    # Для extreme розподілу застосовуємо відповідне перетворення
    if key == "extreme":
        sample = -sample + 1
    chi2_results[key] = perform_chi2_test(sample, globals()[dist_name], dist_params)

# Виведення результатів
print("\nРезультати χ² тесту:")
for key, result in chi2_results.items():
    print(f"\n{key.capitalize()} розподіл:")
    print(f"Statistic: {result['statistic']:.4f}, p-value: {result['p_value']:.4f}")

sns.set(style="whitegrid")

# Гістограми
plt.figure(figsize=(15, 5))

# Експоненціальний розподіл
plt.subplot(1, 3, 1)
sns.histplot(rand_exp, kde=True, stat='density', color='blue', bins=20)
plt.title('Histogram of Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

# Нормальний розподіл
plt.subplot(1, 3, 2)
sns.histplot(rand_norm, kde=True, stat='density', color='green', bins=30)
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

# Розподіл екстремальних значень
plt.subplot(1, 3, 3)
sns.histplot(-rand_extreme+1, kde=True, stat='density', color='red', bins=30)
plt.title('Histogram of Extreme Value Distribution')
plt.xlabel('Value')
plt.ylabel('Density')

plt.tight_layout()
plt.show()

# Probability Plot для кожної вибірки

# Експоненціальний розподіл
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
probplot(rand_exp, dist="expon", plot=plt)
plt.title('Probability Plot of Exponential Distribution')

# Нормальний розподіл
plt.subplot(1, 3, 2)
probplot(rand_norm, dist="norm", plot=plt)
plt.title('Probability Plot of Normal Distribution')

# Розподіл екстремальних значень
plt.subplot(1, 3, 3)
probplot(-rand_extreme+1, dist="gumbel_r", sparams=(0,1), plot=plt)
plt.title('Probability Plot of Extreme Value Distribution')

plt.tight_layout()
plt.show()