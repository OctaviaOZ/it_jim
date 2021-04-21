[corr2D_image.py](/corr2D_image.py)

A simple 2D correlation function on your own using only numpy, but basic math only. Do calculations in float.
Input: two grayscale images. Output: *.png file with a correlation image.

[detect_object.py](/detect_object.py)

From set of images with blobs (binary large objects)
represented by black spots the function that detects (finds xmin, xmax, ymin, ymax
of) black spots on these images. This function also visualizes
results by surrounding each spot (blob) with a red rectangle.
The input of the function is the path to the folder with images.
The first output is a list of dicts like this:
[{'file': SR1.png, 'coords': [left,right,top,bottom]}, ...]
Second output: *.png files with a visualization of results.
