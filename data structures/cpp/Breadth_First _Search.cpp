#include <iostream>
#include <list>
#include <queue>
using namespace std;

class Graph {
  int numVertices;
  list<int>* adjLists;
  bool* visited;

   public:
  Graph(int vertices);
  void addEdge(int src, int dest);
  void BFS(int startVertex);
};

Graph::Graph(int vertices) {
  numVertices = vertices;
  adjLists = new list<int>[vertices];
}


void Graph::addEdge(int src, int dest) {     // Add edges to the graph
  adjLists[src].push_back(dest);
  adjLists[dest].push_back(src);
}

// BFS algorithm
void Graph::BFS(int startVertex) {
  visited = new bool[numVertices];
  for (int i = 0; i < numVertices; i++)
    visited[i] = false;

  list<int> queue;

  visited[startVertex] = true;
  queue.push_back(startVertex);

  list<int>::iterator i;

  while (!queue.empty()) {
    int currVertex = queue.front();
    cout << "Visited " << currVertex << " "<<"\n";
   
    queue.pop_front();

    for (i = adjLists[currVertex].begin(); i != adjLists[currVertex].end(); ++i) {
      int adjVertex = *i;
      if (!visited[adjVertex]) {
        visited[adjVertex] = true;
        queue.push_back(adjVertex);
        
      }
    }
  } 
  cout <<"START VERTEX:";
  cout <<  startVertex << " ";
}
void recursiveBFS(Graph const &graph, queue<int> &q,
                    vector<bool> &discovered)
{
    if (q.empty())
        return;
 
    // pop front node from queue and print it
    int v = q.front();
    q.pop();
    cout << v << " ";
 
    // do for every edge (v -> u)
    for (int u : graph.adjList[v])
    {
        if (!discovered[u])
        {
            // mark it discovered and push it into queue
            discovered[u] = true;
            q.push(u);
        }
    }
 
    recursiveBFS(graph, q, discovered);
}
int main() {
  Graph g(15);
  g.addEdge(1, 2);
  g.addEdge(1, 3);
  g.addEdge(1, 4);
  g.addEdge(2, 5);
  g.addEdge(2, 6);
  g.addEdge(5, 9);
  g.addEdge(5, 10);g.addEdge(4, 7);g.addEdge(4, 8);g.addEdge(7, 11);
  g.addEdge(7, 12);
recursiveBFS(graph, q, discovered)
  g.BFS(2);

  return 0;
}