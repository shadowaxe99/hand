```python
import numpy as np
from data_preprocessing import SVGData, processedSVGData

class Features:
    def __init__(self, stroke_shapes, pen_pressure, slant, curvature):
        self.stroke_shapes = stroke_shapes
        self.pen_pressure = pen_pressure
        self.slant = slant
        self.curvature = curvature

def extractFeatures(svg_data):
    # Placeholder functions for feature extraction
    def extract_stroke_shapes(svg_data):
        # Analyze stroke paths to determine stroke shapes
        pass

    def extract_pen_pressure(svg_data):
        # Analyze pen coordinates to determine pen pressure
        pass

    def extract_slant(svg_data):
        # Analyze stroke paths to determine slant
        pass

    def extract_curvature(svg_data):
        # Analyze stroke paths to determine curvature
        pass

    stroke_shapes = extract_stroke_shapes(svg_data)
    pen_pressure = extract_pen_pressure(svg_data)
    slant = extract_slant(svg_data)
    curvature = extract_curvature(svg_data)

    return Features(stroke_shapes, pen_pressure, slant, curvature)

extractedFeatures = extractFeatures(processedSVGData)

# Send a message that the features have been extracted
print("FeaturesExtracted")
```