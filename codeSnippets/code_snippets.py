# constant time
def func1(array1):
    return array1[0]


# linear time
def func2(array1):
    for element in array1:
        print(element)


# nlogn
def func3(array1):
    return sorted(array1)


# quadratic
def func4(array1):
    for element1 in array1:
        for element2 in array1:
            print(f"{element1} and {element2}")


# exponential
def calculate_binary_tree_nodes(level_depth):
    """
    Recursively calculates nodes in a perfect binary tree of a given depth.
    Time Complexity: O(2^n)
    """
    # Base case: we have reached the bottom level
    if level_depth <= 0:
        return 1

    # Recursive case: branch out into two more paths
    left_branch_nodes = calculate_binary_tree_nodes(level_depth - 1)
    right_branch_nodes = calculate_binary_tree_nodes(level_depth - 1)

    total_nodes = left_branch_nodes + right_branch_nodes
    return total_nodes
