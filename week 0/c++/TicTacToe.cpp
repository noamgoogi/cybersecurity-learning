#include <iostream>

void printBoard(int board[3][3])
{
    for(int y=0; y<3;y++)
    {
        for(int x=0; x<3;x++)
        {
            std::cout << " | ";
            int cube = board[y][x];
            switch(cube)
            {
                case 1:
                    std::cout << "O";
                    break;
                case 2:
                    std::cout << "X";
                    break;
                default:
                    std::cout << " ";
            }
        }
        std::cout << " |\n";
        std::cout << "\n";
    }
}

bool isSpotEmpty(int spot)
{
    return spot == 0;
}

void changeSpot(int &spot, int value)
{
    if(isSpotEmpty(spot) && (value == 1 || value == 2))
    {
        spot = value;
    }
}

bool didPlayerWin(int board[3][3], int player)
{
    for(int x=0; x<3;x++)
    {
        if (board[x][0] == player && board[x][1] == player && board[x][2] == player)
        {
            return true;
        }
        if (board[0][x] == player && board[1][x] == player && board[2][x] == player)
        {
            return true;
        }
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
    {
        return true;
    }
    if (board[2][0] == player && board[1][1] == player && board[0][2] == player)
    {
        return true;
    }
    return false;
}

void playerTurn(int board[3][3], int player)
{
    int x;
    int y;
    std::cout << "where to place? ";
    std::cin >> x;
    std::cin >> y;
    changeSpot(board[y][x], player);
}
int main()
{
    int board[3][3] = {{0,0,0},
                        {0,0,0},
                        {0,0,0}};

    do
    {
        printBoard(board);
        playerTurn(board, 1);
        if(didPlayerWin(board, 1))
        {
            std::cout << "Player O Won";
            break;
        }
        printBoard(board);
        playerTurn(board, 2);
        if(didPlayerWin(board, 2))
        {
            printBoard(board);
            std::cout << "Player X Won";
            break;
        }
    }while(!didPlayerWin(board, 1) && !didPlayerWin(board, 2));

    return 0;
}
