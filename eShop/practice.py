class greeting:
    say = "hi"

    to = "Chike"

    def greet(self):
        return f"{self.say}, {self.to}"

    def new(self):
        return f"{self.greet()}"

def main():

    mean = greeting()

    print(mean.new())

if __name__ == "__main__":
    main()