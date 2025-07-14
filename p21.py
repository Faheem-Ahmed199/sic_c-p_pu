# Read number of nodes
N = int(input())

# Dictionaries to store child positions
tree1 = {}
tree2 = {}

# Read first tree
for _ in range(N-1):
    u, v, c = input().split()
    tree1[(int(u), c)] = int(v)

# Read second tree
for _ in range(N-1):
    u, v, c = input().split()
    tree2[(int(u), c)] = int(v)

# Check for mirror property
is_mirror = True
for (u, c) in tree1:
    if c == 'L':
        if tree1[(u, 'L')] != tree2.get((u, 'R')):
            is_mirror = False
            break
    elif c == 'R':
        if tree1[(u, 'R')] != tree2.get((u, 'L')):
            is_mirror = False
            break

# Print result
print("yes" if is_mirror else "no")
