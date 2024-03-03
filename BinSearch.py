def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        iterations += 1

    # Знайдений елемент може бути або arr[mid], або arr[left]
    result_value = min(arr[left], arr[mid]) if left <= mid else arr[mid]

    return iterations, result_value

# Приклад використання:
sorted_array = [0.1, 0.5, 0.7, 1.2, 1.5, 2.0, 2.3, 3.0, 3.5, 4.2]
target_value = 2.1

iterations, upper_bound = binary_search(sorted_array, target_value)
print(f"Кількість ітерацій: {iterations}")
print(f"Верхня межа: {upper_bound}")
