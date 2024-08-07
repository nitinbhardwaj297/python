def lower_char(sentence):
    store_smallele = None
    for ele in sentence:
        if ele == ele.lower():
            store_smallele = ele
    
    return store_smallele

lower_char("Nitin")
