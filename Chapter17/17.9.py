def get_word_counts(input_file):
    word_counts = dict()
    words = []
    for line in input_file:
        words += line.split()
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    return word_counts

def get_word_count(word, word_counts):
    return word_counts[word]

def main():
    input_file = open("AliceInWonderland.txt", "r") 
    word_counts = get_word_counts(input_file)
    print get_word_count("the", word_counts) 
    print get_word_count("Alice", word_counts) 

main()
