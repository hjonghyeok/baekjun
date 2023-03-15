
# def solution(heights, seats):
#     answer = []
#     merge_heights = []
#     for dept in heights:
#         for student in dept:
#             merge_heights.append(student)
        
#     heights = sorted(merge_heights)
#     columns = 4
#     rows = len(heights) // columns + 1

#     for i in range(0, rows):
#         aa = i * columns + seats - 1
#         if i * columns + seats - 1 < len(heights):
#             answer.append(heights[i *  columns + seats - 1])

#     return answer

# heights = [[171,158,164,180,155,174],[164,168,157,185,155,169],[173,183,149,151,188,190]]

# seats = 2

# print(solution(heights, seats))
# 1 5 9 13


def solution(maps, start, visited):
    answer = []
    queue = list()
    visited = list()
    
    queue.append(start)
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            answer.append(node)
            queue = []
            queue.extend(maps[node-1])
        
    return answer
        
    
maps = [[4],[3,4],[2,5],[1,2,5,7],[3,4],[7],[4,6]]
start = 1
visited = []

print(solution(maps, start, visited))