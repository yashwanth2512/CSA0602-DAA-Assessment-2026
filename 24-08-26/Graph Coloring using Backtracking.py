

def is_safe(vertex, color, graph, colors):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


def graph_coloring(graph, m):
    n = len(graph)

    colors = [0] * n

    def solve(vertex):

        if vertex == n:
            return True

        for color in range(1, m + 1):

            if is_safe(vertex, color, graph, colors):

                colors[vertex] = color

                if solve(vertex + 1):
                    return True

                colors[vertex] = 0

        return False

    if solve(0):
        print("Graph Coloring:")
        for i in range(n):
            print("Vertex", i, "-> Color", colors[i])
    else:
        print("No valid coloring exists")


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

m = 3

graph_coloring(graph, m)
