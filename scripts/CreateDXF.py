import ezdxf

def create_drawing(drawing_type):
    drawing_dxf = ezdxf.new(drawing_type)
    return drawing_dxf