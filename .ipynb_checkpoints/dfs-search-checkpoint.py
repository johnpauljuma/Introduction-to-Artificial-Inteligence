class environment(object):
    mygraph = {"1":set(["2","3"]),
                "2":set(["1","4"]),
                "3":set(["1","4"]),
                "4":set(["2","3"])
                }
    state = "2"
    goal = "4"
class agent (environment):
    #this function looks through all available paths and returns
    def dfs(graph,start,goal):
        stack = [(start,[start])]
        p = []
        while stack:
            (vertex,path) = stack.pop()
            for next in graph[vertex]-set(path):
                if next == goal:
                    p.append(path+[next])
            else:
                stack.append((next,path+[next]))
        return p
    def __init__(self,environment):
        print("dfs-all paths",
agent.dfs(environment.mygraph,environment.state,environment.goal))
e1 = environment()
a1 = agent(e1)