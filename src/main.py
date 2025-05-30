from sample_analyzer import SampleAnalyzer
from grouped_data_analyzer import GroupedDataAnalyzer


def read_data_from_file(filename):
    """
    Читает числовые данные из текстового файла. Автоматически определяет разделитель: запятая или перенос строки.

    :param filename: Путь к файлу с данными.
    :return: Список чисел.
    """
    with open(filename, "r") as file:
        content = file.read()
    if "," in content:
        return [float(x.strip()) for x in content.strip().split(",") if x.strip()]
    else:
        return [float(x.strip()) for x in content.strip().splitlines() if x.strip()]


def solve_task_1_sample_analysis(data):
    print("\n" + "=" * 60)
    print("ЗАДАЧА 1: АНАЛИЗ ВЫБОРКИ".center(60))
    print("=" * 60)
    analyzer = SampleAnalyzer(data)

    print(f"\nВариационный ряд:\n{analyzer.sorted_data}\n")
    print(f"Статистический ряд:")
    for value, freq in analyzer.freq_table.items():
        print(f"  Значение: {value:.2f} \t Частота: {freq}")

    print("\nХарактеристики выборки:")
    print(f"  Минимум: {analyzer.calculate_extremes()[0]:.2f}")
    print(f"  Максимум: {analyzer.calculate_extremes()[1]:.2f}")
    print(f"  Размах: {analyzer.calculate_range():.2f}")
    print(f"  Медиана: {analyzer.calculate_median():.2f}")
    q1, q3 = analyzer.calculate_quartiles()
    print(f"  Квартиль 1 (Q1): {q1:.2f}")
    print(f"  Квартиль 3 (Q3): {q3:.2f}")
    print(f"  Среднее: {analyzer.calculate_mean():.2f}")
    print(
        f"  Начальный момент 2-го порядка: {analyzer.calculate_initial_moment(2):.2f}"
    )
    print(
        f"  Центральный момент 2-го порядка: {analyzer.calculate_central_moment(2):.2f}"
    )
    print(f"  Дисперсия: {analyzer.calculate_variance():.2f}")
    print(f"  Среднеквадратическое отклонение: {analyzer.calculate_std():.2f}")

    analyzer.plot_frequency_polygon()
    analyzer.plot_empirical_distribution()


def solve_task_2_grouped_analysis(data):
    print("\n" + "=" * 60)
    print("ЗАДАЧА 2: ГРУППИРОВАННЫЙ СТАТИСТИЧЕСКИЙ АНАЛИЗ".center(60))
    print("=" * 60)
    grouped_analyzer = GroupedDataAnalyzer(data)

    print("\nГруппированный ряд (интервалы и частоты):")
    for i, (bin_range, freq) in enumerate(
        zip(grouped_analyzer.bins, grouped_analyzer.freq), start=1
    ):
        print(
            f"  Интервал {i}: {bin_range[0]:.2f} - {bin_range[1]:.2f}  |  Частота: {freq}"
        )

    print("\nХарактеристики по группированным данным:")
    print(f"  Оценка среднего: {grouped_analyzer.estimate_grouped_mean():.2f}")
    print(f"  Оценка дисперсии: {grouped_analyzer.estimate_grouped_variance():.2f}")

    grouped_analyzer.plot_histogram()


def main():
    filepath = "data.txt"
    data = read_data_from_file(filepath)

    solve_task_1_sample_analysis(data)
    solve_task_2_grouped_analysis(data)


if __name__ == "__main__":
    main()
