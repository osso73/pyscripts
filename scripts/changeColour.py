#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 19/03/2020 09:13

changeColour.py - replace a colour by another on an image
       
@author: opujo
"""

import os, argparse, sys
from PIL import Image, ImageColor


def exit_error(string):
    print(string)
    print("Type 'changeColour --help' for information on usage.")
    exit(0)

def get_colours(sysarg, args):
    order = list()
    for elm in sysarg:
        if elm.startswith('-n') or elm.startswith('--n'):
            order.append('name')
        elif elm.startswith('-'):
            order.append(elm[1:])
    
    assert len(order) == 2, f'Number of colours incorrect! {order}'
    
    #colour1
    if order[0] == 'rgb':
        colour1 = tuple(args.rgb[0] + [255])
    elif order[0] == 'rgba':
        colour1 = tuple(args.rgba[0])
    else:
        if args.name[0].lower() == 'transparent':
            colour1 == (0, 0, 0, 0)
        else:
            colour1 = ImageColor.getcolor(args.name[0], 'RGBA')
    
    #colour2
    if order[1] == 'rgb':
        if order[0] == 'rgb':
            colour2 = tuple(args.rgb[1] + [255])
        else:
            colour2 = tuple(args.rgb[0] + [255])
    elif order[1] == 'rgba':
        if order[0] == 'rgba':
            colour2 = tuple(args.rgba[1])
        else:
            colour2 = tuple(args.rgba[0])
    else:
        if order[0] == 'name':
            if args.name[1].lower() == 'transparent':
                colour2 = (0, 0, 255, 0)
            else:
                colour2 = ImageColor.getcolor(args.name[1], 'RGBA')
        else:
            if args.name[0].lower() == 'transparent':
                colour2 = (255, 0, 255, 128)
            else:
                colour2 = ImageColor.getcolor(args.name[0], 'RGBA')            
    
    return colour1, colour2


#get arguments
desc = 'replace a colour by another on an image'
epi= 'You need to provide two arguments: the first one is the colour you \
want to change, and the second one is the new colour. Each colour can be \
described as an RGB, RGBA or by name. Use "transparent" as a name for \
transparent. The output file will be on .png.'
parser = argparse.ArgumentParser(description=desc, epilog=epi, argument_default=[])

parser.add_argument("image", help="Filename of the image, including path \
                    if it is in a different folder than current.")
parser.add_argument("-rgb", help="Colour represented by 3 values, from 0 to \
                    255", nargs=3, action='append', type=int, 
                    metavar=('R#', 'G#', 'B#'))
parser.add_argument("-rgba", help="Colour represented by 4 values, from 0 to \
                    255, the last one representing the transparency.", 
                    nargs=4, action='append', type=int, 
                    metavar=('R#', 'G#', 'B#', 'A#'))
parser.add_argument('-n', '--name', help='Colour represented by name, such as \
                    cyan, blue, or olive.', action='append')

args = parser.parse_args()

# get colours from arguments
if len(args.rgb) + len(args.rgba) + len(args.name) != 2:
    exit_error("Please provide 2 colours.")

original, final = get_colours(sys.argv, args)

# open image and replace
im = Image.open(args.image).convert('RGBA')
width, height = im.size

for x in range(width):
    for y in range(height):
        if im.getpixel((x, y)) == original:
            im.putpixel((x, y), final)

# save new image

base, ext = os.path.splitext(args.image)
newname = base + "_new.png"
im.save(newname)
