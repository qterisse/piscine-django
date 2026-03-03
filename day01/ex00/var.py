def my_var():
    arr = [
        42,
        "42",
        "quarante-deux",
        42.0,
        True,
        [42],
        {"42": 42},
        (42, ),
        set()
    ]

    for var in arr:
        print(f"{var} est de type {type(var)}")

if __name__ == "__main__":
    my_var()