public class MergeSortExample {

    public static void mergeSort(int[] array) {
        // Проверяем наличие элементов в массиве
        if (array.length <= 1) {
            return; // Одну ячейку сортировать не надо
        }
        
        // Рассчитываем середину массива
        int mid = array.length / 2;
        
        // Создание левого и правого подмассива
        int[] leftHalf = new int[mid];
        int[] rightHalf = new int[array.length - mid];
        
        // Копируем левую половину в левый подмассив
        System.arraycopy(array, 0, leftHalf, 0, mid);
        
        // Копируем правую половину в правый подмассив
        System.arraycopy(array, mid, rightHalf, 0, array.length - mid);
        
        // Рекурсивно сортируем оба подмассива
        mergeSort(leftHalf);
        mergeSort(rightHalf);
        
        // Объединяем отсортированные подмассивы обратно в оригинальный массив
        merge(array, leftHalf, rightHalf);
    }

    private static void merge(int[] result, int[] leftHalf, int[] rightHalf) {
        // Индексы для левого, правого подмассивов и результирующего массива
        int l = 0; // индекс для левого подмассива
        int r = 0; // индекс для правого подмассива
        int k = 0; // индекс для результирующего массива
        
        // Объединяем два отсортированных подмассива
        while (l < leftHalf.length && r < rightHalf.length) {
            if (leftHalf[l] <= rightHalf[r]) {
                result[k++] = leftHalf[l++];
            } else {
                result[k++] = rightHalf[r++];
            }
        }
        
        // Добавляем остатки из левого подмассива, если они остались
        while (l < leftHalf.length) {
            result[k++] = leftHalf[l++];
        }
        
        // Добавляем остатки из правого подмассива, если они остались
        while (r < rightHalf.length) {
            result[k++] = rightHalf[r++];
        }
    }

    public static void main(String[] args) {
        int[] numbers = {38, 27, 43, 3, 9, 82, 10};
        
        System.out.println("Исходный массив:");
        printArray(numbers);
        
        mergeSort(numbers);
        
        System.out.println("\nОтсортированный массив:");
        printArray(numbers);
    }

    // Вспомогательная функция для печати массива
    private static void printArray(int[] array) {
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
