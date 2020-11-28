# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z)


def stringCompression(string):
    new_string = ''
    uncompressible = False
    prev = ''
    
    for i in string:
        if i == prev:
            uncompressible = True
            count = int(new_string[-1]) + 1
            new_string = new_string[:-1] + str(count)
        else:
            new_string += f'{i}1'
            prev = i
            
    if uncompressible:
        return new_string
    return string


print(stringCompression('abcdd'))