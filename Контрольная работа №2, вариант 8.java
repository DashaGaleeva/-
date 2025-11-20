public static List<int[]> aStar(int[][] grid) {
    int n = grid.length, m = grid[0].length;
    PriorityQueue<Node> open = new PriorityQueue<>();
    Set<String> closed = new HashSet<>();
    open.add(new Node(0, 0, 0, heuristic(0, 0, n - 1, m - 1)));
    Node[][] parent = new Node[n][m];
    while (!open.isEmpty()) {
        Node curr = open.poll();
        if (curr.row == n - 1 && curr.col == m - 1) {
            return reconstructPath(parent, n - 1, m - 1);
        }
        closed.add(curr.row + "," + curr.col);
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};  
        for (int i = 0; i < 4; i++) {
            int newRow = curr.row + dr[i];
            int newCol = curr.col + dc[i];
            if (newRow < 0 || newRow >= n || newCol < 0 || newCol >= m || grid[newRow][newCol] == 1) {
                continue;
            }
            if (closed.contains(newRow + "," + newCol)) {
                continue;
            }
            int newG = curr.g + 1; // Стоимость шага = 1
            Node neighbor = new Node(newRow, newCol, newG, heuristic(newRow, newCol, n - 1, m - 1));
            if (!open.contains(neighbor)) {
                open.add(neighbor);
                parent[newRow][newCol] = curr;
            } else {
                for (Node node : open) {
                    if (node.row == newRow && node.col == newCol && newG < node.g) {
                        node.g = newG;
                        parent[newRow][newCol] = curr;
                        break;
                    }
                }
            }
        }
    }
    return new ArrayList<>();
}
private static int heuristic(int row, int col, int targetRow, int targetCol) {
    return Math.abs(targetRow - row) + Math.abs(targetCol - col);
}
private static List<int[]> reconstructPath(Node[][] parent, int row, int col) {
    List<int[]> path = new ArrayList<>();
    Node current = parent[row][col];   
    path.add(new int[]{row, col});
    while (current != null) {
        path.add(new int[]{current.row, current.col});
        current = parent[current.row][current.col];
    }
    Collections.reverse(path);
    return path;
}
static class Node implements Comparable<Node> {
    int row, col;
    int g;
    int h;
    int f;
    public Node(int row, int col, int g, int h) {
        this.row = row;
        this.col = col;
        this.g = g;
        this.h = h;
        this.f = g + h;
    }
    @Override
    public int compareTo(Node other) {
        return Integer.compare(this.f, other.f);
    }
}
