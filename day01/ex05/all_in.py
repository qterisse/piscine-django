import sys

def main(args: str):
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

    def get_city(state: str):
        states_low = {k.lower(): v for k, v in states.items()}
        return capital_cities[states_low[state]]

    def get_state(city: str):
        states_inv = {v: k for k, v in states.items()}
        capital_inv = {v.lower(): k for k, v in capital_cities.items()}
        return states_inv[capital_inv[city]]

    for arg in args.split(","):
        arg = arg.strip()
        if (arg == ""):
            continue

        if arg.lower() in [c.lower() for c in capital_cities.values()]:
            state = get_state(arg.lower()).capitalize()
            city = get_city(state.lower())
        elif arg.lower() in [s.lower() for s in states]:
            city = get_city(arg.lower()).capitalize()
            state = get_state(city.lower())
        else:
            print(f"{arg} is neither a capital city nor a state")
            continue

        print(f"{city} is the capital of {state}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit()
    main(sys.argv[1])