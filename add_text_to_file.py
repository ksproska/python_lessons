def main():
    while True:
        # pobranie tekstu z konsoli
        given_text = input("Add text:   ")
        with open('example.txt', 'a', encoding='utf8') as f:
            f.write(given_text)


if __name__ == '__main__':
    main()
