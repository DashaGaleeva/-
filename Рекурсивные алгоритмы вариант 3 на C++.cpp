#include <iostream>

// Рекурсивная функция для нахождения НОД по алгоритму Евклида
int gcd(int a, int b) {
    // Базовый случай: если второе число равно 0, НОД равен первому числу
    if (b == 0) {
        return a;
    }
    // Рекурсивный вызов: НОД(a, b) = НОД(b, a mod b)
    return gcd(b, a % b);
}

int main() {
    int num1, num2;
    
    std::cout << "Введите два целых числа: ";
    std::cin >> num1 >> num2;
    
    // Убедимся, что числа положительные (алгоритм работает с абсолютными значениями)
    num1 = (num1 < 0) ? -num1 : num1;
    num2 = (num2 < 0) ? -num2 : num2;
    
    int result = gcd(num1, num2);
    std::cout << "НОД(" << num1 << ", " << num2 << ") = " << result << std::endl;
    
    return 0;
}
