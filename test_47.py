
SSN_white_list = [1234, 2342, 2331]

while True:

    user_ssn_number = input('Enter your SSN number in format (0000: )')

    if len(user_ssn_number) !=4:
        print('Invalid SSN number, please check the format (0000)');
        continue