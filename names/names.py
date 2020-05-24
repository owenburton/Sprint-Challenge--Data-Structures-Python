import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ---------- ANSWER -----------
# Runtime complexity of the original code is O(N^2), because append() is O(1), each for-loop is O(N),
# and you just multiply the runtime complexity of each loop together.

# ---------- FASTER -----------
# The runtime complexity of my solution is O(Nlog(N)), because I must iterate through every item of 
# second list, which is O(N). And at each iteration, I check if duplicate, which is O(log(N))
from binary_search_tree import BinarySearchTree

# duplicates2 = []

names_bst = BinarySearchTree(names_1[0])
for n in names_1[1:]:
    names_bst.insert(n)

for n in names_2:
    if names_bst.contains(n):
        duplicates.append(n)
        # duplicates2.append(n)

# assert set(duplicates).issubset(duplicates2)

# ---------- Stretch Goal -----------
# duplicates = set(names_1).intersection(names_2)
# runtime: 0.0039975643157958984 seconds


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
