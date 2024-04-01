import sys
import ezdxf

def load_source(source_path): 
    try:
        source_dxf = ezdxf.readfile(source_path)
    except IOError:
        print('Not a DXF file or a generic I/O error')
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print('Invalid or corrupted DXF file')
        sys.exit(2)
    return source_dxf