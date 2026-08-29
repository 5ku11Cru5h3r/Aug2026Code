
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
    s = "babad"
    # s = input()
    max_length = 1
    for a in range(1, len(s)-1):
        b = a
        max_length_ = 1
        while s[a] == s[b] and a < len(s) and b > 0:
            a += 1
            b -= 1
            max_length_ += 2
            max_length = max(max_length_, max_length)
    print(f"{max_length}")


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

    
def main():
    # group_anagram()
    # run_length_compression()
    longest_palindrome()
    # name_anonymizer()
    # substr()
    # ciphr()
    pass


main()
