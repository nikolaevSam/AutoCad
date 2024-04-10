from utils import config
import sys
import ezdxf

def load_source(path): 
    try:
        source_dxf = ezdxf.readfile(path)
    except IOError:
        print('Not a DXF file or a generic I/O error')
        sys.exit(1)
    except ezdxf.DXFStructureError:
        print('Invalid or corrupted DXF file')
        sys.exit(2)
    return source_dxf

source_dxf = load_source(config.source_path)