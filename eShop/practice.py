
Choice = {
    1: 'first floor',
    2: 'second floor',
    3: 'third floor',
}

def value(x):
    level = int(input('Enter a level: '))
    fv = False
    for k, v in x.items():
        if level != k:
            pass
        else:
            fv = v
            break
    if fv:
        return fv
    else:
        return 'invalid floor level'
        
def main():
    print(value(Choice))
if __name__ == '__main__':
    main()