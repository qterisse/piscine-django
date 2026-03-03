def main():
    with open("./numbers.txt") as f:
        print(f.read().replace(",", "\n"), end="")

if __name__ == "__main__":
    main()