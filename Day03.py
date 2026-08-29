def x():
    s = ["staff", "potion", "spellbook"]

    print("Portal transition activated!")

    a = input()
    b = s.pop(0)
    s.append(a)

    print(f"Ejected oldest item: {b}")
    print(f"Current items in the magic bag: {s}")


def main():
    x()


main()