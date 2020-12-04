'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
 

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
import 
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.right:
                
                queue.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)
                
            if node.left:
                queue.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)
        
        queue = collections.deque([target])
        distance = 0
        visited = set()
        visited.add([target])
        res= []

        while queue and distance <= K:

            for _ in range(len(queue)):
                node = queue.popleft()
                if distance == K:
                    res.append(node.val)

                for nei in graph[node]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            distance += 1
        return res




'''
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"

'''

#Solution 1:
# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         seen  = set([path[0] for path in paths])
#         for path in paths:
#             if path[1] not in seen:
#                 return path[1]


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        cities1 = [c[0] for c in paths]
        cities2 = [ c[1] for c in paths]

        
        for city in cities2:
            if city not in cities1:
                return city