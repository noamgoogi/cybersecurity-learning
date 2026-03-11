#include <iostream>

int main()
{
    char op;
    double num1;
    double num2;
    double result;

    std::cout << "********** Simple Calculator **********\n";
    std::cout << "First number: ";
    std::cin >> num1;

    std::cout << "Second number: ";
    std::cin >> num2;

    std::cout << "Operator: ";
    std::cin >> op;

    result = num1;
    switch(op)
    {
        case '+':
            result += num2;
            std::cout << "result is: " << result << "\n";
            break;
        case '-':
            result -= num2;
            std::cout << "result is: " << result << "\n";
            break;
        case '*':
            result *= num2;
            std::cout << "result is: " << result << "\n";
            break;
        case '/':
            result /= num2;
            std::cout << "result is: " << result << "\n";
            break;
        default:
            std::cout << "Thats wasnt a valid operator!\n";
    }
    std::cout << "***************************************\n";
    return 0;
}