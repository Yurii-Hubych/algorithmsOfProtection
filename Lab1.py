def register(isLower, char):
    if(isLower):
        return char
    else:
        return char.upper

def shiftEncryption(alphabet, text, key):
    encryptedText = ""
    for symbol in text:
        isLower = symbol.islower() if symbol.isalpha() else 1
        symbol = symbol.upper()
        pos = alphabet.find(symbol)
        if pos != -1:
            new_pos = (pos + key) % len(alphabet)
            new_symbol = alphabet[new_pos]
            if isLower:
                new_symbol = new_symbol.lower()
            encryptedText += new_symbol
        else:
            encryptedText += symbol

    return encryptedText



ukrainian_alphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-,.:; "
uaText = "Хрещатик - серце Києва, де історія зустрічає сьогодення."
enText = "Flowers bring joy and beauty to our lives."

print("Початковий текст - " + uaText)

encryptedText = shiftEncryption(ukrainian_alphabet, uaText, 29)

print("Зашифрований текст із зміщенням на 29 символів вправо - " + encryptedText)

with open("writeUA.txt", "w", encoding="utf-8") as f:
    f.write(encryptedText)

with open("writeUA.txt", "r", encoding="utf-8") as f:
    encryptedText = f.read()

decryptedText = shiftEncryption(ukrainian_alphabet, encryptedText, -29)
print("Розшифрований текст із зміщенням на 29 символів вліво - " + decryptedText)


# EN TEXT
print("Початковий текст - " + enText)

encryptedText = shiftEncryption(english_alphabet, enText, 29)

print("Зашифрований текст із зміщенням на 29 символів вправо - " + encryptedText)

with open("writeEN.txt", "w", encoding="utf-8") as f:
    f.write(encryptedText)

with open("writeEN.txt", "r", encoding="utf-8") as f:
    encryptedText = f.read()

decryptedText = shiftEncryption(english_alphabet, encryptedText, -29)
print("Розшифрований текст із зміщенням на 29 символів вліво - " + decryptedText)