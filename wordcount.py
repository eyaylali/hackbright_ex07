from sys import argv
import string

def unpack(input_file): 

    opened_file = open(input_file)

    words = []

    for line in opened_file:
        line = line.translate(string.maketrans("",""), string.punctuation)
        line = line.strip().lower()
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

def sort_by_freq(tally_count):
    desc = sorted(tally_count.values())
    for i in desc:
        if 
    print desc


# def sort_same_freq(): 

# def print_output(freq_sorted):
#     for word in freq_sorted:
#         key, value = word
#         print key, value

def main(input_file):
    unpacked = unpack(input_file)
    tally_count = tally(unpacked)
    freq_sorted = sort_by_freq(tally_count)
    # print_output(freq_sorted)

if __name__ == "__main__":
    script, input_file = argv
    main(input_file)