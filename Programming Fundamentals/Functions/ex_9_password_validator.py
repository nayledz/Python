def valid_password(string):
    counter = 0
    is_valid = True
    if not (6 <= len(string) <= 10):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for ch in string:
        if ch.isdigit():
            counter += 1
        if ch in "[@_!#$%^&*()<>?/|}{~:]":
            print("Password must consist only of letters and digits")
            is_valid = False
            break
    if counter < 2:
        print("Password must have at least 2 digits")
        is_valid = False

    if is_valid:
        print("Password is valid")


password = input()
valid_password(password)