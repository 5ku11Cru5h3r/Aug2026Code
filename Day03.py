def x():
    s = ["staff", "potion", "spellbook"]

    print("Portal transition activated!")

    a = input()
    b = s.pop(0)
    s.append(a)

    print(f"Ejected oldest item: {b}")
    print(f"Current items in the magic bag: {s}")


def playlist():
    """
        ### Exercise 2: Movie Night Playlist
    **Scenario**: You are organizing a movie marathon. You start with a playlist: `["Inception", "The Matrix", "Interstellar"]`. Prompt the user to enter the name of a movie they want to add.
    * If the movie is already in the list, print `"Already added!"` and do not insert it.
    * If it is not in the list, append it to the end of the list.
    Finally, sort the movie list alphabetically and print the updated playlist.
    * **Sample Input**: `"Interstellar"`
    * **Sample Output**:
      ```text
      Already added!
      Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']
      ```
    * **Sample Input**: `"Avatar"`
    * **Sample Output**:
      ```text
      Added Avatar!
      Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']
      ```
    """
    playlist = ["Inception", "The Matrix", "Interstellar"]
    # while True:
    movie = input()
    if not (playlist.count(movie)):
        playlist.append(movie)
        playlist = sorted(playlist, key=lambda x: x.lower())
        print(f"{playlist=}")
        # break
    else:
        print("retry (r) any other to continue")
        print(f"{playlist=}")

        # break


def cargo_train():
    """
    ### Exercise 3: The Cargo Train Scanner
    **Scenario**: A train has wagons carrying different resources: `["coal", "iron", "gold", "coal", "timber", "coal"]`. The train conductor wants to inspect the cargo. Write a program that prompts the user to enter a resource type (e.g., `"coal"` or `"gold"`).
    * Print the total number of wagons carrying that resource (using `.count()`).
    * If the resource is on the train, print the index of the very first wagon carrying it (using `.index()`). If it is not found, print `"Resource not found on train!"`.
    * **Sample Input**: `"coal"`
    * **Sample Output**:
      ```text
      Number of coal wagons: 3
      First coal wagon is at index: 0
      ```
    * **Sample Input**: `"oil"`
    * **Sample Output**: `"Resource not found on train!"`

    ---
    """
    x = ["coal", "iron", "gold", "coal", "timber", "coal"]
    y = input()

    print(f"Number of coal wagons: {x.count(y)}")
    print(f"First coal wagon is at index: {x.index(y)}")
    ...


def vip_queue():
    """
        ### Exercise 4: Nightclub VIP Queue
    **Scenario**: A nightclub bouncer maintains a list of VIP guests who are allowed inside: `["Guido", "Esha", "Rajan", "Kishori"]`. As guests arrive at the door, the bouncer prompts the user to enter their name.
    * If the guest is on the VIP list, move them from their current position in the queue and insert them at the front of the queue (index 0).
    * If the guest is not on the VIP list, print "Access denied. Not on the VIP list." and do not modify the list.
    Run this program in a loop. The loop should stop when the user types `"exit"`. Print the updated queue state after each guest arrives.
    * **Sample Walkthrough**:
      ```text
      Current VIP queue: ['Guido', 'Esha', 'Rajan', 'Kishori']
      Enter guest name: Rajan
      Rajan moved to the front!
      Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

      Enter guest name: Vinod
      Access denied. Not on the VIP list.
      Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

      Enter guest name: exit
      ```
    """
    l = ["Guido", "Esha", "Rajan", "Kishori"]
    while True:
        k = input("Enter guest name: ")
        if l.count(k):
            l.pop(l.index(k))
            l.insert(0, k)
            print(f"{k} moved to the front!")
            # print(f"Current VIP queue: {l}")
        elif k == "exit":
            break
        else:
            print('Access denied. Not on the VIP list.')
        print(f"Current VIP queue: {l}")

def xxxxx():
    ...
def main():
    
    ...


main()
