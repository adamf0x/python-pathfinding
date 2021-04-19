# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sys
import time

import pygame
from pygame.locals import *

import heapq

from operator import *

class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print
            temp.data,
            temp = temp.next

class TreeNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def aStar(nodes, startNode, endNode, dimensions, drawnNodes):
    gScores = {}
    hScores = {}
    openSet = nodes
    fScores = []
    scores = {}
    infinity = 10000000000000000000000
    for i in openSet:
        scores[i] = {'fScore': infinity, 'hScore': infinity, 'gScore': infinity, 'parent': None}
        heapq.heappush(fScores, (infinity, i))
    for j in fScores:
        if j[1] == startNode:
            fScores.remove(j)
            heapq.heappush(fScores, (0, startNode))
            break
    scores[startNode] = {'fScore': 0, 'hScore': 0, 'gScore': 0, 'parent': None}

    current = heapq.heappop(fScores)[1]
    path = []
    searched = []
    while current != endNode:
        if current[0] > 0 and drawnNodes[(current[0]-1, current[1])] != 1:
            curr = (current[0]-1, current[1])
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1]-endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[1] > 3 and drawnNodes[(current[0], current[1]-1)] != 1:
            curr = (current[0], current[1]-1)
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1] - endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[0] < dimensions[0] and drawnNodes[(current[0] + 1, current[1])] != 1:
            curr = (current[0] + 1, current[1])
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1]-endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[1] < dimensions[1] and drawnNodes[(current[0], current[1] + 1)] != 1:
            curr = (current[0], current[1] + 1)
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1]-endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[0] > 0 and current[1] > 3 and drawnNodes[(current[0] - 1, current[1] - 1)] != 1:
            curr = (current[0] - 1, current[1] - 1)
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1]-endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[0] < dimensions[0] and current[1] < dimensions[1] and drawnNodes[(current[0] + 1, current[1] + 1)] != 1:
            curr = (current[0] + 1, current[1] + 1)
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1] - endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[0] > 0 and current[1] < dimensions[1] and drawnNodes[(current[0] - 1, current[1] + 1)] != 1:
            curr = (current[0] - 1, current[1] + 1)
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1] - endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        if current[0] < dimensions[0] and current[1] > 3 and drawnNodes[(current[0] + 1, current[1] - 1)] != 1:
            curr = (current[0] + 1, current[1] - 1)
            searched.append(curr)
            scores[curr]['parent'] = current
            if 'parent' not in current or scores[current]['parent'] == None:
                gScore = 1
            else:
                gScore = scores[scores[current]['parent']]['gScore'] + 1
            hScore = abs(curr[0] - endNode[0]) + abs(curr[1]-endNode[1])
            fScore = gScore + hScore
            scores[curr] = {'fScore': fScore, 'hScore': hScore, 'gScore': gScore}
            for j in fScores:
                if j[1] == curr:
                    fScores.remove(j)
                    heapq.heappush(fScores, (fScore, j[1]))
                    break
        current = heapq.heappop(fScores)[1]
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
                searched, path = aStar(nodes, startIndex, endIndex, ((int(maxScreenWidth/cellSize))-1, int(maxScreenHeight/cellSize)-1), drawnNodes)
                for node in searched:
                    if node in drawnNodes and drawnNodes[node] != 2 and drawnNodes[node] != 3:
                        drawnNodes[node] = 4
                        rect = pygame.rect.Rect((20 * node[0] + widthOffsetToCenter, 20 * node[1]),
                                                (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (0, 255, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                        pygame.display.flip()
                        # time.sleep(0.05)
                for node in path:
                    if node in drawnNodes and drawnNodes[node] != 2 and drawnNodes[node] != 3:
                        drawnNodes[node] = 5
                        rect = pygame.rect.Rect((20*node[0] + widthOffsetToCenter, 20*node[1]), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (255, 0, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                        pygame.display.flip()
                        # time.sleep(0.05)
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
    # node1 = TreeNode(4)
    # node1.insert(2)
    # node1.insert(7)
    # node1.insert(9)
    # node1.insert(6)
    # node1.PrintTree()
    # print()
    # def invertTree(rootNode):
    #     if rootNode.left is None and rootNode.right is None:
    #         return
    #     temp = rootNode.left
    #     rootNode.left = rootNode.right
    #     rootNode.right = temp
    #     invertTree(rootNode.left)
    #     invertTree(rootNode.right)
    # invertTree(node1)
    # node1.PrintTree()
    # print()
    # hugeValues = {}
    # def nthHugeNumber(number):
    #     if number <= 1:
    #         return number
    #     try:
    #         if hugeValues[number]:
    #             return hugeValues[number]
    #         else:
    #             hugeValues[number] = (nthHugeNumber(number - 1) + nthHugeNumber(number - 2)) ^ (
    #                         nthHugeNumber(number - 2) ^ math.factorial(2147483647))
    #             return (nthHugeNumber(number - 1) + nthHugeNumber(number - 2)) ^ (
    #                         nthHugeNumber(number - 2) ^ math.factorial(10000))
    #     except KeyError as e:
    #         hugeValues[number] = (nthHugeNumber(number-1) + nthHugeNumber(number-2))^(nthHugeNumber(number-2)^math.factorial(10000))
    #         return (nthHugeNumber(number-1) + nthHugeNumber(number-2))^(nthHugeNumber(number-2)^math.factorial(10000))
    # print(nthHugeNumber(998))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
