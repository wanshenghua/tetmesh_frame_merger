#python3
#File name: tetmesh_frame_merger.py
#Description: 
#   given a tetmesh file and its frame file provided by Dr. Yang Liu, merge them into one file so that the frames become traits of each tet.

from __future__ import print_function
import sys

def help():
    print('Tet-mesh and frames merger to merge .tm and .frame to .tm format.')
    print('Ver 0.01 Build 20130421')
    print('Author: Shenghua Wan @ Louisiana State University')
    print("Contact: wanshenghua 'at' gmail 'dot' com")
    print()
    print('Format: tetmesh_frame_merger.py tmesh.tm tmesh.frame > merged.tm')

#main function
tmesh_file_name = ''
frame_file_name = ''
if len(sys.argv) != 3 :
    help()
    sys.exit(-1)
else :
    tmesh_file_name = sys.argv[1]
    frame_file_name = sys.argv[2]

#read the tet-mesh file
tmesh_contents = ''
with open(tmesh_file_name, 'r') as f:
    tmesh_contents = f.readlines()

#read the frame files
frame_contents = ''
with open(frame_file_name, 'r') as f:
    frame_contents = f.readlines()

#print vertex lines
tet_id = 0
for line in tmesh_contents:
    if line[:6] == 'Vertex':
        print(line, end='')
    elif line[:11] == 'Tetrahedron':
        line = line.rstrip(); #remove trailing whitespace, including newline
        matrix = frame_contents[tet_id].split()
        #check if other traits exist
        if line.find('{') == -1: #not exist
            print(line + ' {VF0=(' + matrix[0] + ' ' + matrix[1] + ' ' + matrix[2] + ') VF1=(' + matrix[3] + ' ' + matrix[4] + ' ' + matrix[5] + ') VF2=(' + matrix[6] + ' ' + matrix[7] + ' ' + matrix[8] + ')}')
        else : #exist
            line_split = line.split('{')
            print(line_split[0] + ' {VF0=(' + matrix[0] + ' ' + matrix[1] + ' ' + matrix[2] + ') VF1=(' + matrix[3] + ' ' + matrix[4] + ' ' + matrix[5] + ') VF2=(' + matrix[6] + ' ' + matrix[7] + ' ' + matrix[8] + ') ' + line_split[1])
        tet_id += 1

#end
