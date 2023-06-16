def strcounter(string):  # сложность O(n)
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)


strcounter('aaabbcdeee')