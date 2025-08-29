"""CairoSVG转换器"""
try:
    import cairosvg
except ImportError:
    cairosvg = None

from pathlib import Path

def convert_single_file(svg_path, eps_path):
    """转换单个文件"""
    if cairosvg is None:
        print("错误: cairosvg未安装，请运行: uv add cairosvg")
        return False
    
    try:
        cairosvg.svg2eps(url=str(svg_path), write_to=str(eps_path))
        return True
    except Exception:
        return False

def batch_convert(input_dir, output_dir):
    """批量转换"""
    if cairosvg is None:
        print("错误: cairosvg未安装")
        return
    
    svg_files = list(Path(input_dir).glob("*.svg"))
    
    for svg_file in svg_files:
        eps_file = output_dir / f"{svg_file.stem}.eps"
        success = convert_single_file(svg_file, eps_file)
        print(f"{'✓' if success else '✗'} {svg_file.name}")
