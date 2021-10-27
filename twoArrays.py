# Program to take two arrays of the same length, and return all pairs of numbers (one from each array)
# where their sum is closest to a target number.

a1 = [7, 4, 1, 10]
a2 = [4, 5, 8, 7]
target = 13


def compute(a1, a2, target):
    a1.sort()
    a2.sort()
    pairs = [(a1[0], a2[0])]
    smallest_residual = abs(a1[0] + a2[0] - target)

    i = 0
    j = len(a1) - 1

    while i < len(a1) and j >= 0:

        residual = a1[i] + a2[j] - target

        if abs(residual) < smallest_residual:
            smallest_residual = abs(residual)
            pairs = [(a1[i], a2[j])]

        elif abs(residual) == smallest_residual:
            pairs.append((a1[i], a2[j]))

        if residual < 0:
            i += 1
        else:
            j -= 1

    return pairs
