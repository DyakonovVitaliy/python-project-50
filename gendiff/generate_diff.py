from gendiff.create_diff_files import generate_diff_list
from gendiff.define_extension import split_filename
from gendiff.open_file import open_file
from gendiff.formaters.stylish import render_stylish
from gendiff.formaters.plain import render_plain
from gendiff.formaters.json import render_json


def generate_diff(file1, file2, formater='stylish'):
    data1, extension1 = split_filename(file1)
    data2, extension2 = split_filename(file2)
    parsed_file1 = open_file(data1, extension1)
    parsed_file2 = open_file(data2, extension2)
    result_list = generate_diff_list(parsed_file1, parsed_file2)
    if formater == 'stylish':
        return render_stylish(result_list)
    if formater == 'plain':
        return render_plain(result_list)
    if formater == 'json':
        return render_json(result_list)
