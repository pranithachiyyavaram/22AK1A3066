def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def print_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    print(primes)
def main():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))   
        if start > end:
            print("Invalid range. The start must be less than or equal to the end.")
            return  
        print(f"Prime numbers in the range [{start}, {end}]:")
        print_primes_in_range(start, end)   
    except ValueError:
        print("Invalid input. Please enter integers.")
if __name__ == "__main__":
    main()
