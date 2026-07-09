"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        d={};
        def func(node):
            if(node):
                if(node not in d):
                    d[node]=Node(node.val);
                    for i in node.neighbors:
                        func(i);
        func(node);
        visited=set();
        def func2(node):
            if(node):
                if(node in visited):
                    return;
                visited.add(node);
                for i in node.neighbors:
                    d[node].neighbors.append(d[i]);
                for i in node.neighbors:
                    func2(i)
        func2(node);
        if(node):
            return d[node]
        else:
            return None
            

        """
        :type node: Node
        :rtype: Node
        """
        