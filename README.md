# hough3Dlines_aux

Auxiliary functions to work with Iterative Hough Transform for 3D Line Detection (https://github.com/cdalitz/hough-3d-lines)
The functions are in hough_aux.py:
- format_ply2hough: Transforms an ASCII PLY point cloud to the required format for Hough 
- show_hough: Gets the raw file and creates a ply of the result. 

- get_lines: The whole proccess, transforms ply to hough format txt, call the hough exe and generates the results ply.
 Any changes in the hough parameters have to be made on 'cmd'
