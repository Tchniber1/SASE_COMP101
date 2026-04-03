def main() -> None:
    n = int(input().strip())
    values = input().split()

    seen = set()
    unique_order = []

    for i in range(n):
        x = int(values[i])
        if x not in seen:
            seen.add(x)
            unique_order.append(str(x))

    print(" ".join(unique_order))


