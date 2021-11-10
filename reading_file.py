if __name__ == '__main__':
    with open("ludzie.txt", 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            print(line)
            print(line.split('\t'))
