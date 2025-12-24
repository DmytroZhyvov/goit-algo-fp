import random
from collections import Counter

import matplotlib.pyplot as plt


ANALYTIC_PROB = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}


def simulate_two_dice(n_rolls: int = 1000000, seed: int = 42):
    """Simulates rolling two dice n_rolls times"""
    random.seed(seed)

    counts = Counter()
    for _ in range(n_rolls):
        s = random.randint(1, 6) + random.randint(1, 6)
        counts[s] += 1

    probs = {s: counts[s] / n_rolls for s in range(2, 13)}
    return counts, probs


def print_comparison_table(n_rolls, counts, mc_probs):
    print(f"Rolls: {n_rolls}\n")
    header = f"{'Sum':>3} | {'Count':>10} | {'MC prob':>10} | {'Analytic':>10} | {'Abs diff':>10}"
    print(header)
    print("-" * len(header))

    for s in range(2, 13):
        mc = mc_probs[s]
        an = ANALYTIC_PROB[s]
        diff = abs(mc - an)
        print(f"{s:>3} | {counts[s]:>10} | {mc:>10.6f} | {an:>10.6f} | {diff:>10.6f}")


def plot_probabilities(mc_probs):
    sums = list(range(2, 13))
    mc = [mc_probs[s] for s in sums]
    an = [ANALYTIC_PROB[s] for s in sums]

    x = range(len(sums))
    width = 0.4

    plt.figure(figsize=(10, 5))
    plt.bar([i - width / 2 for i in x], mc, width=width, label="Monte Carlo")
    plt.bar([i + width / 2 for i in x], an, width=width, label="Analytic")
    plt.xticks(list(x), sums)
    plt.xlabel("Sum of two dice")
    plt.ylabel("Probability")
    plt.title("Two Dice Sum Probabilities: Monte Carlo vs Analytic")
    plt.grid(True, axis="y")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    N = 500000
    counts, mc_probs = simulate_two_dice(n_rolls=N, seed=42)

    print_comparison_table(N, counts, mc_probs)
    plot_probabilities(mc_probs)
