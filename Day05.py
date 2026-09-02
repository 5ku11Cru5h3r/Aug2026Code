import re


def analyze_server_logs(logs_text: str){
    log_list = logs_text.slice('\n')
    pattern_1 = r"""^(?P<ipaddress>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) - - (?P<timestamp>\[[0-9]{1,2}\/[A-Za-z]{3,3}\/[0-9]{4,4}\:[0-9]{2,2}\:[0-9]{2,2}\:[0-9]{2,2}\]) \"(?P<method_name>(GET|POST|PUT|DELETE)) (?P<directory>\/[a-z.]+) (?P<proto>[A-Z0-9\/\.]+)\" (?P<status>[0-9]{3,3}) (?P<bytes>[0-9]{1,})$"""
    for log in log_list:
}


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
    if re.match(r, email) == None:
        return False
        # raise ValueError("email not entered correctly")
    else:
        return True


def main():
    print(validate_academic_email("arham.khan@cdac.res.in"))  # Output: True
    print(validate_academic_email("lisa_stud12@mit.edu"))      # Output: True
    # Output: False (invalid suffix)
    print(validate_academic_email("vinod@gmail.com"))
    # Output: False (contains uppercase letters)
    print(validate_academic_email("ALICE@college.edu"))
    print(validate_academic_email("bob@mit.edu.com"))
    total1 = calculate_cafeteria_bill(100.0)
    print(f"{total1=}")
    total2 = calculate_cafeteria_bill(
        100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0
    )
    print(f"{total2=}")


main()
