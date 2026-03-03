class Intern:
    DEFAULT_NAME = "My name? I'm nobody, an intern, I have no name."

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name=DEFAULT_NAME):
        self.Name = name
    
    def __str__(self):
        return self.Name
    
    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return self.Coffee()


if __name__ == "__main__":
    bob = Intern()
    mark = Intern("Mark")

    print(bob)
    print(mark)
    print(mark.make_coffee())

    try:
        bob.work()
    except Exception as e:
        print(e)

