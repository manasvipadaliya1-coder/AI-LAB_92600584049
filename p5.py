#tower of hanoi

def tower_of_hanoi(n, source, helper, destination):

    if n==1:
        print("move disk 1 from", source , "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print("move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, helper, source, destination)

#number of disks
n = int(input("enter number of disks:"))

#solve tower of hanoi
tower_of_hanoi(n, "A", "B", "C")

#total number of moves
print("total moves:", (2**n) -1)
