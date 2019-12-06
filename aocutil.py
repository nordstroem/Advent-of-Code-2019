def read_lines(path, fun=lambda x: x):
    with open(path,'r') as inp:
        lines = inp.readlines()
        return [fun(l.strip()) for l in lines]

def read_file(path):
    with open(path,'r') as inp:
        return inp.read()
