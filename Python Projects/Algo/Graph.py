import threading

import pygame
from properties import *
import random

from typer.colors import WHITE

pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("")
font = pygame.font.SysFont("Arial", 16)


def give_random_centre()->tuple[int,int]:
    return random.randint(2*circle_radius, screen_width - 2*circle_radius), random.randint(2*circle_radius, screen_height - 2*circle_radius)

def circle(x, y,radius = circle_radius):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

def line(start, end):
    pygame.draw.line(screen, (255, 255, 255), start, end, 1)

def text(x,y,text):
    number_text = font.render(text, True, WHITE)
    text_rect = number_text.get_rect(center=(x, y))
    screen.blit(number_text, text_rect)


def build_pyramid(n):
    x = dx + 2 * circle_radius

    const_x = 2 * dx + circle_radius
    const_y = 2 * dy + circle_radius

    for i in range(1, n + 1):
        circle(x, screen_height // 2)
        coordinates.append((x, screen_height // 2))

        y = screen_height // 2
        for j in range(1, i):
            y += const_y
            circle(x, y)
            coordinates.append((x, y))
            pass

        y = screen_height // 2
        for j in range(1, i):
            y -= const_y
            circle(x, y)
            coordinates.append((x, y))
            pass
        x += const_x

def is_valid_point(x, y, min_distance=30):
    for px, py in point_set:
        if abs(px - x) < min_distance and abs(py - y) < min_distance:
            return False
    return True

def generate_points(n):
    i = 0
    while i != n:
        temp_x,temp_y = give_random_centre()

        if is_valid_point(temp_x,temp_y):
            i += 1
            point_set.add((temp_x,temp_y))
            point_list[i] = (temp_x,temp_y)

def generate_edges(n, max_edges=None):
    nodes = list(range(1, n + 1))
    edges = set()  # Using a set to avoid duplicates

    max_edges = max_edges or 2 * n  # Limit the number of edges to prevent too many connections

    while len(edges) < max_edges:
        u, v = random.sample(nodes, 2)  # Pick two distinct nodes
        edge = (u, v) if u < v else (v, u)  # Keep edges in a consistent order

        if edge not in edges:
            edges.add(edge)

    return list(edges)

def generate_graph():
    hs = {}
    for edge in edges:
        x,y = edge
        if x is None or y is None:
            continue
        if x not in hs:
            hs[x] = []
        if y not in hs:
            hs[y] = []

        hs[x].append(y)
        hs[y].append(x)

    return hs

def redraw(text):
    circle(x, y)
    text(x, y, str(vertex))

def dfs(startNode):
    visited = set()
    stack = [startNode]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)



        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


point_list = {}
point_set = set()
edges = generate_edges(50,100)
generate_points(100)
graph = generate_graph()



while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    for point1, point2 in edges:
        line(point_list[point1], point_list[point2])

    for vertex,value in point_list.items():
        x,y = value
        circle(x,y)
        text(x,y,str(vertex))


    # build_pyramid(20)
    # for start, end in edges:
    #     line(start, end)

    pygame.display.update()

pygame.quit()
