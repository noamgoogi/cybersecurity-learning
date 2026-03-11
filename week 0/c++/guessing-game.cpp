#include <iostream>

int main()
{
    int range;
    int num;
    int guess;
    int tries = 0;
    
    srand(time(NULL));
    
    std::cout << "Enter range (1 -> ?): ";
    std::cin >> range;
    num = (rand() % range) + 1;
    do
    {
        std::cout << "Enter you guess? (1-" << range << ")";
        std::cin >> guess;
        tries ++;
        if(guess > num)
        {
            std::cout << "TO HIGH!\n";
        }
        else if(guess < num)
        {
            std::cout << "to low!\n";
        }
    }while(guess != num);

    std::cout << "You guessed right! the number is: " << guess << "\nyou guessed in the " << tries << " try\n";
    
    return 0;
}