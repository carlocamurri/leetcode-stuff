def convert(name):
    words = name.split('_')
    capitalized = map(lambda x: x.capitalize(), words)
    return ''.join(capitalized)
