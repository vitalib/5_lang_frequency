import re
import collections
import argparse
import chardet


def get_encoding(filepath):
    with open(filepath, 'rb') as a_file:
        return chardet.detect(a_file.read())['encoding']


def load_data(filepath):
    file_encoding = get_encoding(filepath)
    with open(filepath, encoding=file_encoding) as a_file:
        return a_file.read()


def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args().filename


def print_frequency(words_frequency):
    longest_word = max(words_frequency,
                       key=lambda frequency: len(frequency[0])
                       )[0]
    max_field_width = len(longest_word)
    print('Most frequent words:')
    for word_freq in words_frequency:
        print('{:{width}} {}'.format(*word_freq, width=max_field_width))


if __name__ == '__main__':
    file_name = get_file_name()
    text = load_data(file_name)
    all_words = re.findall(r'\w+', text.lower())
    most_frequent_words = collections.Counter(all_words).most_common(10)
    print_frequency(most_frequent_words)
