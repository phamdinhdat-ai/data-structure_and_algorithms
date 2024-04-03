

#include <iostream>
#include <stack>
#include <vector>
#include <queue>
using namespace std;


struct Edge{
    int src, dest;
};

class Graph{
    public:
        // create a new vector
        vector<int>  adjList;

        Graph(vector<Edge> const &edge, int n){
            adjList.resize(n);

            for (auto &edge: edge){
                adjList[edge.src].push(edge.dest);
                adjList[edge.dest].push_back(edge.src);
            }
        }
};



void BFS(Graph const &graph, int v, vector<bool> &discovered){
    queue<int> q;

    discovered[v] = true; 

    q.push(v);

    while (! q.empty()){
        v = q.front();
        q.pop();
        cout << v << " ";
        for (int u: graph.adjList[v]){
            if (! discovered[u]){
                discovered[u] = true;
                q.push(u);
            }
        };
    }
}
// void DFS(Graph const &graph, int v, vector<bool> &discovered){
    

//     discovered[v] = true;
//     cout << v << " ";
//     for(int u: graph.adjList[v]){
//         if(!discovered[u]){
//             DFS(graph, u, discovered);
//         }
//     }
// }


int main()
{
    // vector of graph edges as per the above diagram
    vector<Edge> edges = {
        {1, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}, {5, 9},
        {5, 10}, {4, 7}, {4, 8}, {7, 11}, {7, 12}
        // vertex 0, 13, and 14 are single nodes
    };
 
    // total number of nodes in the graph (labelled from 0 to 14)
    int n = 15;
 
    // build a graph from the given edges
    Graph graph(edges, n);
 
    // to keep track of whether a vertex is discovered or not
    vector<bool> discovered(n, false);
 
    // Perform BFS traversal from all undiscovered nodes to
    // cover all connected components of a graph
    for (int i = 0; i < n; i++)
    {
        if (discovered[i] == false)
        {
            // start BFS traversal from vertex `i`
            BFS(graph, i, discovered);
        }
    }
 
    return 0;
}