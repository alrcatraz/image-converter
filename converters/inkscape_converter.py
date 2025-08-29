"""Inkscape矢量转换器"""
import subprocess
from pathlib import Path

def convert_single_file(svg_path, eps_path):
    """转换单个文件"""
    try:
        cmd = [
            "inkscape",
            str(svg_path),
            "--export-filename", str(eps_path),
            "--export-type=eps",
            "--export-text-to-path",
            "--export-ps-level=3",
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return result.returncode == 0
    except Exception:
        return False

def batch_convert(input_dir, output_dir):
    """批量转换"""
    svg_files = list(Path(input_dir).glob("*.svg"))
    
    for svg_file in svg_files:
        eps_file = output_dir / f"{svg_file.stem}.eps"
        success = convert_single_file(svg_file, eps_file)
        print(f"{'✓' if success else '✗'} {svg_file.name}")
