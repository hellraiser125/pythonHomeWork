import random

class PasswordGen:

    def __init__(self):
        self.__length = 0
        self.__digits = '0123456789'
        self.__low = 'abcdefghijklmnopqrstuvwxyz'
        self.__upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.__spec = '!#$%&*+-=?@^_.'
        self.__chars = ''
        self.__num_of_pass = 0
        self.__include_digits = False
        self.__include_upp = False
        self.__include_low = False
        self.__include_punctuation = False
        self.__exclude_ambiguous_characters = False

    def get_data(self):
        self.__num_of_pass = int(input('Num of passwords for genration '))
        self.__length = int(input('Length of password: '))
        self.__include_digits = input('Include digits (0123456789) in password ? (Yes/No): ')
        self.__include_upp = input('Include uppercase letters in password? (Yes/No): ')
        self.__include_low = input('Include lowercase letters in password? (Yes/No): ')
        self.__include_punctuation = input('Include special symbols ( ! # $% & * + - =? @ ^ _ ) in password ? (Yes/No): ')
        self.__exclude_ambiguous_characters = input('Include ambiguous symbols ( il1Lo0O ) in password ? (Yes/No): ')
        if self.__include_digits == 'Yes':
            self.__chars += self.__digits
        if self.__include_upp == 'Yes':
            self.__chars += self.__upp
        if self.__include_low == 'Yes':
            self.__chars += self.__low
        if self.__include_punctuation == 'Yes':
            self.__chars += self.__spec
        if self.__exclude_ambiguous_characters == 'Yes':
            self.__chars = self.__chars.replace('1', '')
            self.__chars = self.__chars.replace('0', '')
            self.__chars = self.__chars.replace('l', '')
            self.__chars = self.__chars.replace('I', '')
            self.__chars = self.__chars.replace('O', '')
        print('Symbols which can be in password: ', self.__chars)

    def generate_password(self):
        for i in range(self.__num_of_pass):
            password = ''
            for j in range(self.__length):
                password += self.__chars[int(random.random() * len(self.__chars))]
            print(f"Your {i + 1} password: {password}")


x = PasswordGen()
x.get_data()
x.generate_password()
