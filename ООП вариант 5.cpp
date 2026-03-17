#include <bits/stdc++.h>
using namespace std;
class Apartment{
    private:
        int flat_number;
        double S;
        int human_number;
        double debt;
    public:
        Apartment(){
            flat_number = 1;
            S = 1;
            human_number = 0;
            debt = 0;
        };
         Apartment(int number, double s, int human, double d){
            flat_number = number;
            S = s;
            human_number = human;
            debt = d;
        };
        ~Apartment(){
            cout<<"объект уничтожен"<<endl;
        };
        int getNumber(){
            return flat_number;
        };
        double getS(){
            return S;
        };
        int getHuman(){
            return human_number;
        };
        double getDebt(){
            return debt;
        };
        void setNumber(int number){
            if (number > 0){
                flat_number = number;
            }
            else{
                flat_number = 1;
                cout << "Номер квартиры не может быть меньше 1" << endl;
            };
        };
        void setS(double s){
            if (s > 0){
                S = s;
            }
            else{
                S = 1;
                cout << "Площадь квартиры не может быть 0 или отрицательной" << endl;
            };
        };
        void setHuman(int human){
            if (human >= 0){
                human_number = human;
            }
            else{
                human_number = 0;
                cout << "Количество жильцов в квартире не может быть отрицательным" << endl;
            };
        };
        void setDebt(double d){
            if (d >= 0){
                debt = d;
            }
            else{
                debt = 0;
                cout << "Долг не может быть отрицательным" << endl;
            };
        };
        void printInfo(){
            cout << flat_number << endl;
            cout << S << endl;
            cout << human_number << endl;
            cout << debt << endl;
        };
        void bill(double b){
            if (b > 0){
                debt += b*S;
            }
            else{
                cout << "Счет не может быть 0 или отрицательным" << endl;
            };
        };
        void pay(double p){
            if (p > 0){
                debt -= p;
            }
            else{
                cout << "Оплата не может быть 0 или отрицательной" << endl;
            };
        };
};
int main() {
	Apartment a;
	Apartment m(5, 100, 5, 0);
	a.getNumber();
	a.getHuman();
	a.getS();
	a.getDebt();
	a.setNumber(-2);
	a.setHuman(-1);
	a.setS(-1);
	a.setDebt(-1);
	m.printInfo();
	m.bill(-3);
	m.bill(50);
	m.printInfo();
	m.pay(-576);
	m.pay(12);
	m.printInfo();
}
