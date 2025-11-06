public class GCD {
    /**
     * Рекурсивная функция для нахождения НОД двух чисел по алгоритму Евклида.
     *
     * @param a первое число (неотрицательное)
     * @param b второе число (неотрицательное)
     * @return НОД чисел a и b
     */
    public static int gcd(int a, int b) {
        // Базовый случай: если одно из чисел равно 0, НОД — второе число
        if (b == 0) {
            return a;
        }
        
        // Рекурсивный вызов: НОД(a, b) = НОД(b, a mod b)
        return gcd(b, a % b);
    }

    // Пример использования
    public static void main(String[] args) {
        int num1 = 48;
        int num2 = 18;
        
        int result = gcd(num1, num2);
        System.out.println("НОД(" + num1 + ", " + num2 + ") = " + result);
        // Вывод: НОД(48, 18) = 6
    }
}
