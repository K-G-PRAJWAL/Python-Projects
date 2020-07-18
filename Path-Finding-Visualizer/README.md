# A* Path Finding Algorithm

<img src="/Path-Finding-Visualizer/img.jpg">

An A* path finding algorithm is used to find the shortest distance between two given points on a graph. This algorithm, unlike other path-finding algorithm such as Dijkstra's algorithm doesn't brute force search for every node to find a path, but use a  heuristic function that guides which path is essential for accomplishing the task.

The formula used here is `F(n) = G(n) + H(n)`
where,
- G(n) => The G score is the shortest distance between start node to the current node.
- H(n) => The H score is the heuristic the estimates the distance of end node from the start node.
- F(n) => The F score is the addition of both G score and H score.

Learn more about A-star path finding algorithm [here](https://en.wikipedia.org/wiki/A*_search_algorithm).