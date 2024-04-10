from scripts import CreateDXF, SaveDXF, BlockDXF, LoadDXF;
from utils import config;
from utils import blocks;

dwgName = ['one', 'two', 'three']

for i in dwgName:
    drawing_dxf = CreateDXF.create_drawing(config.drawing_type)
    BlockDXF.block_import(LoadDXF.source_dxf, drawing_dxf, blocks.LYNX_EUR_BRD_SATMP['EUR_BDR_A1_LYNX'])
    BlockDXF.add_block(drawing_dxf, blocks.LYNX_EUR_BRD_SATMP['EUR_BDR_A1_LYNX'], 0, 0)
    SaveDXF.save_drawing(drawing_dxf, i)



# def createDrawing(drawing_type):
#     return CreateDXF.create_drawing(drawing_type)

# drawing_dxf = createDrawing(config.drawing_type)



# SaveDXF.save_drawing(drawing_dxf, config.file_name) # change file_name to current dwg name
