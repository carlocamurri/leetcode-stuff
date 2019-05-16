def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


def generate_expectations(file_lines):
    stripped = [line.rstrip(' \n\r') for line in file_lines]
    evaluated = [eval(line) for line in stripped if line != '']
    expectations = []
    for l, k in pairwise(evaluated):
        expectations.append((l, k))
    return expectations


