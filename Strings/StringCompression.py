def compress(chars):
    curr = 0
    modded = 0
    while curr < len(chars):
        ptr = curr + 1
        count = 1
        while ptr < len(chars) and chars[curr] == chars[ptr]:
            ptr += 1
            count += 1
        if count == 1:
            chars[modded] = chars[curr]
            curr = ptr
            modded += 1
        elif count > 9:
            chars[modded] = chars[curr]
            str_count = str(count)
            for i in range(len(str_count)):
                chars[modded + 1] = str_count[i]
                modded += 1
            modded += 1
            curr = ptr
        else:
            chars[modded] = chars[curr]
            chars[modded + 1] = str(count)
            modded += 2
            curr = ptr

    return chars


print(compress(['a', 'a', 'b', 'b', 'c', 'c', 'c']))
print(compress(['a', 'b', 'b', 'c', 'c']))
print(compress(['a']))
print(compress(["a", "b", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b"]))
print(compress(["a", "b", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b", "c", "d", "d"]))
