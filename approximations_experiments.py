import graph
import matplotlib.pyplot as plt


def run_expected_performance(n, m, runs):
    mvc_sum = 0
    a1_sum = 0
    a2_sum = 0
    a3_sum = 0

    for _ in range(runs):
        G = graph.create_random_graph(n, m)

        mvc = graph.MVC(G)
        l = len(mvc)

        if l == 0:
            continue

        mvc_sum += l

        G1 = graph.copy_graph(G)
        G2 = graph.copy_graph(G)
        G3 = graph.copy_graph(G)

        r1 = graph.approx1(G1)
        r2 = graph.approx2(G2)
        r3 = graph.approx3(G3)

        a1_sum += len(r1)
        a2_sum += len(r2)
        a3_sum += len(r3)

    r1 = a1_sum / mvc_sum
    r2 = a2_sum / mvc_sum
    r3 = a3_sum / mvc_sum

    return r1, r2, r3, mvc_sum


def plot_three_curves(x_values, y1, y2, y3, xlabel, title):
    plt.figure()
    plt.plot(x_values, y1, marker='o', label="Approx1")
    plt.plot(x_values, y2, marker='o', label="Approx2")
    plt.plot(x_values, y3, marker='o', label="Approx3")
    plt.xlabel(xlabel)
    plt.ylabel("sum approx sizes / sum MVC sizes")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def experiment1():
    print("EXPERIMENT 1")

    n = 10
    runs = 1000

    m_values = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45]

    expected1 = []
    expected2 = []
    expected3 = []

    for m in m_values:
        r1, r2, r3, mvc_sum = run_expected_performance(n, m, runs)

        expected1.append(r1)
        expected2.append(r2)
        expected3.append(r3)

        print(f"m = {m:2d} , MVC sum = {mvc_sum:5d} , "
              f"approx1 = {r1:.3f},  approx2 = {r2:.3f} , approx3 = {r3:.3f}")

    plot_three_curves(
        m_values, expected1, expected2, expected3,
        "Number of edges (m)",
        "Approximation  vs Number of Edges"
    )   


def experiment2():
    print("EXPERIMENT 2")

    runs = 1000

    m = 20
    n_values = [i for i in range(2, 16)]
    n_values = [n for n in n_values if (n * (n - 1) // 2) >= m]

    expected1 = []
    expected2 = []
    expected3 = []

    for n in n_values:
        r1, r2, r3, mvc_sum = run_expected_performance(n, m, runs)

        expected1.append(r1)
        expected2.append(r2)
        expected3.append(r3)

        print(f"n = {n:2d} , m = {m:3d} , MVC sum = {mvc_sum:5d} , "
              f"approx1 = {r1:.3f},  approx2 = {r2:.3f} , approx3 = {r3:.3f}")

    plot_three_curves(
        n_values, expected1, expected2, expected3,
        "Number of nodes (n)",
        f"Approximation vs Number of Nodes"
    )


def experiment3():
    print("EXPERIMENT 3")

    runs = 1000
    n_values = [i for i in range(2, 16)]
    d = 0.5

    expected1 = []
    expected2 = []
    expected3 = []

    for n in n_values:
        max_edges = n * (n - 1) // 2
        m = int(d * max_edges)

        if m < 1:
            m = 1

        r1, r2, r3, mvc_sum = run_expected_performance(n, m, runs)

        expected1.append(r1)
        expected2.append(r2)
        expected3.append(r3)

        print(f"n = {n:2d} , m = {m:3d} , MVC sum = {mvc_sum:5d} , "
              f"approx1 = {r1:.3f},  approx2 = {r2:.3f} , approx3 = {r3:.3f}")

    plot_three_curves(
        n_values, expected1, expected2, expected3,
        "Number of nodes (n)",
        f"Approximation vs Number of Nodes"
    )
   

def main():
    #experiment1()
    #experiment2()
    experiment3()


if __name__ == "__main__":
    main()