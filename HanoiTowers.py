import time, pygame, signal, sys
from pygame import display
from pygame import draw
from pygame import Color
from pygame import Rect

WHITE = (255, 255, 255)
BROWN = (133, 94, 66)
GREEN = (100, 200, 100)
RED = (200, 100, 100)
BLACK = (0, 0, 0)

pygame.init()
__screen = pygame.display.set_mode((640, 480))
__maxSize = max(int(sys.argv[1]), 0) if len(sys.argv) > 1 else 3
__diskHeight = min(300/max(__maxSize, 1), 50)
__sleepTime = 3.0 / max(__maxSize, 1)**2


stacks = [  [i for i in range(__maxSize,0,-1)],
            [],
            [] ]


def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    time.sleep(__sleepTime)

def drawStacks(stacks):    
    __screen.fill(Color(50,50,150,255))
    
    stackWidth = 15
    stack = Rect(0 - stackWidth/2, 90, stackWidth, 310)
    disk = None
    
    for l in stacks:
        stack.move_ip(640/4, 0)
        draw.rect(__screen, BROWN, stack)
        
        for i, disk in enumerate(l, start=1):
            diskWidth = 640/5 * (float(disk)/float(__maxSize)) + stackWidth * 2
            disk = Rect((stack.left + stackWidth/2) - diskWidth/2, 400 - __diskHeight * (i), diskWidth, __diskHeight)
            
            draw.rect(__screen, RED, disk)
            draw.rect(__screen, BLACK, disk, 2)
            disk.width /= 10
            disk.height -= 6
            disk.move_ip(diskWidth/6, 3)
            draw.rect(__screen, WHITE, disk)
            
    draw.rect(__screen, GREEN, Rect(0, 400, 640, 80))
    display.flip()
    handleEvents()

def printStacks(stacks):
    for l in stacks:
        print(l, flush=True)
    time.sleep(0.02)
    
def solve(size, frm, to, over):
    if(size == 0):
        return
    
    solve(size - 1, frm, over, to)
    
    to.append(frm.pop())
    #Stuff just happened, let's Draw
    #printStacks(stacks)
    drawStacks(stacks)
    
    solve(size - 1, over, to, frm)
    
def main():
    drawStacks(stacks)
    time.sleep(0.5)
    
    result = solve(__maxSize, stacks[0], stacks[2], stacks[1])
    
    while True:
        handleEvents()
    pygame.quit()
    exit()
    
main()