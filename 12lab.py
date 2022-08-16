import random
import string
"""
def get_the_data():
    step = int(input('Encryption step: '))
    lang = input('Choose lang UA/EU: ')
    message = input("Text foe encryption/decryption: ").upper()
    return step, message, lang

def ces_cypher(step, message, lang, state='encrypt'):
    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    alphabets = {"EU": alfavit_EU, "UA": alfavit_RU}
    real_alphabet = alphabets.get(lang)
    if state == 'encrypt':
        for i in message:
            old_place = real_alphabet.find(i)
            new_place = old_place + step
            if i in real_alphabet:
                result += real_alphabet[new_place]
            else:
                result += i
    elif state == 'decrypt':
        for i in message:
            old_place = real_alphabet.find(i)
            new_place = old_place - step
            if i in real_alphabet:
                result += real_alphabet[new_place]
            else:
                result += i

    return result

step, message, lang = get_the_data()
res = ces_cypher(step, message, lang, state='encrypt')
print(res)

def brut_force():
    letter = input('Letter>>> ').upper().split()
    [print('{}){}'.format(i+1,j)) for i,j in enumerate(letter)]

    word = letter[int(input('Word № ')) - 1]

    for i in range(26):
        ALFA = [chr(i) for i in range(65,91)]
        final = ''

        for key in range(i):
            ALFA.append([0])
            del ALFA[0]

        for char in word:
            if ord(char) in range(65,91):
                final +=chr((ord(char)-i-13)%26+65)
            else:
                final += char

        print('{}) {}'.format(i,final))
    print()
    print('_'*79)
    final = ''
    key = int(input('Key>>> '))
    letter = ' '.join(letter)

    for char in letter:
        if ord(char) in range(65,91):
            final += chr((ord(char)-key-13)%26+65)
        else:
            final+=char
    print('Decrypt >>> {}'.format(final))

brut_force()
"""
def pair():
    alf = {'v': 'l',
           'q': 'r',
           'f': 'o',
           's': 'e',
           'p': 'x',
           'u': 'd',
           'n': 'z',
           'a': 'g',
           'm': 'b',
           'j': 'w',
           'c': 't',
           'k': 'i',
           'h': 'y',
           'l': 'v',
           'r': 'q',
           'o': 'f',
           'e': 's',
           'x': 'p',
           'd': 'u',
           'z': 'n',
           'g': 'a',
           'b': 'm',
           'w': 'j',
           't': 'c',
           'i': 'k',
           'y': 'h'}
    phrase = input('Input the phrase to code: ')
    s = ' '
    for i in phrase:
        s += alf.get(i)
    print(s)
    phr = input('Input encrypt phrase : ')
    e = ' '
    for i in phr:
        e += alf.get(i)
    print(e)
pair()


#RSA
'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p-1) * (q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private key_pair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("===========================================================================================================")
    print("================================== RSA Encryptor / Decrypter ==============================================")
    print(" ")

    p = int(input(" - Enter a prime number (17, 19, 23, etc): "))
    q = int(input(" - Enter another prime number (Not one you entered above): "))

    print(" - Generating your public / private key-pairs now . . .")

    public, private = generate_key_pair(p, q)

    print(" - Your public key is ", public, " and your private key is ", private)

    message = input(" - Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)

    print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypt(private, encrypted_msg))

    print(" ")
    print("============================================ END ==========================================================")
    print("===========================================================================================================")