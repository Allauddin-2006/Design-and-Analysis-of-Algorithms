#    A
#   / \
#  B   C
# /
#D

map_rooms = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],  # Added Room C to prevent a KeyError
    "D": [],
}

def dfs(start, goal):
    to_do = [start]
    visited = []
    order = []
    
    while to_do:
        room = to_do.pop()
        
        if room in visited:
            continue
            
        # These must be outside the 'if room in visited' block
        visited.append(room)
        order.append(room)
        
        if room == goal:
            return order
            
        # The loop must look up paths and add them to the to_do stack
        for nxt in map_rooms.get(room, []):
            to_do.append(nxt)
            
    return order

order = dfs("A", "D")
print(order)

