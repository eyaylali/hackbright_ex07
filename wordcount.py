from sys import argv
import string
from operator import itemgetter

def unpack(input_file): 
    '''Takes in path to text file;
    Returns list of strings, punctuation and spaces removed.'''

    opened_file = open(input_file)

    words = []

    for line in opened_file:
        line = line.translate(None, string.punctuation)
        # line = line.replace(string.punctuation, "") # doesn't work?
        line = line.strip().lower()
        words += line.split()

    opened_file.close()    
    return words  

def tally(words):
    '''Takes in list of strings;
    Returns a dictionary of word strings:count of frequency'''

    tally_count_dict = {}

    for word in words:
        tally_count_dict[word] = tally_count_dict.get(word, 0) + 1

    # for word in words:
    #     tally_count_dict[word] = tally_count_dict.setdefault(word, 0) + 1

    return tally_count_dict





def sort_by_freq(tally_count_dict):
    '''Takes in a dictionary;
    Returns a list of tuples, sorted alphabetically by key and in descending order by value'''

    alphabetical_list = sorted(tally_count_dict.items()) #list of tuples alphabetically a-z
    desc_list = sorted(alphabetical_list, key = itemgetter(1), reverse = True) 
        #accesses second value of tuple, sorts into ascending order, reverses into descending
        #desc = sorted(desc,key=lambda (x,y):(-y,x))
    return desc_list


def print_output(freq_sorted):
    '''Takes in a list of tuples;
    Prints keys and values.'''

    for key, value in freq_sorted:
        print key, value

def main(input_file):
    unpacked = unpack(input_file)
    tally_count_dict = tally(unpacked)
    freq_sorted = sort_by_freq(tally_count_dict)
    print_output(freq_sorted)

if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)