double restar(double a, double b);
int suma(int num1, int num2);

int main()
{
    int num1 = 200;
    int num2 = 48;

    double numero3 = 28.5;
    double numero4 = 33.5;

    double resultadoResta = restar(numero4, numero3);
    int res = suma(num1, num2);

    return 5;
}

double restar(double a, double b)
{
    int resultado = 0;

    resultado = a - b;

    return resultado;
}

int suma(int num1, int num2){
    int res = 0;
    res = num1 + num2;
    return res;
}