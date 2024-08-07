def stringrotation(s1, s2):
    s2 = s2[::-1]
    if s1 == s2:
        return "String is matching "
    else:
        return "Strings are not matching "

output = stringrotation("ABCD", "CDBA")
print(output)

                                                                                                                                                                                                