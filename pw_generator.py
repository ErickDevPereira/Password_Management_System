import random

def shuffle(lst):
    length = len(lst)
    shuffled_list = []
    for _ in range(0, length):
        ind = random.randint(0, len(lst) - 1)
        shuffled_list.append(lst[ind])
        lst.remove(lst[ind])
    return shuffled_list

'''Given an integer n, this function returns a string with n characters,
where n should be greater than 6. Moreover, the returned string has characters
with 4 types: upper letter, lower letter, digit and symbol'''
def new_password(n):
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = lower_letters.upper()
    symbols = '!@#$%&*-_.'
    num = '0123456789'
    tot_possibilities  = lower_letters + upper_letters + symbols + num
    pw_characters = [-1, -1, -1, -1, -1, -1]
    pos_lower = random.randint(0, 5)
    pos_upper = random.randint(0, 5)
    while pos_upper == pos_lower:
        pos_upper = random.randint(0, 5)
    pos_symbol = random.randint(0, 5)
    while pos_symbol in (pos_lower, pos_upper):
        pos_symbol = random.randint(0, 5)
    pos_num = random.randint(0, 5)
    while pos_num in (pos_lower, pos_upper, pos_symbol):
        pos_num = random.randint(0, 5)
    pw_characters[pos_lower] = random.choice(lower_letters)
    pw_characters[pos_upper] = random.choice(upper_letters)
    pw_characters[pos_symbol] = random.choice(symbols)
    pw_characters[pos_num] = random.choice(num)
    for ind, item in enumerate(pw_characters):
        if item == -1:
            pw_characters[ind] = random.choice(tot_possibilities)
    if n > 6:
        for i in range(n):
            if i > 5:
                pw_characters.append(random.choice(tot_possibilities))
    my_pw = ''.join(shuffle(pw_characters))#The shuffle brings more arbitrarity over the creation of the password.
    return my_pw

if __name__ == '__main__':
    print(new_password(16))