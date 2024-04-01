from scripts import CreateDXF, SaveDXF, BlockDXF;
from utils import config;

drawing_dxf = CreateDXF.create_drawing(config.drawing_type)

BlockDXF.block_import(source_dxf, drawing_dxf, 'EUR_BDR_A1_LYNX')

BlockDXF.add_block(drawing_dxf, 'EUR_BDR_A1_LYNX', 0, 0)

SaveDXF.save_drawing(drawing_dxf, config.file_name)
