alphabet = {
    "а" : 0,
    "б" : 32,
    "в" : 31,
    "г" : 30,
    "ґ" : 29,
    "д" : 28,
    "е" : 27,
    "є" : 26,
    "ж" : 25,
    "з" : 24,
    "и" : 23,
    "і" : 22,
    "ї" : 21,
    "й" : 20,
    "к" : 19,
    "л" : 18,
    "м" : 17,
    "н" : 16,
    "о" : 15,
    "п" : 14,
    "р" : 13,
    "с" : 12,
    "т" : 11,
    "у" : 10,
    "ф" : 9,
    "х" : 8,
    "ц" : 7,
    "ч" : 6,
    "ш" : 5,
    "щ" : 4,
    "ь" : 3,
    "ю" : 2,
    "я" : 1
}

def findLetterInDictionaryByGivenLetter(givenLetter):
    for letter in alphabet:
        if letter == givenLetter:
            return alphabet[letter]

def findLetterInDictionaryByGivenKey(givenKey):
    if givenKey > 32:
        givenKey %= 33
    for letter in alphabet:
        if alphabet[letter] == givenKey:
            return letter

def encryption(text, gamma):
    text = text.lower()
    print(text)
    encryptedText = ""
    for i in range(len(text)):
        numberOfLetterInText = findLetterInDictionaryByGivenLetter(text[i])
        numberOfLetterInGamma = findLetterInDictionaryByGivenLetter(gamma[i])
        encryptedNumberOfLetter = numberOfLetterInGamma + numberOfLetterInText
        encryptedText += findLetterInDictionaryByGivenKey(encryptedNumberOfLetter)
    return encryptedText

def decryption(text,gamma):
    decryptedText = ""
    for i in range(len(text)):
        numberOfLetterInText = findLetterInDictionaryByGivenLetter(text[i])
        numberOfLetterInGamma = findLetterInDictionaryByGivenLetter(gamma[i])
        encryptedNumberOfLetter = numberOfLetterInText - numberOfLetterInGamma
        if encryptedNumberOfLetter < 0:
            encryptedNumberOfLetter += 33
        decryptedText += findLetterInDictionaryByGivenKey(encryptedNumberOfLetter)
    return decryptedText



gamma = "прикладнаматематикаприкладнама"
text = "Життяцедарякийпотрібноцінувати"
encryptedText = encryption(text, gamma)
print(encryptedText)
print(decryption(encryptedText, gamma))
