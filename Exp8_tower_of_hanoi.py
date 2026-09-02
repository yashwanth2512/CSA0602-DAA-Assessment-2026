"""
Experiment 8: Tower of Hanoi
Objective: Analyze exponential recursion.
Complexity: O(2^n)
"""

import time


def tower_of_hanoi(n, source, auxiliary, destination, moves):
    if n == 1:
        moves.append(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary, moves)
    moves.append(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination, moves)


if __name__ == "__main__":
    n = 3
    moves = []

    start = time.perf_counter()
    tower_of_hanoi(n, 'A', 'B', 'C', moves)
    end = time.perf_counter()

    print(f"Tower of Hanoi solution for n = {n} disks:")
    for i, move in enumerate(moves, start=1):
        print(f"{i}. {move}")

    print(f"\nTotal moves: {len(moves)}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Time Complexity: O(2^n) -> each call spawns two recursive calls, "
          "and the number of moves is 2^n - 1")
    print("Space Complexity: O(n) -> recursion stack depth")
    print("Explanation: The number of moves grows exponentially with the "
          "number of disks.")
