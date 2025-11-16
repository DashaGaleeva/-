// Граф
<dependency>
    <groupId>org.jgrapht</groupId>
    <artifactId>jgrapht-core</artifactId>
    <version>1.5.1</version>
</dependency>
import org.jgrapht.*;
import org.jgrapht.graph.*;
public class JGraphTExample {
    public static void main(String[] args) {
        // Создаём неориентированный граф
        Graph<Integer, DefaultEdge> graph = 
            new SimpleGraph<>(DefaultEdge.class);
        // Добавляем вершины
        graph.addVertex(1);
        graph.addVertex(2);
        graph.addVertex(3);
        // Добавляем рёбра
        graph.addEdge(1, 2);
        graph.addEdge(2, 3);
        graph.addEdge(1, 3);
        System.out.println("Граф: " + graph);
        System.out.println("Рёбра: " + graph.edgeSet());
    }
}

// Дерево
class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;
    public TreeNode(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
public class BinarySearchTree {
    private TreeNode root;
    public BinarySearchTree() {
        this.root = null;
    }
    // Вставка значения
    public void insert(int value) {
        root = insertRec(root, value);
    }
    private TreeNode insertRec(TreeNode node, int value) {
        if (node == null) {
            return new TreeNode(value);
        }
        if (value < node.value) {
            node.left = insertRec(node.left, value);
        } else if (value > node.value) {
            node.right = insertRec(node.right, value);
        }
        return node;
    }
    // Поиск значения
    public boolean search(int value) {
        return searchRec(root, value);
    }
    private boolean searchRec(TreeNode node, int value) {
        if (node == null) {
            return false;
        }
        if (node.value == value) {
            return true;
        }
        return (value < node.value) 
            ? searchRec(node.left, value) 
            : searchRec(node.right, value);
    }
    // Удаление значения
    public void delete(int value) {
        root = deleteRec(root, value);
    }
    private TreeNode deleteRec(TreeNode node, int value) {
        if (node == null) {
            return null;
        }
        if (value < node.value) {
            node.left = deleteRec(node.left, value);
        } else if (value > node.value) {
            node.right = deleteRec(node.right, value);
        } else {
            // Найден узел для удаления   
            // Случай 1: нет детей (лист)
            if (node.left == null && node.right == null) {
                return null;
            }
            // Случай 2: один ребёнок
            else if (node.left == null) {
                return node.right;
            } else if (node.right == null) {
                return node.left;
            }
            // Случай 3: два ребёнка
            else {
                // Находим минимальный узел в правом поддереве
                TreeNode minNode = findMin(node.right);
                node.value = minNode.value;
                node.right = deleteRec(node.right, minNode.value);
            }
        }
        return node;
    }
    private TreeNode findMin(TreeNode node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }
    // Обходы дерева
    public void inOrderTraversal() {
        System.out.print("In-order: ");
        inOrderRec(root);
        System.out.println();
    }
    private void inOrderRec(TreeNode node) {
        if (node != null) {
            inOrderRec(node.left);
            System.out.print(node.value + " ");
            inOrderRec(node.right);
        }
    }
    public void preOrderTraversal() {
        System.out.print("Pre-order: ");
        preOrderRec(root);
        System.out.println();
    }
    private void preOrderRec(TreeNode node) {
        if (node != null) {
            System.out.print(node.value + " ");
            preOrderRec(node.left);
            preOrderRec(node.right);
        }
    }
    public void postOrderTraversal() {
        System.out.print("Post-order: ");
        postOrderRec(root);
        System.out.println();
    }
    private void postOrderRec(TreeNode node) {
        if (node != null) {
            postOrderRec(node.left);
            postOrderRec(node.right);
            System.out.print(node.value + " ");
        }
    }
    // Проверка пустоты дерева
    public boolean isEmpty() {
        return root == null;
    }
    // Получение высоты дерева
    public int getHeight() {
        return getHeightRec(root);
    }
    private int getHeightRec(TreeNode node) {
        if (node == null) {
            return -1; // Пустое поддерево имеет высоту -1
        }
        int leftHeight = getHeightRec(node.left);
        int rightHeight = getHeightRec(node.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
