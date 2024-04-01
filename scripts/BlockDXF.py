from ezdxf.addons import Importer

def block_import(source, drawing, block):
    importer = Importer(source, drawing)
    importer.import_block(block)
    importer.finalize()

def add_block(drawing, block, x, y):
    msp = drawing.modelspace()
    msp.add_blockref(block, insert=(x,y))