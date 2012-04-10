#!/usr/bin/env python
#coding:utf-8
# Author:  brobey

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/svgwrite'))

import svgwrite
from svgwrite import cm, mm   
    
if __name__ == '__main__':
    xmult   = 200.0
    ymult   = 200.0

    xlast = 0.0
    ylast = 0.0
    dwg = svgwrite.Drawing(filename="graphics.svg", debug=True, height=1000, width=1000)
    for line in open('rundata'):
       ar = line.split()
       if len(ar) == 0:
          break
       if ar[0] == "viewport":
          x1 = float(ar[1])*xmult
          y1 = float(ar[2])*ymult
          x2 = float(ar[3])*xmult
          y2 = float(ar[4])*ymult
          dwg.viewbox(minx=x1-20.0,miny=y1-20.0,width=(x2-x1)+40.0,height=(y2-y1)+40.0)
       if ar[0] == "rect":
          x1 = float(ar[1])*xmult
          y1 = float(ar[2])*ymult

          x2 = float(ar[3])*xmult
          y2 = float(ar[4])*ymult
          width  = x2-x1
          height = y2-y1
          #print "rect", x1, y1, x2, y2, width, height
          dwg.add( dwg.rect( insert=(x1, y1), size=(width, height), stroke='black', stroke_width=2, fill='white' ) )
       if ar[0] == "polygon4":
          x1 = float(ar[1])*xmult
          y1 = float(ar[2])*ymult

          x2 = float(ar[3])*xmult
          y2 = float(ar[4])*ymult

          x3 = float(ar[5])*xmult
          y3 = float(ar[6])*ymult

          x4 = float(ar[7])*xmult
          y4 = float(ar[8])*ymult

          print "polygon", x1, y1, x2, y2, x3, y3, x4, y4
          dwg.add( dwg.polygon( points=[(x1, y1), (x2, y2), (x3, y3), (x4, y4)], stroke='red', stroke_width=3, fill='white' ) )
       if ar[0] == "line_init":
          xlast = float(ar[1])*xmult
          ylast = float(ar[2])*ymult
       if ar[0] == "line":
          x1 = float(ar[1])*xmult
          y1 = float(ar[2])*ymult
          dwg.add(dwg.line( (xlast,ylast), (x1,y1), stroke='blue' ) )
          xlast = x1
          ylast = y1
       if ar[0] == "text":
          x1 = float(ar[1])*xmult
          y1 = float(ar[2])*ymult
          dwg.add(dwg.text( ar[3], insert=(x1,y1), stroke='black', font_size=18) )
    dwg.save()
  
