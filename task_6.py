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
    else:
        print("Не вибрано жодного продукту.")


# Виклик жадібного алгоритму
greedy_algorithm(items, budget)

# динамічне програмування
# вибір продуктів з максимальною калорійністю в межах бюджету


def dynamic_programming(items, budget):
    pass


dynamic_programming(items, budget)
