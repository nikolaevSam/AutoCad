from utils import config;
from scripts import LoadDXF;

source_dxf = LoadDXF.load_source(config.source_path)

HTRDATA01 = source_dxf.blocks.get('LYNX_EUR_TRACEDATA01')
BRD = source_dxf.blocks.get('EUR_BDR_A1_LYNX')

dwgBlocks = {
    HTRDATA01,
    BRD,
}