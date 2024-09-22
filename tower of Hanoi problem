class TowerOfHanoi:
    def __init__(self, n):
        self.n = n  # Initialize the number of disks

    def solve(self):
        # Start solving by moving n disks from source 'A' to destination 'C' using auxiliary 'B'
        self._move_disks(self.n, 'A', 'B', 'C')

    def _move_disks(self, n, source, auxiliary, destination):
        if n == 1:
            # Base case: only one disk to move
            self._print_move(1, source, destination)
            return
        # Move n-1 disks from source to auxiliary, so they are out of the way
        self._move_disks(n - 1, source, destination, auxiliary)
        # Move the nth disk from source to destination
        self._print_move(n, source, destination)
        # Move the n-1 disks from auxiliary to destination
        self._move_disks(n - 1, auxiliary, source, destination)

    def _print_move(self, disk, source, destination):
        # Print the move
        print(f"Move disk {disk} from {source} to {destination}")


# Example usage
if __name__ == "__main__":
    n = 3  # Number of disks
    hanoi = TowerOfHanoi(n)
    hanoi.solve()
