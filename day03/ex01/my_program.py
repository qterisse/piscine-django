import path

if __name__ == "__main__":
    print("\n-- MY PROGRAM --\n")

    if (not path.os.path.exists("./hello")):
        path.os.mkdir("hello")

    with open("./hello/world", "w") as f:
        f.write("Hello, world!")
    
    print("File successfully created")

    with open("./hello/world") as f:
        print("File content: " + f.read())
