items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# жадібний алгоритм
# вибір продуктів з максимальною калорійністю на одиницю вартості


def greedy_algorithm(items, budget):
    items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    result = {}

    for item, data in items:
        if budget >= data["cost"]:
            result[item] = data
            budget -= data["cost"]

    if result:
        print("\nВибрані продукти:")
        for item, data in result.items():
            print(
                f"{item}: Вартість: {data['cost']}, Калорії: {data['calories']}")
        total_calories = sum(d["calories"] for d in result.values())
        print(f"Сума калорій: {total_calories}")
    else:
        print("Не вибрано жодного продукту.")


# Виклик жадібного алгоритму
print("Жадібний алгоритм:")
greedy_algorithm(items, budget)
print("____________________________________________")

# динамічне програмування
# вибір продуктів з максимальною калорійністю в межах бюджету


def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, data = list(items.items())[i - 1]
        for w in range(budget + 1):
            if data["cost"] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - data["cost"]] + data["calories"])
            else:
                dp[i][w] = dp[i - 1][w]

    result = {}
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item, data = list(items.items())[i - 1]
            result[item] = data
            w -= data["cost"]

    if result:
        print("\nВибрані продукти:")
        for item, data in result.items():
            print(
                f"{item}: Вартість: {data['cost']}, Калорії: {data['calories']}")
        total_calories = sum(d["calories"] for d in result.values())
        print(f"Сума калорій: {total_calories}")
    else:
        print("Не вибрано жодного продукту.")


# Виклик динамічного програмування
print("\nДинамічне програмування:")
dynamic_programming(items, budget)
