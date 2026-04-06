def minandmax(numbers):
    min = numbers[0]
    max = numbers[0]

    for num in numbers:
        if num < min:
            min = num
        elif num > max:
            max = num
    
    return [min, max]

if __name__ == "__main__":
    print(minandmax([2, 4, 1, 0, 2, -1]))
    print(minandmax([20, 50, 12, 6, 14, 8]))
    print(minandmax([100, -100]))
    