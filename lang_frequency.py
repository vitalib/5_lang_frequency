import string
import argparse
import chardet


def get_encoding(filepath):
    with open(filepath, 'rb') as a_file:
        return chardet.detect(a_file.read())['encoding']


def load_data(filepath):
    file_encoding = get_encoding(filepath)
    with open(filepath, encoding=file_encoding) as a_file:
        return a_file.read()


def get_most_frequent_words(text):
    frequences_dict = dict()
    for word in text.split():
        if word in frequences_dict:
            frequences_dict[word] += 1
        else:
            frequences_dict[word] = 1
    return sorted(frequences_dict.items(),
                  key=lambda word_freq: word_freq[-1],
                  reverse=True,
                  )[:10]


def get_file_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    return parser.parse_args().filename


def delete_punctuation(text):
    for sign in string.punctuation:
        text = text.replace(sign, ' ')
    return text


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
    text = text.lower()
    text = delete_punctuation(text)
    words_frequency = get_most_frequent_words(text)
    print_frequency(words_frequency)
