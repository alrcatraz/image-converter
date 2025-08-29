#!/usr/bin/env python3
"""
SVG到EPS矢量转换工具
支持多种转换方法
"""

import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="矢量SVG到矢量EPS转换工具")
    parser.add_argument("input", help="输入SVG文件或目录")
    parser.add_argument("-o", "--output", help="输出目录", default="./eps_output")
    parser.add_argument("-m", "--method", choices=["inkscape", "cairo"], 
                       default="inkscape", help="转换方法")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"错误: 输入路径不存在 {args.input}")
        sys.exit(1)
    
    output_path.mkdir(exist_ok=True)
    
    if input_path.is_file():
        # 单个文件转换
        if args.method == "inkscape":
            from converters.inkscape_converter import convert_single_file
        else:
            from converters.cairo_converter import convert_single_file
        
        success = convert_single_file(input_path, output_path / f"{input_path.stem}.eps")
        print("✓ 成功" if success else "✗ 失败")
        
    else:
        # 批量转换
        if args.method == "inkscape":
            from converters.inkscape_converter import batch_convert
        else:
            from converters.cairo_converter import batch_convert
        
        batch_convert(input_path, output_path)

if __name__ == "__main__":
    main()
