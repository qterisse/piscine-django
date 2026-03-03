import sys

def main(capital: str):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    states_inv = {v: k for k, v in states.items()}

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    capital_inv = {v: k for k, v in capital_cities.items()}


    if not capital in capital_cities.values():
        print("Unknown capital city")
        return

    print(states_inv[capital_inv[capital]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    main(sys.argv[1])