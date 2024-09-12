class Section:
    suggestion = []

def main():
    toys = Section()

    i=0

    while i < 3:
        ask = input('What are you suggesting we add to this section? ')
        i+=1
        toys.suggestion.append(ask)

    for _ in toys.suggestion:
        print(_, end=', ')

if __name__ == "__main__":
    main()