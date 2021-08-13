"""1.Line Segment Information.
    This program allows the user to draw a line segment and then displays some graphical
    and textual information about the line segment.
    Input: Two mouse clicks for the end points of the line segment.
    Output: Draw the midpoint of the segment in cyan. Draw the line.
            Print the length and the slope of the line.
    Formulas: dx = x2 - x1
              dy = Y2 - Yl
              slope = dy / dx
              length = J dx2 + dy2
"""

import pygame
import sys
from pygame import display, draw, mouse
#print(help(display))

window1 = display.set_mode((500, 500))
window1.fill('black')
display.set_caption("Line Length, Center & Slope Finder.")


line = []

while True:
    pygame.time.delay(10)
    tmp = pygame.event.get()
    for env in tmp:
        if env.type == pygame.MOUSEBUTTONDOWN:
            but = mouse.get_pressed()
            a = mouse.get_pos()
            if but[0]:
                line.append(a)
                print(line)

            elif but[2]:
                window1.fill('black')
                display.set_caption("Line Length, Center & Slope Finder.")
                display.update()
                line = []

            else:
                pass

        if env.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if len(line) == 2:
        x1, y1 = line[0]
        x2, y2 = line[1]
        length = ((x2-x1)**2+(y2-y1)**2)**(1/2)
        mid = [(x2+x1)//2, (y2+y1)//2]
        mid2 = [(x2+x1)/2, (y2+y1)/2]
        slope = (y2-y1)/(x2-x1)
        for i in range(2):
            if mid[i] < 0:
                mid[i] *= -1
        if slope < 0:
            slope *= -1
        draw.line(window1, "red", start_pos=line[0], end_pos=line[1])
        window1.set_at(mid, 'cyan')
        display.set_caption(f"Length: {str(length)[0:6]} pixels; Center: {mid2} ; Slope: {str(slope)[0:4]}")
        print(f"Length: {length} pixels; Center: {mid2} ; Slope: {slope}")
        line = []
        display.update()

