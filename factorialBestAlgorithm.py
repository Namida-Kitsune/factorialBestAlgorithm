def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
if __name__ == "__main__":
    try:
        n = int(input("Input : "))
        print("Answer",factorial(n))
    except:
        print("Do not enter numbers over 1558.")
