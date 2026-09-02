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

    log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""

    pprint.pprint(analyze_server_logs(logs_text=log_data))

    directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."

    pprint.pprint(scrape_directory_phones(directory))


main()
