import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple


class SampleAnalyzer:
    """Класс для анализа выборки и построения графиков."""

    def __init__(self, data: List[float]):
        """Инициализация анализатора выборки."""
        self.raw_data = data
        self.n = len(data)
        self.sorted_data = sorted(data)
        self.freq_table = self._calculate_frequency_table()

    def _calculate_frequency_table(self) -> Dict[float, int]:
        """Вычисляет статистический ряд (частоты значений)."""
        freq = {}
        for num in self.sorted_data:
            freq[num] = freq.get(num, 0) + 1
        return freq

    def plot_frequency_polygon(self):
        """Строит полигон частот по значениям выборки."""
        plt.figure(figsize=(10, 5))
        plt.plot(list(self.freq_table.keys()), list(self.freq_table.values()), "bo-")
        plt.title("Полигон частот")
        plt.xlabel("Значения")
        plt.ylabel("Частота")
        plt.grid()
        plt.show()

    def calculate_extremes(self) -> Tuple[float, float]:
        """Возвращает минимальное и максимальное значения выборки."""
        return self.sorted_data[0], self.sorted_data[-1]

    def calculate_range(self) -> float:
        """Вычисляет размах выборки (разницу между max и min)."""
        return self.sorted_data[-1] - self.sorted_data[0]

    def calculate_median(self) -> float:
        """Вычисляет медиану выборки."""
        return np.median(self.sorted_data)

    def calculate_quartiles(self) -> Tuple[float, float]:
        """Вычисляет первый и третий квартили выборки."""
        q1 = np.percentile(self.sorted_data, 25)
        q3 = np.percentile(self.sorted_data, 75)
        return q1, q3

    def calculate_mean(self) -> float:
        """Вычисляет выборочное среднее значение."""
        return np.mean(self.raw_data)

    def calculate_variance(self) -> float:
        """Вычисляет выборочную дисперсию (с корректировкой на n-1)."""
        return np.var(self.raw_data, ddof=1)

    def calculate_std(self) -> float:
        """Вычисляет выборочное среднеквадратическое отклонение."""
        return np.std(self.raw_data, ddof=1)

    def calculate_initial_moment(self, order: int) -> float:
        """Вычисляет выборочный начальный момент заданного порядка."""
        return np.mean(np.power(self.raw_data, order))

    def calculate_central_moment(self, order: int) -> float:
        """Вычисляет выборочный центральный момент заданного порядка."""
        mean = self.calculate_mean()
        return np.mean([(x - mean) ** order for x in self.raw_data])

    def empirical_distribution(self, x: float) -> float:
        """Вычисляет значение эмпирической функции распределения в точке x."""
        count = sum(1 for num in self.sorted_data if num <= x)
        return count / self.n

    def plot_empirical_distribution(self):
        """Строит график эмпирической функции распределения."""
        x = sorted(list(set(self.sorted_data)))
        y = [self.empirical_distribution(val) for val in x]

        plt.figure(figsize=(10, 5))
        plt.step(x, y, where="post")
        plt.title("Эмпирическая функция распределения")
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.grid()
        plt.show()
