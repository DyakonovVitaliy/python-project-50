from os.path import splitext

EXTENSION = ('json', 'yml', 'yaml')


def return_content_and_extension(file):
    extension = splitext(file)[1][1:]
    if extension in EXTENSION:
        with open(file) as f:
            data = f.read()
            return data, extension
