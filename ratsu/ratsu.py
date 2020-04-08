from collections import defaultdict
import heapq

# dijkstra based on https://gist.github.com/kachayev/5990802 (with some modifications)

def dijkstra(graph, start, end):
    # graph is map of node -> list of other accessible nodes

    q, seen, mins = [(0,start,())], set(), {start: 0}
    while q:
        (cost,v1,path) = heapq.heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == end: return (cost, path)
            
            for v2 in graph.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + 1
                if prev is None or next < prev:
                    mins[v2] = next
                    heapq.heappush(q, (next, v2, path))
    return None, None

def shortest_path(*args):
    plen, path = dijkstra(*args)
    if plen is None: return None, None
    realpath = []
    sub = path
    while sub != ():
        realpath.append(sub[0])
        sub = sub[1]
    return plen, realpath[::-1]

def enumerate_jump_neighbours(x,y, width, height, jump_len):
    for flip in (True, False):
        for new_x in (x+jump_len, x-jump_len) if flip else (x+1, x-1):
            if new_x < 0 or new_x >= width:
                continue
            for new_y in (y+1, y-1) if flip else (y+jump_len, y-jump_len):
                if new_y < 0 or new_y >= height:
                    continue
                yield new_x, new_y

def compute_graph(board):
    width = len(board[0])
    height = len(board)
    edges = defaultdict(set)
    for y,row in enumerate(board):
        for x,node in enumerate(row):
            if node in '.@':
                for newx, newy in enumerate_jump_neighbours(x, y, width, height, 2):
                    if board[newy][newx] == '.':
                        edges[(x,y,False)].add((newx,newy,False))
                        edges[(x,y,True)].add((newx,newy,True))
                        edges[(newx,newy,False)].add((x,y,False))
                        edges[(newx,newy,True)].add((x,y,True))
                    if board[newy][newx] == '*':
                        edges[(x,y,False)].add((newx,newy,False))
                        edges[(x,y,True)].add((newx,newy,False))
                for newx, newy in enumerate_jump_neighbours(x, y, width, height, 3):
                    if board[newy][newx] == '.':
                        edges[(x,y,False)].add((newx,newy,True))
                    if board[newy][newx] == '*':
                        edges[(x,y,False)].add((newx,newy,False))
            if node == '@':
                start_pos = (x, y, False)
            if node == '*':
                end_pos = (x, y, False)
    return edges, start_pos, end_pos

def main():
    board = open("ratsusis.txt").read().strip().split('\n')[1:]
    edges, start_pos, end_pos = compute_graph(board)
    base_len, best_path = shortest_path(edges, start_pos, end_pos)
    out = str(base_len)+'\n'+'\n'.join(map(lambda x: str(x[1]+1)+" "+str(x[0]+1), best_path))
    open("ratsuval.txt", 'w').write(out)

main()
