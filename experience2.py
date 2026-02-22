import matplotlib.pyplot as plt
from graph import create_random_graph, has_cycle, is_connected

# =========================
# Experiment 2
# =========================
def experiment_connected():
    n = 50
    runs = 500
    edge_values = list(range(25, 250, 5))
    probabilities = []

    for m in edge_values:
        connected_count = 0

        for _ in range(runs):
            G = create_random_graph(n, m)
            if is_connected(G):
                connected_count += 1

        probabilities.append(connected_count / runs)

    plt.plot(edge_values, probabilities, label="Connected probability")
    plt.xlabel("Number of edges (m)")
    plt.ylabel("Probability of connected")
    plt.title("Connected Probability vs Number of Edges")
    plt.legend()
    plt.grid(True)
    plt.show()


# =========================
# Main
# =========================
if __name__ == "__main__":
    experiment_connected()