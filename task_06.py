from __future__ import annotations
from typing import Dict, List, Tuple


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """Selects items greedily by highest calories-to-cost ratio without exceeding the budget"""
    ranked = sorted(
        items.items(),
        key=lambda kv: kv[1]["calories"] / kv[1]["cost"],
        reverse=True,
    )

    chosen = []
    total_cost = 0
    total_calories = 0

    for name, data in ranked:
        cost = data["cost"]
        calories = data["calories"]
        if total_cost + cost <= budget:
            chosen.append(name)
            total_cost += cost
            total_calories += calories

    return chosen, total_cost, total_calories


def dynamic_programming(items, budget):
    """Finds the optimal set of items maximizing calories within the given budget."""
    names = list(items.keys())
    costs = [items[n]["cost"] for n in names]
    calories = [items[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        c = costs[i - 1]
        cal = calories[i - 1]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if c <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - c] + cal)

    chosen = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen.append(names[i - 1])
            b -= costs[i - 1]
    chosen.reverse()

    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in chosen)

    return chosen, total_cost, total_calories


if __name__ == "__main__":
    budget = 200

    greedy_items, greedy_cost, greedy_cals = greedy_algorithm(items, budget)
    print("Greedy:")
    print("  items:", greedy_items)
    print("  cost:", greedy_cost)
    print("  calories:", greedy_cals)

    dp_items, dp_cost, dp_cals = dynamic_programming(items, budget)
    print("\nDynamic programming:")
    print("  items:", dp_items)
    print("  cost:", dp_cost)
    print("  calories:", dp_cals)
