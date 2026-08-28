def factorial():
    """
    Q.1.
    Using for loop,
    write and run a Python program for this algorithm.
     Here is an algorithm to print out n! (n factorial) from 0! to 10! :1.Setf=12.Set n=0
     3.Repeat the following 10 times:a.Outputn,"!=",fb.Add 1 to n c.Multiply f by n
    """

    x = 1
    for i in range(10):
        x *= i + 1
        print(f"{i+1}!={x}")


def factorial_part_two():
    x, i = 1, 1
    while x < 2 * (10**8):
        x*=i
        print(f"{i}!={x}")
        i+=1
    print(x*i)

def main():
    # factorial()
    # factorial_part_two()
    
    ...


main()
