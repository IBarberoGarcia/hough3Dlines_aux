import matplotlib.pyplot as plt 
import numpy as np


def read_ply(ply_file):
    '''Gets an ASCII ply file and returns a dictionary with x,y,z,nx,ny,nz,red,green,blue, faces (the ones that are presented
    in the file. If some value is missed (eg. no normals) the dict will not have that value.'''
    properties=[]#List of property names
    with open(ply_file, 'r') as f:
        lines = f.readlines()
    j=0
    faces_num=0
    for line in lines:
        if line.startswith('element vertex'):
            verts_num = int(line.split(' ')[-1])
        elif line.startswith('element face'):
            faces_num = int(line.split(' ')[-1])
        elif line.startswith('property'):
            properties.append(line.split(' ')[-1].strip('\n'))
        elif line.startswith('end_header'):
            start_line=j+1
            break
        j+=1
    
    ply_dict={}    
    verts_lines = lines[start_line:start_line + verts_num]
    
    verts = np.array([list(map(float, l.strip().split(' '))) for l in verts_lines])
    if faces_num>0:
        faces_lines = lines[start_line + verts_num:]
        faces = np.array([list(map(int, l.strip().split(' '))) for l in faces_lines])[:,1:]
        ply_dict['faces'] = faces
        
    i=0
    while i<len(properties):
        attr=properties[i]
        if attr == "x":
            ply_dict['x'] = verts.transpose()[i]
        elif attr == "y":
            ply_dict['y'] = verts.transpose()[i]
        elif attr == "z":
            ply_dict['z'] = verts.transpose()[i]
        elif attr == "nx":
            ply_dict['nx'] = verts.transpose()[i]
        elif attr == "ny":
            ply_dict['ny'] = verts.transpose()[i]
        elif attr == "nz":
            ply_dict['nz'] = verts.transpose()[i]
        elif attr == "red":
            ply_dict['red'] = [int(num) for num in verts.transpose()[i]]
        elif attr == "green":
            ply_dict['green'] = [int(num) for num in verts.transpose()[i]]
        if attr == "blue":
            ply_dict['blue'] = [int(num) for num in verts.transpose()[i]]
        i+=1
    return ply_dict

def format_ply2hough(ply_file, out_file):
    '''Transforms an ASCII ply to the required format for using the hough algorithm.'''
    out=open(out_file, 'w')
    ply_dict = read_ply(ply_file)
    x=ply_dict['x']
    y=ply_dict['y']
    z=ply_dict['z']
    i=0
    for i in range(0,len(x)):
        out.write(str(x[i]) + ',' + str(y[i]) + ',' +  str(z[i]) + '\n')
        i+=1
    out.close()


def show_hough(hough_file, axis='xy'):
    '''Shows the lines detected by hough algorithm.
    -hough_file: output file from hough detection as in:https://github.com/cdalitz/hough-3d-lines
    using the -raw option.
    -axis:'xy','xz','yz' as the visualization is 2D'''

    h_f = open(hough_file, 'r')
    lines = h_f.readlines()
    l1 = lines[0]
    xmin = float(l1.split()[0])
    xmax = float(l1.split()[1])
    ymin = float(l1.split()[2])
    ymax = float(l1.split()[3])
    zmin = float(l1.split()[4])
    zmax = float(l1.split()[5])
    
    l2 = lines[1]
    t0 = float(l2.split()[0])
    t1 = float(l2.split()[1])
    
    with open(hough_file, 'r') as f:
        lines = f.readlines()[2:]
        j=0
        for line in lines:
            ax = float(line.split()[0])
            bx = float(line.split()[3])
            ay = float(line.split()[1])
            by = float(line.split()[4])
            az = float(line.split()[2])
            bz = float(line.split()[5])
            
            #Choose combination of axis...
            if axis=='xy':
                plt.plot([ax+t0*bx,ax+t1*bx],[ay+t0*by,ay+t1*by])
                plt.xlim([xmin, xmax])
                plt.ylim([ymin, ymax])
            elif axis=='yz':
                plt.plot([ay+t0*by,ay+t1*by],[az+t0*bz,az+t1*bz])
                plt.xlim([ymin, ymax])
                plt.ylim([zmin, zmax])
            elif axis=='xz':
                plt.plot([ax+t0*bx,ax+t1*bx],[az+t0*bz,az+t1*bz])
                plt.xlim([xmin, xmax])
                plt.ylim([zmin, zmax])
        
        
ply_file='cloud.ply' 
out_file='cloud_hough.txt'   
#Get cloud in the required format...
format_ply2hough(ply_file, out_file)
#After processing with hough, show results with matplotlib...
hough_file='outlines.dat'
show_hough(hough_file, 'xy')
