public class InterpolationSearch {

    // Реализация интерполирующего поиска
    public static int interpolationSearch(int[] arr, int target) {
        int low = 0;                   // Нижний индекс
        int high = arr.length - 1;     // Верхний индекс

        // Продолжаем искать, пока границы не пересекутся
        while ((low <= high) && (target >= arr[low]) && (target <= arr[high])) {
            // Предсказываем местоположение искомого элемента
            int pos = low + (((target - arr[low]) * (high - low)) / (arr[high] - arr[low]));

            // Если элемент найден, возвращаем его индекс
            if (arr[pos] == target) {
                return pos;
            }

            // Если элемент меньше ожидаемого, сужаем поиск влево
            if (arr[pos] < target) {
                low = pos + 1;
            }
            // Если элемент больше ожидаемого, сужаем поиск вправо
            else {
                high = pos - 1;
            }
        }

        // Если элемент не найден, возвращаем -1
        return -1;
    }

    // Метод для вывода массива
    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    // Пример использования
    public static void main(String[] args) {
        int[] myList = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
        int elementToFind = 22;

        // Выводим массив на экран
        System.out.print("Исходный массив: ");
        printArray(myList);

        // Вызываем функцию поиска
        int index = interpolationSearch(myList, elementToFind);

        // Выводим результат
        if (index != -1) {
            System.out.println("Элемент " + elementToFind + " найден на индексе " + index);
        } else {
            System.out.println("Элемент " + elementToFind + " не найден.");
        }
    }
}
