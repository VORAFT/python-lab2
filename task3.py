def check_fibonacci_in_set():
    numbers_set = set(range(1, 51))
    
    fib_list = []
    a, b = 1, 1
    while a <= 50:
        fib_list.append(a)
        a, b = b, a + b
    
    fib_set = set(fib_list)
    
    result_set = numbers_set.intersection(fib_set)
    
    print("Початкова множина (від 1 до 50):")
    print(numbers_set)
    print("\nМножина чисел Фібоначчі, що входять у діапазон:")
    print(result_set)
    print(f"\nКількість чисел Фібоначчі: {len(result_set)}")

check_fibonacci_in_set()