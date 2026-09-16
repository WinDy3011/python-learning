import os
import string

#D:\python_project\helper_files\practice_text_english.txt
def get_count_words(filename):
    all_words = []

    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                word = word.strip(string.punctuation)
                all_words.append(word)
    print("get_count_words finished")
    return all_words

def count_exsclusive_words(filename):
    with open(filename, "r") as f:
        words_dict = dict()

        for line in f:
            words = line.split()

            for word in words:
                word = word.lower()
                word = word.strip(string.punctuation)
                if word not in words_dict:
                    words_dict[word] = 1
                else:
                    words_dict[word] += 1
        return words_dict

def sort_dict(dictionary):
    new_dict = dict()
    while dictionary:

        last_value = 0
        max_key = None

        for key, value in dictionary.items():
            if value > last_value:
                last_value = value
                max_key = key

        new_dict[max_key] = last_value
        dictionary.pop(max_key)
    return new_dict



def main():
    filename = input("Specify the path file: ")
    if not os.path.exists(filename):
        print("The specified path does not exist")
        return
    word = get_count_words(filename)
    exclusive_words = count_exsclusive_words(filename)

    print("the number of all words" , len(word))
    print("The exclusive words: ", len(exclusive_words))
    sorted_words = sort_dict(exclusive_words)
    for word in sorted_words:
        print(f"{word} : {sorted_words[word]}")


if __name__ == "__main__":
    main()
