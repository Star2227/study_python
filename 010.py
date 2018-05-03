filename = 'README.txt'
with open(filename) as file_object:
    contents = file_object.read()
    words = contents.split()
    num_words = len(words)
    print(num_words)