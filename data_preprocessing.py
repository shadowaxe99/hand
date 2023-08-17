```python
import os
from xml.dom import minidom

class SVGData:
    def __init__(self, stroke_paths, pen_coordinates):
        self.stroke_paths = stroke_paths
        self.pen_coordinates = pen_coordinates

def preprocessSVGData(svg_file_path):
    # Parse the SVG file
    doc = minidom.parse(svg_file_path)
    path_strings = [path.getAttribute('d') for path in doc.getElementsByTagName('path')]
    doc.unlink()

    # Extract stroke paths and pen coordinates
    stroke_paths = []
    pen_coordinates = []
    for path_string in path_strings:
        path_data = path_string.strip().split(' ')
        stroke_paths.append(path_data)
        pen_coordinates.append((float(path_data[1]), float(path_data[2])))

    return SVGData(stroke_paths, pen_coordinates)

# Process all SVG files in the given directory
def process_all_SVG_files(directory):
    processedSVGData = []
    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            svg_data = preprocessSVGData(os.path.join(directory, filename))
            processedSVGData.append(svg_data)
    return processedSVGData

# Example usage:
# processedSVGData = process_all_SVG_files('/path/to/svg/files')
```