import image_to_latex_document

path_to_image = "src/images/FSC.PNG"

latex_doc = image_to_latex_document.image_to_latex_document(path_to_image)
with open('src/outputs/tex_image.tex', 'w+') as f:
    f.write(latex_doc)

