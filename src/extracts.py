def get_extr_data(str_):
    op = {}
    # str_ = "This is very good to have a cup of tea or coffee before brakfast."
    cnt_words = len(str_.split(" "))
    vowels = "aeiouAEIOU"
    count_vowels = sum(str_.count(vowel) for vowel in vowels)
    count_cons = len(str_) - count_vowels
    op = {
        "string": str_,
        "count_words": cnt_words,
        "count_vowels": count_vowels,
        "count_consonants": count_cons,
    }
    print(op)
    return op
