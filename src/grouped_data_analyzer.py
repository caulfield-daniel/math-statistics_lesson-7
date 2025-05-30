from typing import List
import matplotlib.pyplot as plt


class GroupedDataAnalyzer:
    """
    Класс для анализа группированных данных.
    Позволяет построить гистограмму и оценить среднее и дисперсию
    генеральной совокупности на основе сгруппированных данных.
    """

    def __init__(self, data: List[float], num_bins: int = 5):
        """
        Инициализирует анализатор группированных данных.

        :param data: Список числовых значений (не сгруппированных).
        :param num_bins: Количество интервалов (по умолчанию 5).
        """
        self.raw_data = data
        self.n = len(data)
        self.num_bins = num_bins
        self.bins, self.freq = self._group_data()

    def _group_data(self):
        """
        Формирует интервалы (бины) и подсчитывает частоты по ним.

        :return: Кортеж из списка интервалов и частот.
        """
        min_val = min(self.raw_data)
        max_val = max(self.raw_data)
        bin_width = (max_val - min_val) / self.num_bins

        bins = []
        freq = []

        current = min_val
        for _ in range(self.num_bins):
            next_val = current + bin_width
            bins.append((current, next_val))
            count = sum(1 for x in self.raw_data if current <= x < next_val)
            freq.append(count)
            current = next_val

        return bins, freq

    def plot_histogram(self):
        """
        Строит гистограмму на основе исходных данных.
        """
        plt.figure(figsize=(10, 5))
        plt.hist(self.raw_data, bins=self.num_bins, edgecolor="black")
        plt.title("Гистограмма")
        plt.xlabel("Емкость, пкФ")
        plt.ylabel("Частота")
        plt.grid()
        plt.show()

    def estimate_grouped_mean(self) -> float:
        """
        Оценивает среднее значение на основе группированных данных.

        :return: Оценка среднего.
        """
        midpoints = [(b[0] + b[1]) / 2 for b in self.bins]
        return sum(m * f for m, f in zip(midpoints, self.freq)) / self.n

    def estimate_grouped_variance(self) -> float:
        """
        Оценивает дисперсию на основе группированных данных.

        :return: Оценка дисперсии.
        """
        midpoints = [(b[0] + b[1]) / 2 for b in self.bins]
        mean = self.estimate_grouped_mean()
        return sum(f * (m - mean) ** 2 for m, f in zip(midpoints, self.freq)) / (
            self.n - 1
        )