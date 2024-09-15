#github_url: https://github.com/Bipuojha1/softwarenow_assignment2.git

# Ciphered text
ciphered_text = """
VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
"""

# Function to decrypt the text using a Caesar Cipher shift
def decrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Calculate the shifted character
            if char.isupper():
                # Shift within uppercase letters
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Shift within lowercase letters
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result += decrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

# Try all possible shifts from 1 to 25 to find the correct shift key
for s in range(1, 25):
    decrypted_text = decrypt_caesar(ciphered_text, s)
    print(f"Shift {s}:\n{decrypted_text}\n")
