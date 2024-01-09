def uppercase(str):
    for i in str:
        char_imp = i
        num_ord = ord(i)
        if num_ord > 96 and num_ord < 123:
            char_imp = chr(num_ord - 32)
        print("{}".format(char_imp), end="")
    print("")
