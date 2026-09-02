import pprint
import re


def analyze_server_logs(logs_text: str):
    log_list = logs_text.splitlines()
    # print(f'{log_list=}')
    pattern_1 = (
        r"(?P<ipaddress>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) - - "
        r"(?P<timestamp>\[[0-9]{1,2}\/[A-Za-z]{3}\/[0-9]{4}\:[0-9]{2}\:[0-9]{2}\:[0-9]{2}\]) "
        r"\"(?P<method_name>(GET|POST|PUT|DELETE)) (?P<directory>\/[A-Za-z0-9_./]+) (?P<proto>[A-Z0-9\/\.]+)\" "
        r"(?P<status>[0-9]{3}) (?P<bytes>[0-9]+)"
    )
    dict_list = []
    for log in log_list:
        match = re.match(pattern=pattern_1, string=log)
        if match == None:
            dict_list.append(
                "Warning: Could not parse line: '<line>'. Skipping.")
            continue
        dict_1 = {'ip': match.group('ipaddress'),
                  'time': match.group('timestamp'),
                  'method': match.group('method_name'),
                  'resource': match.group('directory'),
                  'status': match.group('status'),
                  'bytes': match.group('bytes')}
        dict_list.append(dict_1)
    return dict_list


def scrape_directory_phones(directory_text):
    ptr = r"\(?(?P<area_code>[0-9]{3})\)?[- ]?(?P<prefix>[0-9]{3})-?(?P<line_number>[0-9]{4})"
    matches = re.finditer(ptr, directory_text)
    return [match.groupdict() for match in matches]


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

def process_dataset(dataset):
    
    parsed = map(
        lambda x: (
            x[0],
            float(x[1].split(":")[1]),
            float(x[2].split(":")[1])
        ),
        dataset
    )

    filtered = filter(
        lambda x: x[1]<=1200, parsed
    )

    mapped = map(
        lambda x: {
            "product": x[0],
            "price": x[1],
            "score": x[2]
        }, filtered
    )

    result = sorted(mapped, key=lambda x:x["score"], reverse=True)

    return result


AUDIT_TRANSACTION_COUNT = 0
def create_bank_account(owner_name, initial_bal):
    balance  = float(initial_bal)
    history = [f'Acc create with {balance}']
    def deposit(amt):
        nonlocal balance
        global AUDIT_TRANSACTION_COUNT

        balance += amt
        history.append(f"deposit {amt}")
        AUDIT_TRANSACTION_COUNT += 1

    def withdraw(amt):
        nonlocal balance
        global AUDIT_TRANSACTION_COUNT

        if balance >= amt:
            balance -= amt
            history.append(f"withdraw {amt}")
            AUDIT_TRANSACTION_COUNT += 1
        else:
            raise ValueError(f"Insufficient balance")

    def get_statment():
        return(
            owner_name,
            balance,
            history.copy()
        )
    return {
        "deposit" : deposit,
        "withdraw" : withdraw,
        "statement" : get_statment
    }

def main():
    pass
    print(AUDIT_TRANSACTION_COUNT)

    acc = create_bank_account("Arham", 1000.0)

    acc["deposit"](200.0)

    acc["withdraw"](150.0)

    try:
        acc["withdraw"](2000.0)
    except ValueError as e:
        print(e)

    owner, bal, txn_history = acc["statement"]()

    print(owner)
    print(bal)
    print(txn_history)

    print(AUDIT_TRANSACTION_COUNT)
# data_input = [
#     ("Laptop", "Price: 1200", "Rating: 4.8"),
#     ("Phone", "Price: 800", "Rating: 4.5"),
#     ("Mouse", "Price: 25", "Rating: 4.7"),
#     ("Charger", "Price: 15", "Rating: 4.2")
# ]

# result = process_dataset(data_input)

# print(result)
    # print(validate_academic_email("arham.khan@cdac.res.in"))  # Output: True
    # print(validate_academic_email("lisa_stud12@mit.edu"))      # Output: True
    # # Output: False (invalid suffix)
    # print(validate_academic_email("vinod@gmail.com"))
    # # Output: False (contains uppercase letters)
    # print(validate_academic_email("ALICE@college.edu"))
    # print(validate_academic_email("bob@mit.edu.com"))
    # total1 = calculate_cafeteria_bill(100.0)
    # print(f"{total1=}")
    # total2 = calculate_cafeteria_bill(
    #     100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0
    # )
    # print(f"{total2=}")

#     log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
# 8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
# Corrupted log entry here
# 10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
# 172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""

#     pprint.pprint(analyze_server_logs(logs_text=log_data))

#     directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."

#     pprint.pprint(scrape_directory_phones(directory))



main()
