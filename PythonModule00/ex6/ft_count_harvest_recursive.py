def ft_count_harvest_recursive() -> None:
    def recursive(days: int) -> None:
        if days > 1:
            recursive(days - 1)
        print(f"Day {days}")

    print(">>> ft_count_harvest_recursive()")
    days = int(input("Days until harvest: "))
    recursive(days)
    print("Harvest time!")
