# **************************************************************** #
# ************** Small tutorial on creating a graph ************** #
# **************************************************************** #

# A graph can be represented as a map in python such as:
#       graph = {"A" : ["B","C"], "B" : ["A","D"], "C" : ["A","D"], "D" : ["B","C"]}
# "D" is here our exit node, and we're supposing that we have 2 ways arcs
# We'll also suppose that the input will be such as we have the number of nodes and exits inside the graph :
#
#       4 4 1
#       0 1
#       0 2
#       1 3
#       2 3
#       3
# 
# Now the graph looks like this:
#  
#       graph = {0: [1, 2], 1: [3, 0], 2: [3, 0], 3: [1, 2]}
#  


def create_graph() -> tuple:
    '''
    This function returns a tuple with both the graph and a list of exit nodes for said graph
    '''

    number_of_nodes,number_of_arcs,number_of_exits = map ( int , input().split() )
    graph = {i: [] for i in range(number_of_nodes)}
    for _ in range(number_of_arcs) :
        node1,node2 = map ( int , input().split() )
        graph[node1].append(node2)
        graph[node2].append(node1)

    exits = [int(input()) for _ in range(number_of_exits)]

    return (graph, exits)


if __name__ == "__main__":
    try:
        graph,exits = create_graph()
        print(f'Your graph:\n{graph}\nThe Exits:\n{exits}')
    except Exception as e:
        print(e)
