from sys import argv

def unpack(input_file): 

    opened_file = open(input_file)

    words = []

    for line in opened_file:
        line = line.strip()
        words += line.split(" ")

    opened_file.close()    
    return words  

def tally(words):
    tally_count = {}
    for word in words:
        if word in tally_count:
            tally_count[word] += 1
        else:
            tally_count[word] = 1

    # tally_count = {word:(tally_count[word]+1 if word in tally_count else 1) for word in words}

    return tally_count 

def print_output(tally_count):
    for word in tally_count.iteritems():
        key, value = word
        print key, value

def main(input_file):
    tally_count = tally(unpack(input_file))
    print_output(tally_count)

if __name__ == "__main__":
    script, input_file = argv
    main(input_file)