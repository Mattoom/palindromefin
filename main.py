def is_palindrome(input_string):
    for i in range(int(len(input_string)/2)):
        index_front = i
        index_back = len(input_string) - i - 1
        if input_string[index_front] != input_string[index_back]:
            return False
    return True


def formatting_str(input_string):
    format_string = ""
    for i in input_string:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            format_string += i
    return format_string.upper()


def count_palindrome(format_string):
    count = 0
    for i in range(2, len(format_string) + 1):
        for j in range(0, len(format_string) - i + 1):
            sub_string = format_string[j:j+i]
            if is_palindrome(sub_string):
                count += 1
    return count


def process_palindrome(input_string):
    format_string = formatting_str(input_string)
    print("Formatted string: {}".format(format_string))
    print("Is palindrome: {}".format(is_palindrome(format_string)))
    print("Palindromes in string: {}".format(count_palindrome(format_string)))


while True:
    choice = input("Choose mode: (I)nteractive, (R)ead from file or (E)xit.\n: ")
    if choice == 'I' or choice == 'i':
        input_string = input("Input a string: ")
        process_palindrome(input_string)
    elif choice == 'R' or choice == 'r':
        text_file = open("{}".format(input("Enter file name: ")), "r")
        process_palindrome(text_file)
    elif choice == 'E' or choice == 'e':
        exit(1)
    else:
        print("Invalid input, try again.")


