// Биноминальная куча (Binomial Heap)
#include <iostream>
#include <vector>
template<typename T>
struct BinomialNode {
    T key;
    int degree;
    BinomialNode* parent;
    BinomialNode* child;
    BinomialNewton* sibling;

    BinomialNode(T k) : key(k), degree(0), parent(nullptr),
                        child(nullptr), sibling(nullptr) {}
};
template<typename T>
class BinomialHeap {
private:
    std::vector<BinomialNode<T>*> roots; // Корни деревьев
    // Слияние двух деревьев одинаковой степени
    BinomialNode<T>* mergeTrees(BinomialNode<T>* a, BinomialNode<T>* b) {
        if (a->key > b->key) std::swap(a, b);
        b->parent = a;
        b->sibling = a->child;
        a->child = b;
        a->degree++;
        return a;
    }
    // Объединение списков корней
    void unionRoots(std::vector<BinomialNode<T>*>& h1, std::vector<BinomialNode<T>*>& h2) {
        std::vector<BinomialNode<T>*> merged;
        int i = 0, j = 0;
        while (i < h1.size() && j < h2.size()) {
            if (h1[i]->degree <= h2[j]->degree) {
                merged.push_back(h1[i++]);
            } else {
                merged.push_back(h2[j++]);
            }
        }
        while (i < h1.size()) merged.push_back(h1[i++]);
        while (j < h2.size()) merged.push_back(h2[j++]);
        roots = merged;
    }
    // Проход по списку корней с объединением деревьев одинаковой степени
    void consolidate() {
        if (roots.empty()) return;
        std::vector<BinomialNode<T>*> newRoots;
        for (auto node : roots) {
            while (!newRoots.empty() && newRoots.back()->degree == node->degree) {
                node = mergeTrees(newRoots.back(), node);
                newRoots.pop_back();
            }
            newRoots.push_back(node);
        }
        roots = newRoots;
    }
public:
    void insert(T key) {
        BinomialNode<T>* node = new BinomialNode<T>(key);
        std::vector<BinomialNode<T>*> temp = {node};
        unionRoots(temp, roots);
        consolidate();
    }
    T getMin() const {
        if (roots.empty()) throw std::runtime_error("Heap is empty");
        T minKey = roots[0]->key;
        for (auto node : roots) if (node->key < minKey) minKey = node->key;
        return minKey;
    }
    // Для полноты: extractMin, merge и др. — требуют дополнительной реализации
};

// Куча Фибоначчи (Fibonacci Heap)
#include <iostream>
template<typename T>
struct FibNode {
    T key;
    int degree;
    bool marked;
    FibNode* parent;
    FibNode* child;
    FibNode* left;
    FibNode* right;
    FibNode(T k) : key(k), degree(0), marked(false),
                 parent(nullptr), child(nullptr),
                 left(this), right(this) {}
};
template<typename T>
class FibonacciHeap {
private:
    FibNode<T>* min;
    int size;
    void addToRootList(FibNode<T>* node) {
        if (!min) {
            min = node;
        } else {
            node->left = min;
            node->right = min->right;
            min->right->left = node;
            min->right = node;
            if (node->key < min->key) min = node;
        }
    }
    void link(FibNode<T>* child, FibNode<T>* parent) {
        child->left->right = child->right;
        child->right->left = child->left;
        child->parent = parent;
        if (!parent->child) {
            parent->child = child;
            child->left = child;
            child->right = child;
        } else {
            child->left = parent->child;
            child->right = parent->child->right;
            parent->child->right->left = child;
            parent->child->right = child;
        }
        parent->degree++;
        child->marked = false;
    }
    void consolidate() {
        if (!min) return;
        std::vector<FibNode<T>*> A(size + 1, nullptr);
        auto start = min;
        do {
            auto curr = start;
            start = start->right;
            int d = curr->degree;
            while (A[d]) {
                auto y = A[d];
                if (curr->key > y->key) std::swap(curr, y);
                link(y, curr);
                A[d] = nullptr;
                d++;
            }
            A[d] = curr;
        } while (start != min);
        min = nullptr;
        for (auto& node : A) {
            if (node) {
                addToRootList(node);
                if (!min || node->key < min->key) min = node;
            }
        }
    }
public:
    FibonacciHeap() : min(nullptr), size(0) {}
    void insert(T key) {
        FibNode<T>* node = new FibNode<T>(key);
        addToRootList(node);
        size++;
    }
    T getMin() const {
        if (!min) throw std::runtime_error("Heap is empty");
        return min->key;
    }
    // extractMin, decreaseKey, delete — требуют полной реализации
};

// Хеш‑таблица (Hash Table)
#include <iostream>
#include <vector>
#include <list>
#include <functional> // для std::hash
template<typename Key, typename Value>
class HashTable {
private:
    std::vector<std::list<std::pair<Key, Value>>> table;
    size_t capacity;
    size_t count;
    size_t hash(const Key& key) const {
        return std::hash<Key>{}(key) % capacity;
    }
    void rehash() {
        std::vector<std::list<std::pair<Key, Value>>> oldTable = table;
        capacity *= 2;
        table.clear();
        table.resize(capacity);
        count = 0;
        for (const auto& bucket : oldTable) {
            for (const auto& pair : bucket) {
                insert(pair.first, pair.second);
            }
        }
    }
public:
    HashTable(size_t initialCapacity = 8)
        : capacity(initialCapacity), count(0) {
        table.resize(capacity);
    }
    void insert(const Key& key, const Value& value) {
        if (count >= capacity *)
          }
}
}
