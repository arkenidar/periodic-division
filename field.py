from div import divide_with_period


def field(n):
    for i in range(1, n):
        print(f"{i: 3}/{n} = {divide_with_period(i,n)}")


def main():
    for n in [3, 7, 11, 13, 17, 19, 23, 29]:
        print(f"Field {n}")
        field(n)


if __name__ == "__main__":
    main()
