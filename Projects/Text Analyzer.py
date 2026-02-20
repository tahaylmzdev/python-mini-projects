import string

print("""
--------------------------------------------------
             WELCOME TO TEXT ANALYZER
--------------------------------------------------
""")


def main():
    menu()


def menu():
    try:
        selection = int(input("""
Please choose one of the options (1/0)
1. Enter Text
0. Exit
> """))
    except ValueError:
        print("\n>>> Please enter valid data!")
        return menu()

    if selection == 1:
        text_input()
    elif selection == 0:
        print("\nWell, have a nice day!")
    else:
        print("\n>>> Please enter valid data")
        return menu()


def text_input():
    text = input("""Please enter your text below:
    > """)

    if not text.strip():
        print("\n\nYou cannot leave blank! Please enter a valid text.")
        return text_input()
    else:
        return analyzer(text)

def analyzer(text):
    # Character Counter
    ch_num = []
    for ch in text.lower():
        if ch.isspace() == False and ch not in string.punctuation:
            ch_num.append(ch)

    total_ch = len(ch_num)

    # Unique Character Counter
    counted_ch = []
    for ch in text.lower():
        if ch in counted_ch:
            continue
        elif ch.isspace() == False and ch not in string.punctuation:
            counted_ch.append(ch)
    un_ch_num = len(counted_ch)

    # Text Cleaner
    clean_text = ""
    for ch in text:
        if ch not in string.punctuation:
            clean_text += ch
    prep_text = clean_text.lower().split()

    # Word Counter
    word_num = len(prep_text)

    # Unique Word Counter
    counted_word = []
    for word in prep_text:
        if word in counted_word:
            continue
        else:
            counted_word.append(word)
    un_word_num = len(counted_word)

    # Most Frequent 5 Words
    word_dict = {}
    for word in prep_text:
        word_dict.update({word: prep_text.count(word)})

    sorted_dict = {k: v for k, v in sorted(word_dict.items(), key=lambda item: item[1], reverse=True)}

    top_5_list = []
    for i, (k, v) in enumerate(sorted_dict.items()):
        if i == 5:
            break
        top_5_list.append(f"{k.capitalize()} ---> {v}")

    return result(total_ch, un_ch_num, word_num, un_word_num, top_5_list)


def result(ch_total, ch_unique, w_total, w_unique, top_words):
    print("\n" + "=" * 50)
    print("                ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total Characters (no punctuations and spaces): {ch_total}")
    print(f"Unique Characters          : {ch_unique}")
    print(f"Total Words                : {w_total}")
    print(f"Unique Words               : {w_unique}")
    print("-" * 50)
    print("Top 5 Most Frequent Words:")
    for item in top_words:
        print(f" * {item}")
    print("=" * 50)

    input("\nPress Enter to go back to Menu...")
    return menu()


if __name__ == "__main__":
    main()