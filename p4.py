#Enrollment number:92600584049
#Name:Manasvi Padaliya

CAP_A = 4
CAP_B = 3


GOAL = 2


def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()


def get_neighbours(state):
    neighbours = []

    a, b = state

    if a < CAP_A:
        neighbours.append(((CAP_A, b), "Fill jug A"))

    if b < CAP_B:
        neighbours.append(((a, CAP_B), "Fill jug B"))

    if a > 0:
        neighbours.append(((0, b), "Empty jug A"))

    if b > 0:
        neighbours.append(((a, 0), "Empty jug B"))

    amount = min(a, CAP_B - b)

    if amount > 0:
        neighbours.append(
            ((a - amount, b + amount), "Pour jug A -> jug B")
        )

    amount = min(b, CAP_A - a)

    if amount > 0:
        neighbours.append(
            ((a + amount, b - amount), "Pour jug B -> jug A")
        )

    return neighbours


def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        
        if state[0] == GOAL or state[1] == GOAL:
            return path + [(state, "Goal reached")]

        
        for neighbour, action in get_neighbours(state):

            if neighbour not in visited:
                stack.append(
                    (neighbour, path + [(neighbour, action)])
                )

    return None


start = (0, 0)


solution = dfs(start)



if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    print("Initial state:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("No solution found")
