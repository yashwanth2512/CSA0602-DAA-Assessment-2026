
def is_safe(v, graph, path, pos):
   
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True


def hamiltonian_cycle(graph):
    n = len(graph)

    path = [-1] * n

    path[0] = 0

    def solve(pos):
        if pos == n:
            return graph[path[pos - 1]][path[0]] == 1

        for v in range(1, n):
            if is_safe(v, graph, path, pos):
                path[pos] = v

                if solve(pos + 1):
                    return True

                path[pos] = -1

        return False

    if solve(1):
        print("Hamiltonian Cycle:")
        print(" -> ".join(map(str, path + [path[0]])))
    else:
        print("No Hamiltonian Cycle exists")



graph = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0]
]

hamiltonian_cycle(graph)
