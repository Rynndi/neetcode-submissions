class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {} 
        for cla in prerequisites:
            if cla[0] not in hashmap:
                hashmap[cla[0]] = []
            hashmap[cla[0]].append(cla[1])
        visiting = set() 
        visited = set() 

        for i in range(numCourses):
            if i not in visited:
                stack = [(i, False)]
                while stack:
                    currClass, processingDone = stack.pop() 
                    if processingDone:
                        visiting.remove(currClass)
                        visited.add(currClass)
                        continue 
                    if currClass in visited:
                        continue 
                    if currClass in visiting:
                        return False 
                    visiting.add(currClass)
                    stack.append((currClass, True))
                    if currClass in hashmap:
                        for neighbor in hashmap[currClass]:
                            if neighbor not in visited:
                                stack.append((neighbor, False))
        return True 