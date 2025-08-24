// ----------------------------------------------------------------------------------------------------
// Title          : C++ program for Tic-Tac-Toe game
// File Name      : gdzdguw.cpp
// Compiled       : g++ (Ubuntu 14.2.0-19ubuntu2) 14.2.0
// Author         : GoDarda
// License        : GNU General Public License
// ----------------------------------------------------------------------------------------------------

#include<iostream>
#include<string>
using namespace std;
class TicTacToe
{
    private:
    char table[3][3];
    public:
    TicTacToe()
    {

    }
    void setBoard()
    {
        int n=1;
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                table[i][j]='0'+n;
                n++;
            }
        }
    }

    void showBoard()
    {
        cout<<"__________\n";
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            if(j<2)
            {
                cout<<table[i][j]<<" | ";
            }
            else
            {
                cout<<table[i][j]<<endl;
            }
            if(i<2)
            {
                cout<<"--+---+--\n";
            }
        }
        cout<<"__________\n\n";
    }

    void playerMove(char num,char player)
    {
        bool wrongMove=true;
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(table[i][j]==num)
                {
                    table[i][j]=player;
                    wrongMove=false;
                }
            }
        }
        if(wrongMove==true)
        {
            cout<<"\nWrong Move\n\n";
        }
    }

    bool checkWinner(char player,bool gameOver)
    {
        for(int i=0;i<3;i++)
            if(table[i][0]==table[i][1]&&table[i][1]==table[i][2])
                gameOver=true;
        for(int i=0;i<3;i++)
            if(table[0][i]==table[1][i]&&table[1][i]==table[2][i])
                gameOver=true;
        if(table[0][0]==table[1][1]&&table[1][1]==table[2][2])
            gameOver=true;
        if(table[0][2]==table[1][1]&&table[1][1]==table[2][0])
            gameOver=true;
        if(gameOver==true)
        {
            cout<<"Player "<<player<<" wins!\n\n";
        }
        return gameOver;
    }

    bool checkDraw(bool gameOver)
    {
        int n=1,count=0;
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                if(table[i][j]=='0'+n)
                {
                    count++;
                }
                n++;
            }
        }
        if(count<1)
        {
            cout<<"It's draw!\n\n";
            gameOver=true;
        }
        return gameOver;
    }
};

int main()
{
    bool done=false,gameOver=false;
    char player='O',num;
    TicTacToe myGame;
    myGame.setBoard();
    do
    {
        if(player=='X')
        {
            player='O';
        }
        else
        {
            player='X';
        }
        myGame.showBoard();
        cout<<"Player \""<<player<<"\" turn> ";
        cin>>num;
        cout<<"\n";
        if(num=='q')
        {
            cout<<"Exit\n";
            break;
        }
        myGame.playerMove(num,player);
        gameOver=myGame.checkWinner(player,gameOver);
        gameOver=myGame.checkDraw(gameOver);
        if(gameOver==true)
        {
            myGame.setBoard();
            gameOver=false;
        }
    }while(!done);
    return 0;
}
