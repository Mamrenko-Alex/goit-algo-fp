import random
import matplotlib.pyplot as plt
from collections import defaultdict


def monte_carlo_simulation(dice_count=2, repeats=500):
    result_counter = defaultdict(int)

    for _ in range(repeats):
        roll_sum = sum(random.randint(1, 6) for _ in range(dice_count))
        result_counter[roll_sum] += 1

    probabilities = {}
    for total in range(dice_count, dice_count * 6 + 1):
        count = result_counter[total]
        probability = count / repeats
        probabilities[total] = probability

    return probabilities


def analytical_probabilities(dice_count=2):
    from functools import lru_cache

    total_possibilities = 6 ** dice_count

    @lru_cache(maxsize=None)
    def count_ways(dice_left, current_sum):
        if dice_left == 0:
            return 1 if current_sum == 0 else 0
        ways = 0
        for i in range(1, 7):
            if current_sum - i >= 0:
                ways += count_ways(dice_left - 1, current_sum - i)
        return ways

    probabilities = {}
    for total in range(dice_count, dice_count * 6 + 1):
        ways = count_ways(dice_count, total)
        probabilities[total] = ways / total_possibilities

    return probabilities


def display_results(mc_probs, analytical_probs):
    print("Сума\tMC %\tАналіт. %")
    for total in sorted(analytical_probs.keys()):
        mc = mc_probs.get(total, 0) * 100
        ana = analytical_probs[total] * 100
        print(f"{total}\t{mc:.2f}%\t{ana:.2f}%")


def plot_probabilities(mc_probs, analytical_probs):
    totals = sorted(analytical_probs.keys())
    mc_values = [mc_probs.get(total, 0) for total in totals]
    analytical_values = [analytical_probs[total] for total in totals]

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(totals, mc_values, label="Монте-Карло", marker='o')
    ax.plot(totals, analytical_values, label="Аналітична", marker='x')
    ax.set_title("Ймовірності сум при киданні 2 кубиків")
    ax.set_xlabel("Сума")
    ax.set_ylabel("Ймовірність")
    ax.legend()
    ax.grid(True)

    cell_text = []
    for total in totals:
        mc_percent = f"{mc_probs.get(total, 0)*100:.2f}%"
        ana_percent = f"{analytical_probs[total]*100:.2f}%"
        cell_text.append([total, mc_percent, ana_percent])

    table = plt.table(
        cellText=cell_text,
        colLabels=["Сума", "Монте-Карло", "Аналітична"],
        cellLoc='center',
        loc='bottom',
        bbox=[0, -1.2, 0.5, 1],
    )

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.2)
    table.auto_set_column_width([0, 1, 2])

    plt.subplots_adjust(left=0.15, bottom=0.45)

    plt.show()


if __name__ == "__main__":
    DICE_COUNT = 2
    REPEATS = 5

    mc_probs = monte_carlo_simulation(DICE_COUNT, REPEATS)
    analytical_probs = analytical_probabilities(DICE_COUNT)

    display_results(mc_probs, analytical_probs)
    plot_probabilities(mc_probs, analytical_probs)
