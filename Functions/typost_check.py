def typos_check(Model,word,value):
    import difflib
    words = Model.objects.all().values_list(value, flat=True)
    match_words = difflib.get_close_matches(word, list(words))
    return match_words
