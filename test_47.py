SSN_white_list = [1234, 2342, 2331, 6547, 7777]


while True:

    user_ssn_number = input('Enter your SSN number in format (0000: )')

    # length checker
    if len(user_ssn_number) != (4,5):
        print('Invalid SSN number, please check the format (0000)');
        continue

    if not user_ssn_number.isdigit():
        print("Please enter digits only !!!")
        continue

    if int(user_ssn_number) not in SSN_white_list:
        print('Your not permissions')
        continue

print('Ok')