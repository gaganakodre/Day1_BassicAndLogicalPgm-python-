def even_odd(a_, b_):

    for n in range(a_, b_):
        if n % 2 == 0:
            print(n, "is a even number")
            continue  # continues with the next iteration of the loop:
    print(n, "is a odd number")


if __name__ == '__main__':
    a = int(input("enter the range"))
    b = int(input("enter the range2"))
    even_odd(a, b)
