from tkinter import N


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
            print("Access denied. Not on the VIP list.")
        print(f"Current VIP queue: {l}")


def word_rev():
    s = input()
    a = s.split()
    ss = " ".join([i[::-1] for i in a])
    print(f"{ss=}")


def curvd():
    inp_strn = input()
    # s = "45 88 30 98 50"
    curved = [
        min(100, int(marks) + (10 if int(marks) < 50 else 5))
        for marks in inp_strn.split()
    ]
    print(curved)


def treasure():
    '''
        ### Exercise 7: Treasure Map Coordinate Filter
        **Scenario**: You have a list of coordinate pairs representing suspected treasure locations on a map: `coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]`. However, the treasure can only exist in the first quadrant of the map (where **both** the X coordinate and Y coordinate are strictly greater than zero (i.e., `x > 0` and `y > 0`)).
        Write a program that uses a list comprehension to filter the list and print only the valid coordinates.
        * **Hardcoded Input**: `coords = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]`
        * **Sample Output**: `[[12, 5], [15, 9]]`
    
    '''
    coordinates = [[12, 5], [-3, 14], [8, -2], [15, 9], [-5, -6]]
    Output = [
        coordinate
        for coordinate in coordinates
        if coordinate[0] > 0 and coordinate[1] > 0
    ]
    print(f"{Output}")


def shopping_cart():
    '''
    ### Exercise 8: De-duplicating Shopping Cart
        **Scenario**: An online shopping cart has duplicate items due to double-clicks: `["apple", "banana", "apple", "orange", "banana", "banana"]`. Write a program that processes the list and removes all duplicate items, **but keeps the first occurrence of each item in its original order**. Print the cleaned cart.
        * **Hardcoded Input**: `cart = ["apple", "banana", "apple", "orange", "banana", "banana"]`
        * **Sample Output**: `['apple', 'banana', 'orange']`
    
        ---
    '''
    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    op = list({items for items in cart})
    print(f'{op = }')
    
def elimination_game():
    N=int(input())
    k=int(input())
    

def main():
    shopping_cart()
    # treasure()
    """
    
    

    ## Part C: Difficult Complexity (2 Exercises)

    ### Exercise 9: The Josephus Elimination Game
    **Scenario**: A group of $N$ soldiers (numbered 1 to $N$) stand in a circle. Starting from the first soldier, every $K$-th soldier is eliminated from the circle. The count continues with the next remaining soldier, moving clockwise. This process repeats until only one soldier remains.
    Write a program that prompts the user to enter $N$ (number of soldiers) and $K$ (elimination interval). Simulate the game using a list and print the order of eliminations and the final survivor.
    * **Sample Input**: `N = 5`, `K = 2`
    * **Sample Output**:
      ```text
      Soldier circle initialized: [1, 2, 3, 4, 5]
      Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
      Eliminated soldier: 4 (Remaining: [1, 3, 5])
      Eliminated soldier: 1 (Remaining: [3, 5])
      Eliminated soldier: 5 (Remaining: [3])
      The sole survivor is: 3
      ```

    ### Exercise 10: Snake Game Board Renderer
    **Scenario**: Render a simple 2D text game board. Write a program that performs the following steps in sequence:
    1. Creates a $5 \times 5$ grid filled with dots `"."` represented as a nested list.
    2. Places a food item `"F"` at grid position `[2, 3]`.
    3. Prompts the user to enter coordinate inputs: a `row` and a `col` (integers between 0 and 4) for the snake's head.
    4. Places the snake's head `"S"` at the user-supplied coordinate `[row, col]`, overwriting the character at that position.
    5. If the user-supplied coordinates are exactly `[2, 3]`, print the message `"Yum! The snake ate the food!"` (the snake `"S"` will occupy index `[2, 3]` on the printed board, overwriting the `"F"`).
    6. Prints the grid neatly line-by-line (each row's elements separated by spaces).

    * **Sample Input**: (User inputs Row `0` and Column `3`)
    * **Sample Output**:
      ```text
      . . . S .
      . . . . .
      . . . F .
      . . . . .
      . . . . .
      ```
    * **Sample Input**: (User inputs Row `2` and Column `3`)
    * **Sample Output**:
      ```text
      . . . . .
      . . . . .
      . . . S .
      . . . . .
      . . . . .
      Yum! The snake ate the food!
      ```
    """
    # word_rev()
    # curvd()
    ...


main()
