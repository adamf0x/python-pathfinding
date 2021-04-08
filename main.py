# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import sys

import pygame


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

if __name__ == "__main__":
    windowSize = width, height = (500, 500)
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode(size=windowSize)
    screen.fill((0,0,0))
    nodes = {}
    for i in range(0, 500, 20):
        for j in range(0,500, 20):
            rect = pygame.rect.Rect((i, j), (18, 18))
            pygame.draw.rect(screen, (128, 128, 128), rect)
            nodes[(int(i/20),int(j/20))] = rect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        if pygame.mouse.get_pressed()[0] == True:
            xOffset = int(pygame.mouse.get_pos()[0]/20)
            yOffset = int(pygame.mouse.get_pos()[1]/20)
            pygame.draw.rect(screen, (0,0,0), nodes[(xOffset,yOffset)])
        if pygame.mouse.get_pressed()[2] == True:
            xOffset = int(pygame.mouse.get_pos()[0] / 20)
            yOffset = int(pygame.mouse.get_pos()[1] / 20)
            pygame.draw.rect(screen, (128, 128, 128), nodes[(xOffset, yOffset)])
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
