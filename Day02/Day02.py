
def sentiment_analysis():
    """
    Exercise 1: Sentence Analysis (Character & Word Count)
    Write a Python program that prompts the user to enter a sentence. The program must count and display:
    The total number of characters (including spaces and punctuation).
    The total number of words.
    Sample Input: "Learning Python is fun!"
    Sample Output:

    Total Characters: 23
    Total Words: 4

    """ 
    str = input("Enter a String: ")

    st = str.split()
    print(len(st))


    count = 0
    for i in str:
        count+=1
    # print(count)
    print(f"Total length: {len(str)}")

def reverse_uppercase():
    """
    Exercise 2: Reversed Uppercased String

    Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

    Sample Input: "Bangalore"
    Sample Output: "EROLAGNAB"
    """
    str = input("enter the String: ")
    reversed=str[::-1].upper()
     
    print(reversed)

def email_extractor():
    """
    Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the @) and print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".

    Sample Input: "vinod@vinod.co"
    Sample Output: "vinod.co"
    Sample Input: "vinod.co"
    Sample Output: "Invalid Email"

    """
    string = input("Enter the string: ")

    if '@' not in string:
        print("String does not contain @")
    else:
        domain = string.split("@")[1]
        print(domain)

def vowel_consonant():
    """
    Write a program that prompts the user to enter a string and counts:

    The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
    The total count of all consonants.

    Sample Input: "Vinod Kumar Kayartaya"
    Sample Output:

    Vowel Frequencies:
    a: 4
    e: 0
    i: 1
    o: 1
    u: 1
    Total Consonants: 12

    """
    str = input("Enter a String: ")
    cA = 0
    cE = 0
    cI = 0
    cO = 0
    cU = 0
    cC = 0

    for ch in str:
        if ch == 'a':
            cA+=1
        elif ch == 'e':
            cE +=1
        elif ch == 'i':
            cI += 1
        elif ch == 'o':
            cO += 1
        elif ch == 'u':
            cU += 1
        elif ch.isalpha():
                cC+=1

    print(f"vowel Frequencies: ")
    print(f"a: {cA}")
    print(f"e: {cE}")
    print(f"i: {cI}")
    print(f"o: {cO}")
    print(f"u: {cU}")
    print(f"Total Consonants: {cC}")

def title_formatter():
        """
        Exercise 5: Custom Title Case Formatter

        Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). Do not use Python's built-in .title() method.

        Sample Input: "WELCOME TO BANGALORE CITY"
        Sample Output: "Welcome To Bangalore City"
        """
        str = input("Enter a String: ")

        split_str = str.split()

        res = []

        for word in split_str:
            new_word = word[0].upper() + word[1:].lower()
        res.append(new_word)

        print(" ".join(res))


def ciphr():
    """
        Exercise 6: Shift Cipher Encrypter

    Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher.
    It should shift each alphabetical character in the string by the specified shift number down the alphabet.
    Maintain uppercase and lowercase characters, and leave
    spaces or punctuation marks completely unchanged.

    . Sample Input: (User inputs string "Vinod" and shift 3)
    . Sample Output: "Ylqrg"
    """
    string_input = input()
    shift = int(input())
    new_string = ""
    for _chr in string_input:
        flag = _chr.isupper()
        fflag = _chr.islower()

        if flag:
            n = (ord(_chr) - ord("A") + shift) % 26
            new_string += chr(ord("A") + n)
        elif fflag:
            n = (ord(_chr) - ord("a") + shift) % 26
            new_string += chr(ord("a") + n)
        else:
            new_string += _chr
    print(new_string)


def substr():
    """
        Exercise 7: Manual Substring Counter

    Write a program that prompts the user to enter a main text string and a substring. Count how many times the substring appears in the main string without using Python's built-in
    .count() method.

    . Sample Input: (User inputs main string
    . Sample Output: 2

    "banana'

    "an" )
    and substring
    """
    string_input = input()
    substring_input = input()

    x = string_input.split(substring_input)
    print(len(x) - 1)


def name_anonymizer():
    """
        Exercise 8: Name Anonymizer

    Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. The output should print the initials of the first and middle names
    followed by the full last name. If the name consists of only a single word, print it as-is.

    . Sample Input: "Vinod Kumar Kayartaya'
    · Sample Output: "V. K. Kayartaya"
    . Sample Input: "Bangalore"
    · Sample Output: "Bangalore"
    """
    full_name = input()
    sep_name = full_name.split(" ")
    short_name = ""

    for i in range(len(sep_name) - 1):
        short_name += sep_name[i][0] + "." + " "
    short_name += sep_name[-1]

    print(short_name)


def longest_palindrome():
    """
        Exercise 9: Longest Palindromic Substring

    Write a program that prompts the user to enter a text string and finds the longest substring within it that reads the same forward and backward. If there are multiple palindromic
    substrings of the same maximum length, print any one of them.

    · Sample Input: "babad"
    · Sample Output: "bab" (or "aba")
    . Sample Input: "cbbd"
    · Sample Output: "bb"
    """
    s = input()
    longest = ""

    for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right<len(s):
            if s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]

                left -= 1
                right += 1
            else:
                break

# EVEN
        left = i 
        right = i+1

        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]

                left -= 1
                right += 1
            else:
                break

    print(longest)


def run_length_compression():
    # s="aabcccccaaa"
    # s="abcd"
    s_input = input()
    result = ""
    count = 1

    for index in range(len(s_input)):
        if index == len(s_input) - 1:
            result += s_input[index] + str(count)

        elif s_input[index] == s_input[index + 1]:
            count += 1
        else:
            result += s_input[index] + str(count)
            count = 1

    if len(result.split("1")) - 1 == len(s_input):
        result = s_input
    print(result)

def group_anagram():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    dict1={tuple(sorted(word)):[] for word in words}
    for word in words:
        dict1[tuple(sorted(word))].append(word)
        
    print(list(dict1.values()))    
    # print(help(dict1.values))    

def date_validator():
    """
    Write a program that prompts the user to enter a date string in the format "DD/MM/YYYY".

Warning

    Do not use any built-in date/time library functions (such as the datetime or time modules) to format or validate the dates. You must parse and split the string manually, and use a custom tuple of month names for the pretty output if needed.

    Your program must:

    Verify if the date is valid. To be valid:
        The month must be between 1 and 12 inclusive.
        The day must be valid for that specific month (e.g., April, June, September, November have 30 days; others have 31 days).
        For February, the day must be at most 29 in a leap year (divisible by 4, except for centuries not divisible by 400) and at most 28 in standard years.
    If the date is valid, use a tuple of month names ("January", "February", ...) to format and print the date in a long-form readable layout: "MonthName DD, YYYY".
    If the date is invalid, print "Invalid Date".

    Sample Input: "26/08/2026"
    Sample Output: "August 26, 2026"
    Sample Input: "29/02/2026" (2026 is not a leap year)
    Sample Output: "Invalid Date"
    Sample Input: "31/04/2026" (April only has 30 days)
    """

    s_input = input("Enter the date in DD/MM/YYYY format: ")

    split_input = s_input.split('/')

    if(len(split_input) != 3 ):
        print(f"Invalid input try in given format")
        return

    day = int(split_input[0])
    month = int(split_input[1])
    year = int(split_input[2])  

    months = ("January", "feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

    if month < 1 or month > 12:
        print("Invalid month")
        return
    
    leap_year = (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)

    if month == 2:
        if leap_year:
            max_day = 29
        else: 
            max_day = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_day = 30
    else: 
        max_day = 31

    if day <= 0 or day > max_day:
        print("Invalid date")
        return

    print(f"{months[month - 1]} {day}, {year}")

    
def main():
    # sentiment_analysis()
    # reverse_uppercase()
    # email_extractor()
    # vowel_consonant()
    # title_formatter()
    # group_anagram()
    # run_length_compression()
    # longest_palindrome()
    # name_anonymizer()
    # substr()
    # ciphr()
    # date_validator()
    pass


main()
