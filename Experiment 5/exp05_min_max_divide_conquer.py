import random

comparison_count = 0


def min_max_dc(arr, low, high):
    global comparison_count

    # Base case: only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: two elements
    if high == low + 1:
        comparison_count += 1

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide
    mid = (low + high) // 2

    left_min, left_max = min_max_dc(arr, low, mid)
    right_min, right_max = min_max_dc(arr, mid + 1, high)

    # Conquer
    comparison_count += 1
    overall_min = left_min if left_min < right_min else right_min

    comparison_count += 1
    overall_max = left_max if left_max > right_max else right_max

    return overall_min, overall_max


def min_max_naive(arr):
    minimum = maximum = arr[0]
    comparisons = 0

    for num in arr[1:]:
        comparisons += 1
        if num < minimum:
            minimum = num

        comparisons += 1
        if num > maximum:
            maximum = num

    return minimum, maximum, comparisons


def performance_analysis():
    print("\nPerformance Analysis")
    print("-" * 55)
    print(f"{'Size':>8} {'DC Comp':>12} {'Naive Comp':>15} {'Formula':>12}")

    for size in [10, 100, 1000, 10000]:
        arr = [random.randint(1, 10000) for _ in range(size)]

        global comparison_count
        comparison_count = 0

        min_max_dc(arr, 0, len(arr) - 1)
        dc = comparison_count

        _, _, naive = min_max_naive(arr)

        formula = 3 * size // 2 - 2

        print(f"{size:>8} {dc:>12} {naive:>15} {formula:>12}")


def main():
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    global comparison_count
    comparison_count = 0

    minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)
    dc_comp = comparison_count

    _, _, naive_comp = min_max_naive(arr)

    print("Array :", arr)
    print("Minimum :", minimum)
    print("Maximum :", maximum)
    print("Divide & Conquer Comparisons :", dc_comp)
    print("Naive Comparisons :", naive_comp)

    performance_analysis()


if __name__ == "__main__":
    main()
