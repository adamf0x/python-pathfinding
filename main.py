# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sys
import time

import pygame
from pygame.locals import *

from operator import *

def aStar(nodes, startNode, endNode, dimensions, drawnNodes):
    searched = []
    path = []
    start = GraphNode(startNode)
    openSet = []
    closedSet = {}
    complete = False
    for i in nodes:
        closedSet[i] = False
    heapq.heappush(openSet, start)
    while openSet:
        currentNode = heapq.heappop(openSet)
        walkableNodes = []
        curr = currentNode.coords
        if curr[0] > 0 and drawnNodes[(curr[0] - 1, curr[1])] != 1:
            walkableNodes.append((curr[0] - 1, curr[1]))
        if curr[1] > 3 and drawnNodes[(curr[0], curr[1] - 1)] != 1:
            walkableNodes.append((curr[0], curr[1] - 1))
        if curr[0] < dimensions[0] and drawnNodes[(curr[0] + 1, curr[1])] != 1:
            walkableNodes.append((curr[0] + 1, curr[1]))
        if curr[1] < dimensions[1] and drawnNodes[(curr[0], curr[1] + 1)] != 1:
            walkableNodes.append((curr[0], curr[1] + 1))
        if curr[0] > 0 and curr[1] > 3 and drawnNodes[(curr[0] - 1, curr[1] - 1)] != 1:
            walkableNodes.append((curr[0] - 1, curr[1] - 1))
        if curr[0] < dimensions[0] and curr[1] < dimensions[1] and drawnNodes[(curr[0] + 1, curr[1] + 1)] != 1:
            walkableNodes.append((curr[0] + 1, curr[1] + 1))
        if curr[0] > 0 and curr[1] < dimensions[1] and drawnNodes[(curr[0] - 1, curr[1] + 1)] != 1:
            walkableNodes.append((curr[0] - 1, curr[1] + 1))
        if curr[0] < dimensions[0] and curr[1] > 3 and drawnNodes[(curr[0] + 1, curr[1] - 1)] != 1:
            walkableNodes.append((curr[0] + 1, curr[1] - 1))
        for i in walkableNodes:
            node = GraphNode(i)
            node.parent = currentNode
            if node.coords == endNode:
                complete = True
                path.append(currentNode.coords)
                return searched, node
            node.gScore = currentNode.gScore + 1
            node.hScore = abs(node.coords[0] - endNode[0]) + abs(node.coords[1] - endNode[1])
            node.fScore = node.gScore + node.hScore
            if closedSet[node.coords] == False:
                nodeInOpen = False
                for j in openSet:
                    if j.coords == node.coords:
                        nodeInOpen = True
                        if j.fScore < node.fScore:
                            break
                        else:
                            j.fScore = node.fScore
                if nodeInOpen is False:
                    heapq.heappush(openSet, node)
                if node.coords not in searched:
                    searched.append(node.coords)
        closedSet[currentNode.coords] = True

    if complete == False:
        return [], []
    return searched, path
def dijkstras(nodes, startNode, endNode, dimensions, drawnNodes):
    shortestPathNodes = {}
    incompleteNodes = nodes
    for i in incompleteNodes:
        incompleteNodes[i] = {'distanceFromStart': float('inf'), 'prevNode': None}
    incompleteNodes[startNode]['distanceFromStart'] = 0
    while len(list(shortestPathNodes.keys())) != len(list(incompleteNodes.keys())):
        sortedList = sorted(incompleteNodes.items(), key=lambda item: item[1]['distanceFromStart'])
        incompleteNodes = {}
        for item in sortedList:
            incompleteNodes[item[0]] = item[1]
        for j in list(incompleteNodes.keys()):
            if incompleteNodes[j]['distanceFromStart'] == float('inf'):
                return
            if j not in shortestPathNodes:
                curr = j
                break
        if curr == endNode:
            shortestPathNodes[curr] = incompleteNodes[curr]
            return shortestPathNodes
        walkableNodes = []
        if curr[0] > 0 and drawnNodes[(curr[0]-1, curr[1])] != 1:
            walkableNodes.append((curr[0]-1, curr[1]))
        if curr[1] > 3 and drawnNodes[(curr[0], curr[1]-1)] != 1:
            walkableNodes.append((curr[0], curr[1]-1))
        if curr[0] < dimensions[0] and drawnNodes[(curr[0]+1, curr[1])] != 1:
            walkableNodes.append((curr[0]+1, curr[1]))
        if curr[1] < dimensions[1] and drawnNodes[(curr[0], curr[1]+1)] != 1:
            walkableNodes.append((curr[0], curr[1]+1))    
        if curr[0] > 0 and curr[1] > 3 and drawnNodes[(curr[0]-1, curr[1]-1)] != 1:
            walkableNodes.append((curr[0]-1, curr[1]-1))
        if curr[0] < dimensions[0] and curr[1] < dimensions[1] and drawnNodes[(curr[0]+1, curr[1]+1)] != 1:    
            walkableNodes.append((curr[0]+1, curr[1]+1))
        if curr[0] > 0 and curr[1] < dimensions[1] and drawnNodes[(curr[0]-1, curr[1]+1)] != 1:
            walkableNodes.append((curr[0]-1, curr[1]+1))
        if curr[0] < dimensions[0] and curr[1] > 3 and drawnNodes[(curr[0]+1, curr[1]-1)] != 1:
            walkableNodes.append((curr[0]+1, curr[1]-1))
        for node in walkableNodes:
            if node in shortestPathNodes:
                walkableNodes.remove(node)
       
        for node in walkableNodes:
            if node[1] == curr[1] or node[0] == curr[0]:
                if incompleteNodes[node]['distanceFromStart'] > incompleteNodes[curr]['distanceFromStart'] + 1:
                    incompleteNodes[node] = {'distanceFromStart': incompleteNodes[curr]['distanceFromStart'] + 1,'prevNode': curr}
            else:
                if incompleteNodes[node]['distanceFromStart'] > incompleteNodes[curr]['distanceFromStart'] + 2:
                    incompleteNodes[node] = {'distanceFromStart': incompleteNodes[curr]['distanceFromStart'] + 2,'prevNode': curr}
        shortestPathNodes[curr] = incompleteNodes[curr]
    return shortestPathNodes
        
if __name__ == "__main__":
    windowSize = width, height = (500, 500)
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode(windowSize,
                                 pygame.RESIZABLE)
    nodes = {}
    oldWindowSize = [pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]]
    drawnNodes = {}
    cellSize = 20
    maxScreenWidth = pygame.display.get_window_size()[0]
    maxScreenHeight = pygame.display.get_window_size()[1]
    drawnNodes[(0, 3)] = 2
    drawnNodes[(int(maxScreenWidth / cellSize) - 1, int(maxScreenHeight / cellSize) - 1)] = 3
    startIndex = (0,3)
    endIndex = ((int(maxScreenWidth / cellSize) - 1, int(maxScreenHeight / cellSize) - 1))
    screenSizeChange = True
    placeStart = False
    placeEnd = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            maxScreenWidth = pygame.display.get_window_size()[0]
            maxScreenHeight = pygame.display.get_window_size()[1]
            screen.fill((0, 0, 0))
            widthOffsetToCenter = 0
            if pygame.display.get_window_size()[0] % cellSize != 0:
                maxScreenWidth = pygame.display.get_window_size()[0] - pygame.display.get_window_size()[0] % cellSize
                while maxScreenWidth % cellSize != 0:
                    maxScreenWidth = pygame.display.get_window_size()[0] - pygame.display.get_window_size()[0] % cellSize
                widthOffsetToCenter = pygame.display.get_window_size()[0] % cellSize/2
            if pygame.display.get_window_size()[1] % cellSize != 0:
                maxScreenHeight = pygame.display.get_window_size()[1] - pygame.display.get_window_size()[1] % cellSize
                while maxScreenHeight % cellSize != 0:
                    maxScreenHeight = pygame.display.get_window_size()[1] - pygame.display.get_window_size()[1] % cellSize
            if event.type == VIDEORESIZE:
                if endIndex[0] > int(maxScreenWidth/cellSize) - 1:
                    print(endIndex, int(maxScreenWidth/cellSize), int(maxScreenHeight/cellSize))
                    drawnNodes[endIndex] = 0
                    endIndex = (int(maxScreenWidth/cellSize) - 1, endIndex[1])
                if endIndex[1] > int(maxScreenHeight/cellSize) - 1:
                    drawnNodes[endIndex] = 0
                    endIndex = (endIndex[0], int(maxScreenHeight/cellSize) - 1)
                print(endIndex, int(maxScreenWidth / cellSize), int(maxScreenHeight / cellSize))
                drawnNodes[endIndex] = 3
            nodes = {}
            for i in range(0, maxScreenWidth, cellSize):
                for j in range(60, maxScreenHeight, cellSize):
                    if (int(i / cellSize), int(j / cellSize)) not in drawnNodes:
                        drawnNodes[(int(i/ cellSize), int(j / cellSize))] = 0
                    if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 0:
                        rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize-2, cellSize-2))
                        pygame.draw.rect(screen, (255, 255, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                    elif drawnNodes[(int(i / cellSize), int(j / cellSize))] == 1:
                        rect = pygame.rect.Rect((i+ widthOffsetToCenter, j), (cellSize-2, cellSize-2))
                        pygame.draw.rect(screen, (128, 128, 128), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                    if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 2:
                        rect = pygame.rect.Rect((i+ widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (0,255,0), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                    if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 3:
                        rect = pygame.rect.Rect((i+ widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (255,0,0), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                    if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 4:
                        rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (0, 255, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                    if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 5:
                        rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (255, 0, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect

            visualizeButton = pygame.rect.Rect((int(pygame.display.get_window_size()[0] / 2) - 50, 10), (100, 30))
            pygame.draw.rect(screen, (70, 40, 100), visualizeButton)
            font = pygame.font.SysFont(None, 14)
            img = font.render('Click To', True, (225, 255, 255))
            img2 = font.render('Visualize Dijkstras', True, (225, 255, 255))
            screen.blit(img, (int(visualizeButton.x) + int(visualizeButton.width / 2) - 35,
                              int(visualizeButton.y) + int(visualizeButton.height / 2) - 12))
            screen.blit(img2, (int(visualizeButton.x) + int(visualizeButton.width / 2) - 35,
                               int(visualizeButton.y) + int(visualizeButton.height / 2)))

            clearButton = pygame.rect.Rect((int(pygame.display.get_window_size()[0] / 2) - 200, 10), (100, 30))
            pygame.draw.rect(screen, (70, 40, 100), clearButton)
            font = pygame.font.SysFont(None, 14)
            img = font.render('Click To Reset', True, (225, 255, 255))
            screen.blit(img, (int(clearButton.x) + int(clearButton.width / 2) - 35,
                              int(clearButton.y) + int(clearButton.height / 2) - 12))

            aStarButton = pygame.rect.Rect((int(pygame.display.get_window_size()[0] / 2) + 100, 10), (100, 30))
            pygame.draw.rect(screen, (70, 40, 100), aStarButton)
            font = pygame.font.SysFont(None, 14)
            img = font.render('Click To', True, (225, 255, 255))
            img2 = font.render('Visualize A*', True, (225, 255, 255))
            screen.blit(img, (int(aStarButton .x) + int(aStarButton .width / 2) - 35,
                              int(aStarButton .y) + int(aStarButton .height / 2) - 12))
            screen.blit(img2, (int(aStarButton .x) + int(aStarButton .width / 2) - 35,
                              int(aStarButton .y) + int(aStarButton .height / 2)))
            if (clearButton.x <= pygame.mouse.get_pos()[0] <= (
                    clearButton.x + clearButton.width) and clearButton.y <= pygame.mouse.get_pos()[1] <= (
                        clearButton.y + clearButton.height)) and event.type == MOUSEBUTTONUP:
                for i in range(0, maxScreenWidth, cellSize):
                    for j in range(60, maxScreenHeight, cellSize):
                        if drawnNodes[(int(i / cellSize), int(j / cellSize))] != 2 and drawnNodes[(int(i / cellSize), int(j / cellSize))] != 3:
                            rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                            pygame.draw.rect(screen, (255, 255, 255), rect)
                            nodes[(int(i / cellSize), int(j / cellSize))] = rect
                            drawnNodes[(int(i / cellSize), int(j / cellSize))] = 0
            if (aStarButton.x <= pygame.mouse.get_pos()[0] <= (
                    aStarButton.x + aStarButton.width) and aStarButton.y <= pygame.mouse.get_pos()[1] <= (
                        aStarButton.y + aStarButton.height)) and event.type == MOUSEBUTTONUP:
                for i in range(0, maxScreenWidth, cellSize):
                    for j in range(60, maxScreenHeight, cellSize):
                        if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 4 or drawnNodes[(int(i / cellSize), int(j / cellSize))] == 5:
                            rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                            pygame.draw.rect(screen, (255, 255, 255), rect)
                            nodes[(int(i / cellSize), int(j / cellSize))] = rect
                            drawnNodes[(int(i / cellSize), int(j / cellSize))] = 0
                searched, endNode = aStar(nodes, startIndex, endIndex, ((int(maxScreenWidth/cellSize))-1, int(maxScreenHeight/cellSize)-1), drawnNodes)
                if (searched, endNode) == ([], []):
                    aStarButton = pygame.rect.Rect((maxScreenWidth / 2 - 140, maxScreenHeight / 2 - 10),
                                                       (280, 30))
                    pygame.draw.rect(screen, (255, 255, 255), aStarButton)
                    font = pygame.font.SysFont(None, 30)
                    img = font.render('End node could not be found', True, (255, 0, 0))
                    screen.blit(img, (maxScreenWidth / 2 - 140,
                                      maxScreenHeight / 2))
                    pygame.display.flip()
                    time.sleep(2)
                    continue

                for node in searched:
                    if node in drawnNodes and drawnNodes[node] != 2 and drawnNodes[node] != 3:
                        drawnNodes[node] = 4
                        rect = pygame.rect.Rect((20 * node[0] + widthOffsetToCenter, 20 * node[1]),
                                                (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (255, 255, 0), rect)
                        pygame.display.flip()
                        time.sleep(0.01)
                        pygame.draw.rect(screen, (0, 255, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                        pygame.display.flip()
                        time.sleep(0.01)
                path = []
                currNode = endNode
                path.append(currNode.coords)
                while currNode is not None:
                    path.append(currNode.coords)
                    currNode = currNode.parent
                for node in path:
                    if node in drawnNodes and drawnNodes[node] != 2 and drawnNodes[node] != 3:
                        drawnNodes[node] = 5
                        rect = pygame.rect.Rect((20*node[0] + widthOffsetToCenter, 20*node[1]), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (255, 0, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                        pygame.display.flip()
                        time.sleep(0.05)
            if (visualizeButton.x <= pygame.mouse.get_pos()[0] <= (visualizeButton.x + visualizeButton.width) and visualizeButton.y <= pygame.mouse.get_pos()[1] <= (visualizeButton.y + visualizeButton.height)) and event.type==MOUSEBUTTONUP:
                for i in range(0, maxScreenWidth, cellSize):
                    for j in range(60, maxScreenHeight, cellSize):
                        if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 4 or drawnNodes[(int(i / cellSize), int(j / cellSize))] == 5:
                            rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                            pygame.draw.rect(screen, (255, 255, 255), rect)
                            nodes[(int(i / cellSize), int(j / cellSize))] = rect
                            drawnNodes[(int(i / cellSize), int(j / cellSize))] = 0
                shortestPathNodes = dijkstras(nodes, startIndex, endIndex, ((int(maxScreenWidth/cellSize))-1, int(maxScreenHeight/cellSize)-1), drawnNodes)
                if not shortestPathNodes:
                    visualizeButton = pygame.rect.Rect((maxScreenWidth/2 - 140, maxScreenHeight/2 - 10),
                                                       (280, 30))
                    pygame.draw.rect(screen, (255, 255, 255), visualizeButton)
                    font = pygame.font.SysFont(None, 30)
                    img = font.render('End node could not be found', True, (255, 0, 0))
                    screen.blit(img, (maxScreenWidth/2 - 140,
                                      maxScreenHeight/2))
                    pygame.display.flip()
                    time.sleep(2)
                    continue
                for node in shortestPathNodes:
                    if node in drawnNodes and drawnNodes[node] != 2 and drawnNodes[node] != 3:
                        drawnNodes[node] = 4
                        rect = pygame.rect.Rect((20*node[0] + widthOffsetToCenter, 20*node[1]), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (0, 255, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                        pygame.display.flip()
                        time.sleep(0.005)
                pathNode = endIndex
                while pathNode != None:
                    if drawnNodes[pathNode] != 2 and drawnNodes[pathNode] != 3:
                        drawnNodes[pathNode] = 5
                        rect = pygame.rect.Rect((20*pathNode[0] + widthOffsetToCenter, 20*pathNode[1]), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (255, 0, 255), rect)
                        pygame.display.flip()
                        time.sleep(0.05)
                    pathNode = shortestPathNodes[pathNode]['prevNode']
                pygame.display.flip()
                continue
            if pygame.mouse.get_pos()[1] >= maxScreenHeight or pygame.mouse.get_pos()[0] >= maxScreenWidth or pygame.mouse.get_pos()[1] < 60:
                continue
            if pygame.mouse.get_pressed()[0] == True:
                if drawnNodes[
                        (int(pygame.mouse.get_pos()[0] / cellSize), int(pygame.mouse.get_pos()[1] / cellSize))] == 2 or  drawnNodes[
                        (int(pygame.mouse.get_pos()[0] / cellSize), int(pygame.mouse.get_pos()[1] / cellSize))] == 3:
                    continue
                if placeStart == True:
                    xOffset = int(pygame.mouse.get_pos()[0] / cellSize)
                    yOffset = int(pygame.mouse.get_pos()[1] / cellSize)
                    print(xOffset, yOffset)
                    pygame.draw.rect(screen, (0, 255, 0), nodes[(xOffset, yOffset)])
                    drawnNodes[
                        (int(pygame.mouse.get_pos()[0] / cellSize), int(pygame.mouse.get_pos()[1] / cellSize))] = 2
                    startIndex = (int(pygame.mouse.get_pos()[0] / cellSize), int(pygame.mouse.get_pos()[1] / cellSize))
                    placeStart = False
                    continue
                elif placeEnd == True:
                    xOffset = int(pygame.mouse.get_pos()[0] / cellSize)
                    yOffset = int(pygame.mouse.get_pos()[1] / cellSize)
                    pygame.draw.rect(screen, (255, 0, 0), nodes[(xOffset, yOffset)])
                    drawnNodes[
                        (int(pygame.mouse.get_pos()[0] / cellSize), int(pygame.mouse.get_pos()[1] / cellSize))] = 3
                    endIndex =  (int(pygame.mouse.get_pos()[0] / cellSize), int(pygame.mouse.get_pos()[1] / cellSize))
                    placeEnd = False
                    continue
                xOffset = int(pygame.mouse.get_pos()[0]/cellSize)
                yOffset = int(pygame.mouse.get_pos()[1]/cellSize)
                pygame.draw.rect(screen, (128,128,128), nodes[(xOffset,yOffset)])
                drawnNodes[(int(pygame.mouse.get_pos()[0]/cellSize),int(pygame.mouse.get_pos()[1]/cellSize))] = 1
            if placeStart or placeEnd:
                pygame.display.flip()
                continue
            if pygame.mouse.get_pressed()[2] == True:
                xOffset = int(pygame.mouse.get_pos()[0] / cellSize)
                yOffset = int(pygame.mouse.get_pos()[1] / cellSize)
                pygame.draw.rect(screen, (255, 255, 255), nodes[(xOffset, yOffset)])
                if drawnNodes[(xOffset, yOffset)] == 2:
                    placeStart = True
                    drawnNodes[(xOffset, yOffset)] = 0
                    continue
                elif drawnNodes[(xOffset, yOffset)] == 3:
                    placeEnd = True
                    drawnNodes[(xOffset, yOffset)] = 0
                    continue
                drawnNodes[(xOffset, yOffset)] = 0
                drawnNodes[(int(pygame.mouse.get_pos()[0]/ cellSize), int(pygame.mouse.get_pos()[1] / cellSize))] = 0
            placeStart = False
            placeEnd = False
            visualize = False
            pygame.display.flip()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/