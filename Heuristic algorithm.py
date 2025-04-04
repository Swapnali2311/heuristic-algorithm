import networkx as nx

# Step 1: Create a simple sample graph
def create_graph():
    G = nx.Graph()
    # Add edges between nodes
    G.add_edges_from([
        (1, 2), (1, 3),
        (2, 4), (3, 4),
        (4, 5), (5, 6),
        (5, 7)
    ])
    return G

# Step 2: Greedy algorithm for vertex cover
def greedy_vertex_cover(G):
    cover = set()
    remaining_edges = set(G.edges())
    
    while remaining_edges:
        # Pick node with the highest degree
        node = max(G.degree, key=lambda x: x[1])[0]
        cover.add(node)

        # Remove all edges connected to this node
        remaining_edges = {e for e in remaining_edges if node not in e}
        G.remove_node(node)  # Optional: remove node to update degrees

    return cover

# Step 3: Execute the algorithm
if __name__ == "__main__":
    G = create_graph()
    cover = greedy_vertex_cover(G)
    print("Greedy Vertex Cover:", cover)
