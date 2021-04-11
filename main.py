# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sys
import time

import pygame
from pygame.locals import *

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

def dijkstras(nodes, startNode, endNode, dimensions):
    shortestPathNodes = {}
    uncompletedNodes = nodes
    prev = None
    for i in uncompletedNodes:
        uncompletedNodes[i] = float('inf')
    uncompletedNodes[startNode] = 0
    while len(list(shortestPathNodes.keys())) != len(list(uncompletedNodes.keys())):
        uncompletedNodes = {k: v for k, v in sorted(uncompletedNodes.items(), key=lambda item: item[1])}
        for j in list(uncompletedNodes.keys()):
            if j not in shortestPathNodes:
                curr = j
                break
        if curr == endNode:
            shortestPathNodes[curr] =[uncompletedNodes[curr], prev]
            return shortestPathNodes
        walkableNodes = []
        if curr[0] > 0:
            walkableNodes.append((curr[0]-1, curr[1]))
        if curr[1] > 0:
            walkableNodes.append((curr[0], curr[1]-1))
        if curr[0] > 0 and curr[1] > 0:
            walkableNodes.append((curr[0]-1, curr[1]-1))
        if curr[0] < dimensions[0]:
            walkableNodes.append((curr[0]+1, curr[1]))
        if curr[1] < dimensions[1]:
            walkableNodes.append((curr[0], curr[1]+1))
        if curr[0] < dimensions[0] and curr[1] < dimensions[1]:    
            walkableNodes.append((curr[0]+1, curr[1]+1))
        if curr[0] > 0 and curr[1] < dimensions[1]:
            walkableNodes.append((curr[0]-1, curr[1]+1))
        if curr[0] < dimensions[0] and curr[1] > 0:
            walkableNodes.append((curr[0]+1, curr[1]-1))

        for node in walkableNodes: 
            if uncompletedNodes[node] > uncompletedNodes[curr] + 1:
                uncompletedNodes[node] = uncompletedNodes[curr] + 1
        shortestPathNodes[curr] = [uncompletedNodes[curr], prev]
        prev = curr
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
    drawnNodes[(0, 0)] = 2
    drawnNodes[(int(maxScreenWidth / cellSize) - 1, int(maxScreenHeight / cellSize) - 1)] = 3
    startIndex = (0,0)
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
                for j in range(0, maxScreenHeight, cellSize):
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

            visualizeButton = pygame.rect.Rect((int(pygame.display.get_window_size()[0] / 2) - 50, 10), (100, 30))
            pygame.draw.rect(screen, (70, 40, 100), visualizeButton)
            font = pygame.font.SysFont(None, 15)
            img = font.render('Click To Start', True, (225, 255, 255))
            screen.blit(img, (int(visualizeButton.x) + int(visualizeButton.width / 2) - 35,
                              int(visualizeButton.y) + int(visualizeButton.height / 2) - 12))
            if (visualizeButton.x <= pygame.mouse.get_pos()[0] <= (visualizeButton.x + visualizeButton.width) and visualizeButton.y <= pygame.mouse.get_pos()[1] <= (visualizeButton.y + visualizeButton.height)) and event.type==MOUSEBUTTONUP:
                for i in range(0, maxScreenWidth, cellSize):
                    for j in range(0, maxScreenHeight, cellSize):
                        if drawnNodes[(int(i / cellSize), int(j / cellSize))] == 4:
                            rect = pygame.rect.Rect((i + widthOffsetToCenter, j), (cellSize - 2, cellSize - 2))
                            pygame.draw.rect(screen, (255, 255, 255), rect)
                            nodes[(int(i / cellSize), int(j / cellSize))] = rect
                            drawnNodes[(int(i / cellSize), int(j / cellSize))] = 0
                shortestPathNodes = dijkstras(nodes, startIndex, endIndex, ((int(maxScreenWidth/cellSize))-1, int(maxScreenHeight/cellSize)-1))
                for node in shortestPathNodes:
                    if node in drawnNodes and drawnNodes[node] != 2 and drawnNodes[node] != 3:
                        drawnNodes[node] = 4
                        rect = pygame.rect.Rect((20*node[0], 20*node[1]), (cellSize - 2, cellSize - 2))
                        pygame.draw.rect(screen, (0, 255, 255), rect)
                        nodes[(int(i / cellSize), int(j / cellSize))] = rect
                        pygame.display.flip()
                        time.sleep(0.005)
                pygame.display.flip()
                continue
            if pygame.mouse.get_pos()[1] >= maxScreenHeight or pygame.mouse.get_pos()[0] >= maxScreenWidth:
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
