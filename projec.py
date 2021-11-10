def swaptxt():
    file1 = input('entir the file name or perish')
    file2 = input('entire the 2nd file name or perish')
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)
    
swaptxt()