# hough3Dlines_aux

Auxiliary functions to work with Iterative Hough Transform for 3D Line Detection (https://github.com/cdalitz/hough-3d-lines)
The functions are in hough_aux.py:
- format_ply2hough: Transforms an ASCII PLY point cloud to the required format for Hough 
- show_hough: Shows detected lines. Requires the raw file given by the tool. It can be obtained with:
    hough3dlines -o outlines.dat -raw -minvotes 5000 cloud_hough.txt
 where outlines is the output file, 5000 is the minimum number of points per line an cloud_hough is the input cloud.
 
 
