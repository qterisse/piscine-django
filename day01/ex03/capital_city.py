import sys

def main(state: str):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if not state in states:
        print("Unknown state")
        return

    print(capital_cities[states[state]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    main(sys.argv[1])