from sys import stdin


def main():
    read = stdin.readline
    t = read().strip()

    if not (t.isdigit()):
        print("Invalid Test not digit")
    elif int(t) > 10 or int(t) < 1:
        print("Invalid Test")
    else:
        t= int(t)
        for _ in range(t):
            data = read().strip()
            print(data)
            if len(data)>100 or len(data)<1:
                print("Invalid Input")
            else:
                cap = 0
                small = 0
                for x in data:
                    if 'A' <= x <= 'Z':
                        cap = cap + 1
                    elif 'a' <= x <= 'z':
                        small = small + 1
                if (cap == 0) and (small == 0):
                    print("Invalid Input")
                else:
                    print(min(cap, small))


if __name__ == "__main__":
    main()
