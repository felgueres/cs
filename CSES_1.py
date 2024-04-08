# SHORTEST ROUTEST I
import sys

v,e = map(int, sys.stdin.readline().split())

edges = []

for _ in range(e):
    a,b,w = map(int, sys.stdin.readline().split())
    edges.append((a,b,w))

