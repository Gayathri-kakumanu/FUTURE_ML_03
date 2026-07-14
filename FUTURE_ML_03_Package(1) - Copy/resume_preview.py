import fitz

def show_resume(uploaded_file):

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    pages = []

    for page in pdf:
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        pages.append(pix)

    return pages