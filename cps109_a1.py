"""

Must have all of these:
1. Conditions and decision making using if/else statements.
2. Working with sequences, such as lists, tuples, and strings.
3. Sequence iteration using for loops, general iteration using wile loops.
4. Importing namespaces, using their functions, writing your own functions.
5. Performing file I/O, reading input from a file, writing output to a file.

Problem:
Pathfinding, A* algorithm

"""

def get_rows(content):
    index = 0
    recording = False
    rows = []

    start = (0, 0)
    end = (1, 1)

    while index < len(content):
        if "====" in content[index]:
            recording = not recording
            index += 1
            continue
        
        if recording:
            new_row = content[index].strip()

            if "S" in new_row:
                start = (new_row.find("S"), index - 1)

            if "G" in new_row:
                end = (new_row.find("G"), index - 1)
            
            rows.append(new_row)

        index += 1
    
    return rows, start, end

def display_map(rows):
    for row in rows:
        print(row)

def get_neighbors(rows, current):
    x, y = current[0], current[1]

    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    )

def heuristic(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] + pos1[1])

def distance(pos1, pos2):
    if abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 1:
        return 1
    else:
        return 999999

def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current] # trace back, since came_from tracks where each node of the path originated from
        path.insert(0, current)
    
    return path

def pathfind(rows, start, end):
    # heuristic can be found
    # Cost = G + H
    # where G is the distance between the current node and the start node
    # where H is the estimated distance from the current node to the end node

    open_set = set()
    came_from = {}

    open_set.add(start)

    current = start
    g_score = {start:0}
    h_score = {start:heuristic(current, end)}

    while open_set != set():
        if current == end:
            return reconstruct_path(came_from, current)

        lowest = 9999999

        for coord in open_set:
            f = g_score.get(coord, float('inf')) + heuristic(coord, end)
            if f < lowest:
                lowest = f
                current = coord
        
        open_set.remove(current)

        for neighbor in get_neighbors(rows, current):
            tentative_g = g_score[current] + distance(current, neighbor)

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                open_set.add(neighbor)

    print("Failed pathfinding...")
    return

def interpret_results(rows, data):
    for tup in data:
        x, y = tup[0], tup[1]

        s = rows[x]
        s = s[:y] + "-" + s[y + 1:]

        rows[x] = s
    
    display_map(rows)

f = open("data.txt", "r")
content = f.readlines()
rows, start, end = get_rows(content)

print(start, end)

result = pathfind(rows, start, end)
interpret_results(rows, result)

f.close()