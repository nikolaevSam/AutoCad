import os
def save_drawing(drawing, file_name):
    # os.mkdir(file_name)
    drawing.saveas(file_name + '.dxf')