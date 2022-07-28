import os

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new_lines = []
    for line in lines:
        if line == "Allen" :
            person = line
            continue
        elif line == "Tom" :
            person = line
            continue
        new_lines.append(person + ',' + line)
    return new_lines

def write_file(output_filename,lines):
    with open(output_filename, 'w', encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')



def main():
    filename = "input.txt"
    output_filename = "output2.txt"
    lines = read_file(filename)
    new_lines = convert(lines)
    print(new_lines)
    write_file(output_filename,new_lines)
    return new_lines
    

main()

