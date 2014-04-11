with open("./pattern") as pattern_file:
    output_file = open('pattern_convert','w')
    for row in pattern_file:
        newline = ''
        for char in row:
            if char == '.':
                newline += '0'
            else:
                newline += '1'
        while len(newline) < 100:
            newline += '0'
        output_file.write(newline + '\n')
    output_file.close()


