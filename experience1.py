import matplotlib.pyplot as plt
from graph import create_random_graph, has_cycle, is_connected


# =========================
# Experiment 1
# =========================
def experiment_cycle():
    n = 50
    runs = 200
    edge_values = list(range(0, 200, 10))
    probabilities = []

    for m in edge_values:
        cycle_count = 0

        for _ in range(runs):
            G = create_random_graph(n, m)
            if has_cycle(G):
                cycle_count += 1

        probabilities.append(cycle_count / runs)

    plt.plot(edge_values, probabilities, label="Cycle probability")
    plt.xlabel("Number of edges (m)")
    plt.ylabel("Probability of cycle")
    plt.title("Cycle Probability vs Number of Edges")
    plt.legend()
    plt.grid(True)
    plt.show()



# =========================
# Main
# =========================
if __name__ == "__main__":
    experiment_cycle()

