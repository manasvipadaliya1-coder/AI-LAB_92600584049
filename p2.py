# capacities of the two jugs
CAP_A = 4
CAP_B = 3

# goal amount
GOAL = 2


# function to print the state
def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()


# generate all possible moves
def get_neighbours(state):
    neighbours = []

    a, b = state

    # 1. Fill jug A
    if a < CAP_A:
        neighbours.append(((CAP_A, b), "Fill jug A"))

    # 2. Fill jug B
    if b < CAP_B:
        neighbours.append(((a, CAP_B), "Fill jug B"))

    # 3. Empty jug A
    if a > 0:
        neighbours.append(((0, b), "Empty jug A"))

    # 4. Empty jug B
    if b > 0:
        neighbours.append(((a, 0), "Empty jug B"))

    # 5. Pour jug A -> jug B
    amount = min(a, CAP_B - b)

    if amount > 0:
        neighbours.append(
            ((a - amount, b + amount), "Pour jug A -> jug B")
        )

    # 6. Pour jug B -> jug A
    amount = min(b, CAP_A - a)

    if amount > 0:
        neighbours.append(
            ((a + amount, b - amount), "Pour jug B -> jug A")
        )

    return neighbours


# BFS algorithm
def bfs(start):
    queue = [(start, [])]
    visited = set()

    while queue:
        state, path = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        # check goal
        if state[0] == GOAL or state[1] == GOAL:
            return path + [(state, "Goal reached")]

        # generate neighbours
        for neighbour, action in get_neighbours(state):

            if neighbour not in visited:
                queue.append(
                    (neighbour, path + [(neighbour, action)])
                )

    return None


# starting state
start = (0, 0)

# run BFS
solution = bfs(start)


# print solution
if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    print("Initial state:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("No solution found")
