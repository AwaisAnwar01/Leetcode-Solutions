import sys

def Kadane(temp):
    max_sum = -sys.maxsize - 1
    current_sum = 0
    start = 0
    local_start = 0
    finish = 0

    for i in range(len(temp)):
        current_sum += temp[i]

        if current_sum < 0:
            current_sum = 0
            local_start = i + 1

        if current_sum > max_sum:
            max_sum = current_sum
            start = local_start
            finish = i

    return max_sum, start, finish

def FindMaxSum(Matrix):
    rows = len(Matrix)
    col = len(Matrix[0]) if rows > 0 else 0

    max_sum = -sys.maxsize - 1
    max_left, max_right, max_top, max_bottom = 0, 0, 0, 0

    for left in range(col):
        temp = [0] * rows

        for right in range(left, col):
            for i in range(rows):
                temp[i] += Matrix[i][right]

            sum, start, finish = Kadane(temp)

            if sum > max_sum:
                max_sum = sum
                max_left, max_right = left, right
                max_top, max_bottom = start, finish

    print("Maximum Sum Submatrix:")
    print("Top-Left: ({}, {})".format(max_top, max_left))
    print("Bottom-Right: ({}, {})".format(max_bottom, max_right))
    print("Max Sum:", max_sum)

# Example usage
Matrix = [
    [6, -5, -7],
    [-9, 3, -6],
    [-10, 4, 7],
    [-8, 9, -3]
]

FindMaxSum(Matrix)
