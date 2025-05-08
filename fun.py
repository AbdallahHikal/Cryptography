from sympy import mod_inverse
import onetimepad
import math
import base64
import pyDes

alphabet ="abcdefghijklmnopqrstuvwxyz"



#========================================================================================================
#                       -------------------------- Caesar -------------------------
def caesar_E(plaintext,key):
    ciphertext=""
    for p in plaintext:
        p_val=ord(p)
        c_value = ( p_val + key )
        ciphertext += chr(c_value)
    return ciphertext

def caesar_D(ciphertext,key):
    plaintext=""
    for c in ciphertext:
        c_val= ord(c)
        p_value=(c_val - key)
        plaintext += chr(p_value)
    return plaintext



#========================================================================================================
#                       -------------------------- Affine -------------------------

def affine_E(plaintext, a, b):
    ciphertext = ""
    for p_ch in plaintext:
        if p_ch.isalpha():
            p_value = alphabet.index(p_ch)
            c_value = (a * p_value + b) % 26
            c_ch = alphabet[c_value]
            ciphertext += c_ch
        else:
            continue
    return ciphertext

def affine_D(ciphertext, a, b):
    plaintext = ""
    for c_ch in ciphertext:
        c_value = alphabet.index(c_ch)
        inv = mod_inverse(a, 26)
        p_value = inv * (c_value - b) % 26
        p_ch = alphabet[p_value]
        plaintext += p_ch
    return plaintext



#========================================================================================================
#                       -------------------------- Vigener -------------------------

def generate_key (text,key):
    
    if len(text) == len(key) :
        return key 
    
    elif len(text) < len(key) :
        key = key[:len(text)]
        return key
    
    elif len(text) > len(key):
        for i in range(len(text)- len(key)):
            key += key[i % len(key)]
        return key

def vigener_E (text,key):
    ciphertext = ""
    key = generate_key(text,key)
    print("the generated key = " + key)
    for i in range(len(text)):
        p_value = alphabet.index(text[i])
        k_value = alphabet.index(key[i])
        c_value = (p_value + k_value)%26
        c_ch = alphabet[c_value]
        ciphertext += c_ch 
    return ciphertext

def vigener_D (text,key):
    plaintext = ""
    key = generate_key(text,key)
    print("the generated key = " + key)
    for i in range(len(text)):
        c_value = alphabet.index(text[i])
        k_value = alphabet.index(key[i])
        p_value = (c_value - k_value)%26
        p_ch = alphabet[p_value]
        plaintext += p_ch 
    return plaintext



#========================================================================================================
#                       -------------------------- RailFence -------------------------

def railfence_E(key, text):
    
    text = text.replace(' ','')
    
    cipherText = [""] * key 
    
    for row in range(key):
        pointer = row
        while pointer < len(text):
            cipherText[row] += text[pointer] 
            pointer += key
        print(cipherText[row])
    return "".join(cipherText)

def railfence_D(key, cipherText):
    n = len(cipherText)
    row_length = [ n // key] * key
    
    for i in range(n % key):
        row_length[i] += 1
    
    rows = []
    p = 0
    for l in row_length:   
        rows.append(cipherText[p:p+l]) 
        p += l    

    plaintext = ""
    for i in range(max(row_length)): 
        for row in rows: 
            if i < len(row):    
                plaintext += row[i] 

    return plaintext



#========================================================================================================
#                       -------------------------- OneTimePad -------------------------

def onetimepad_E(plaintext,key):
    ciphertext= onetimepad.encrypt(plaintext,key)
    return ciphertext

def onetimepad_D(ciphertext,key):
    plaintext= onetimepad.decrypt(ciphertext,key)
    return plaintext



#========================================================================================================
#                       -------------------------- Columnar -------------------------

def columnar_E(s, key):
    rows = math.ceil(len(s) / len(key))
    arr = [['_' for _ in range(len(key))] for _ in range(rows)]
    i = 0
    j = 0
    for h in range(len(s)):
        arr[i][j] = s[h]
        j += 1
        if j > len(key) - 1:
            j = 0
            i += 1

    print("The message matrix is:")
    for r in arr:
        print(r)

    cipher_text = ""
    kk = sorted(key)

    for char in kk:
        h = key.index(char)
        for j in range(len(arr)):
            cipher_text += arr[j][h]

    return cipher_text

def columnar_D(cipher_text, key):
    import math
    rows = math.ceil(len(cipher_text) / len(key))
    arr = [['_' for _ in range(len(key))] for _ in range(rows)]
    col_lengths = [rows] * len(key)

    total_chars = len(cipher_text)
    extra = (rows * len(key)) - total_chars
    for i in range(extra):
        col_lengths[-(i+1)] -= 1

    index = 0
    sorted_key = sorted([(char, i) for i, char in enumerate(key)])
    for char, original_index in sorted_key:
        for row in range(col_lengths[original_index]):
            arr[row][original_index] = cipher_text[index]
            index += 1

    plaintext = ""
    for row in arr:
        for ch in row:
            if ch != '_':
                plaintext += ch

    return plaintext



#========================================================================================================
#                       -------------------------- DES -------------------------

key = b"DESCRYPT"
iv = b"\0\0\0\0\0\0\0\0"

def des_E(data):
    ob = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted = ob.encrypt(data)
    return base64.b64encode(encrypted).decode()  # Convert to base64 string

def des_D(data):
    ob = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_bytes = base64.b64decode(data.encode())  # Convert from base64 to bytes
    decrypted = ob.decrypt(encrypted_bytes)
    return decrypted.decode()  # Convert bytes to string



#========================================================================================================
#                       -------------------------- RSA -------------------------


#========================================================================================================
#                       -------------------------- Scytale -------------------------

def scytale_E(text, columns):
    text = text.replace(" ", "").upper()
    rows = -(-len(text) // columns)
    padded_text = text.ljust(rows * columns, '_')  # Use padding if needed
    cipher = ''
    for col in range(columns):
        for row in range(rows):
            cipher += padded_text[row * columns + col]
    return cipher

def scytale_D(cipher, columns):
    rows = -(-len(cipher) // columns)
    full = [''] * (rows * columns)
    k = 0
    for col in range(columns):
        for row in range(rows):
            if k < len(cipher):
                full[row * columns + col] = cipher[k]
                k += 1
    return ''.join(full).rstrip('_')  # Remove padding if present



#========================================================================================================
#                       -------------------------- Keyboard_Offset -------------------------

def keyboard_offset_E(text):
    keyboard = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    offset = 1
    result = ''
    for char in text.upper():
        if char in keyboard:
            i = keyboard.index(char)
            result += keyboard[(i + offset) % len(keyboard)]
        else:
            result += char
    return result

def keyboard_offset_D(text):
    keyboard = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    offset = 1
    result = ''
    for char in text.upper():
        if char in keyboard:
            i = keyboard.index(char)
            result += keyboard[(i - offset) % len(keyboard)]
        else:
            result += char
    return result