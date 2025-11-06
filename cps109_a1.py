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

    while index < len(content):
        if "====" in content[index]:
            print("Recording?", not recording)
            recording = not recording
            index += 1
            continue
        
        if recording:
            rows.append(content[index].strip())

        index += 1
    
    return rows

def display_map(rows):
    for row in rows:
        print(row)

def get_neighbors():
    pass

def pathfind():
    pass

f = open("data.txt", "r")
content = f.readlines()
rows = get_rows(content)

display_map(rows)

f.close()