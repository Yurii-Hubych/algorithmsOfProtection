# Функція для створення таблиці-ключа
def create_key_table():
    key_table = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'І', 'Ї'],
        ['К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф'],
        ['Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ь', 'Ю', 'Я', 'Є', 'Й', 'Ґ']
    ]
    return key_table

def save_key_table_to_file(key_table, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for row in key_table:
            file.write(" ".join(row) + "\n")

def load_key_table_from_file(filename):
    key_table = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            row = line.strip().split(" ")
            key_table.append(row)
    return key_table

def load_open_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
     return file.read()

def save_to_file(filename, text):
    with open(filename, "w", encoding="utf-8") as file:
     return file.write(text)

def playfair_encrypt(plaintext, key_table):
    # Виправлення непарної довжини тексту додавання символу "Х"
    if len(plaintext) % 2 != 0:
        plaintext += 'Х'

    ciphertext = ''
    plaintext = plaintext.replace(' ', '').upper()  # Видаляємо пробіли та переводимо в верхній регістр

    i = 0  # Індекс для просування по вхідному тексту

    while i < len(plaintext):
        pair = plaintext[i:i + 2]

        if len(pair) == 1:
            pair += 'Х'

        row1, col1 = None, None
        row2, col2 = None, None

        for j in range(0, len(plaintext), 2):  # Змінено змінну i на j
            pair = plaintext[j:j + 2]

            if len(pair) == 1:
                pair += 'Х'

            row1, col1 = None, None
            row2, col2 = None, None

            for row in range(len(key_table)):
                if pair[0] in key_table[row]:
                    row1 = row
                    col1 = key_table[row].index(pair[0])
                if pair[1] in key_table[row]:
                    row2 = row
                    col2 = key_table[row].index(pair[1])

            # Додайте перевірку на None
            if row1 is not None and col1 is not None and row2 is not None and col2 is not None:
                if row1 == row2:  # Правило 2: літери в одному рядку
                    col1 = (col1 + 1) % len(key_table[row1])
                    col2 = (col2 + 1) % len(key_table[row2])
                elif col1 == col2:  # Правило 3: літери в одному стовпці
                    row1 = (row1 + 1) % len(key_table)
                    row2 = (row2 + 1) % len(key_table)
                else:  # Правило 1: літери у різних рядках і стовпцях
                    col1, col2 = col2, col1

                ciphertext += key_table[row1][col1] + key_table[row2][col2]
            else:
                pass

            i += 2

    return ciphertext



def main():
    plaintext =  "Привітзільвова"  # Замініть на свій власний текст
    # key_table = create_key_table()
    # save_key_table_to_file(key_table, "key_table.txt")
    key_table = load_key_table_from_file("key_table.txt")
    ciphertext = playfair_encrypt(plaintext, key_table)
    # Записуємо криптограму у файл
    save_to_file("cryptogram.txt", ciphertext)
    print(f"Криптограма: {ciphertext}")
    print("Криптограму записано у файл 'cryptogram.txt'")

if __name__ == "__main__":
    main()
