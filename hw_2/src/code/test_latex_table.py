import list_of_lists_to_latex_document
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

latex_table = list_of_lists_to_latex_document.list_of_lists_to_latex_document(data)


with open('src/outputs/tex_table.tex', 'w+') as f:
    f.write(latex_table)
