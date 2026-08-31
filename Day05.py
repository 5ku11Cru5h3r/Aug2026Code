import re


def calculate_cafeteria_bill(
    base_price: int, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0
):
    total = sum((base_price, *items))
    # print(total)
    total -= (discount / 100) * total
    total += tax_rate * total
    total += delivery_fee

    return total
    ...


def validate_academic_email(email):
    r = r"^[a-z0-9._]+@[a-z0-9]+\.(edu|res\.in)$"
    if re.match(r,email) == None:
        return False
        # raise ValueError("email not entered correctly")
    else:
        return True

def 

def main():
    print(validate_academic_email("arham.khan@cdac.res.in"))  # Output: True
    print(validate_academic_email("lisa_stud12@mit.edu"))      # Output: True
    print(validate_academic_email("vinod@gmail.com"))          # Output: False (invalid suffix)
    print(validate_academic_email("ALICE@college.edu"))        # Output: False (contains uppercase letters)
    print(validate_academic_email("bob@mit.edu.com")) 
    total1 = calculate_cafeteria_bill(100.0)
    print(f"{total1 =}")
    total2 = calculate_cafeteria_bill(
        100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0
    )
    print(f"{total2 =}")


main()
