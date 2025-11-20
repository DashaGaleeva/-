Задание 8. A* для поиска пути
- Условие. Найти кратчайший путь в сетке с препятствиями от (0,0) до (n-1,m-1).
- Алгоритм: A* с эвристикой «расстояние до цели».
- Язык примера: Java
- public static List<int[]> aStar(int[][] grid) {
- int n = grid.length, m = grid[0].length;
- PriorityQueue<Node> open = new PriorityQueue<>();
- Set<String> closed = new HashSet<>();
- open.add(new Node(0, 0, 0, heuristic(0, 0, n-1, m-1)));
- while (!open.isEmpty()) {
- Node curr = open.poll();
- // ДОПИСАТЬ: генерация соседей, обновление open/closed
- }
- return path;
}
Что дописать: обработку соседей и обновление приоритетов.
