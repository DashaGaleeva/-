#include <iostream>
using namespace std;

// Процедура перестроения кучи сверху вниз
void heapify(int arr[], int n, int root) {
    int largest = root;          // Предположительно, корень является крупнейшим
    int leftChild = 2 * root + 1;// Левый ребенок
    int rightChild = 2 * root + 2;// Правый ребенок

    // Если левый ребенок существует и больше родителя
    if (leftChild < n && arr[leftChild] > arr[largest])
        largest = leftChild;

    // Если правый ребенок существует и больше кандидата на крупнейший
    if (rightChild < n && arr[rightChild] > arr[largest])
        largest = rightChild;

    // Если наибольший элемент изменился, то переставляем их местами
    if (largest != root) {
        swap(arr[root], arr[largest]);
        // Рекурсивно восстанавливаем кучу снизу вверх
        heapify(arr, n, largest);
    }
}

// Основная функция сортировки
void heapSort(int arr[], int n) {
    // Постройка кучи (преобразование массива в max-кучу)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Один за другим извлекаем корни из кучи
    for (int i = n - 1; i > 0; i--) {
        // Меняем местами корневой элемент (max-элемент) с последним элементом
        swap(arr[0], arr[i]);
        // Восстанавливаем кучу после удаления корневого элемента
        heapify(arr, i, 0);
    }
}

// Вспомогательная функция для вывода массива
void printArray(int arr[], int n) {
    for (int i = 0; i < n; ++i)
        cout << arr[i] << " ";
    cout << endl;
}

// Основная программа
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Исходный массив: ";
    printArray(arr, n);

    heapSort(arr, n);

    cout << "Отсортированный массив: ";
    printArray(arr, n);

    return 0;
}
