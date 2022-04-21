#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

map<int, string> itos = {
    {0," "},
    {1,"A"},
    {2,"B"},
    {3,"C"},
    {4,"D"},
    {5,"E"},
    {6,"F"},
    {7,"G"},
    {8,"H"},
    {9,"I"},
    {10,"J"}
};

int inputplayercpu(){
    int n;
    cout<<"human player or cpu"<<endl;
    cin>>n;
    if(n==1){
        cout<<"human player chosen"<<endl;
    }
    else{
        cout<<"cpu chosen"<<endl;
    }
    return n;
}

int inputsize(){
    int n;
    cout<<"size of board"<<endl;
    cin>>n;
    if(n<=0){
        cout<<"invalid size"<<endl;
    }
    return n;
}

void drawhline(int sz){
    cout<<endl;
    for(int i=0;i<=sz;i++){
        cout<<"+---";
    }
    cout<<"+"<<endl;
}

void drawBoard(vector<vector<string>> v){
    int sz=v.size();

    for(int i=0;i<=sz;i++){
        cout<<"| "<<itos[i]<<" ";
    }
    cout<<"|";
    drawhline(sz);
     for(int i=0;i<sz;i++){
         for(int j=0;j<=sz;j++){
            if(j==0){
                cout<<"| "<<i+1<<" ";
            }
            else{
                cout<<"| "<<v[i][j-1]<<" ";
            }
         }
         cout<<"|";
         drawhline(sz);
     }
}

vector<vector<string>> generateBoard(int n_pieces, int size){
    string p1 = "b"; 
    int p1_c1 = rand() % size;
    int p1_c2 = rand() % size;
    string p2 = "q"; 
    int p2_c1 = rand() % size;
    int p2_c2 = rand() % size;
    //validate moves

    vector<vector<string>> board(size,vector<string>(size, " "));

    /*for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            if(i==p1_c1 && j==p1_c2){
                board[i].push_back(p1);
            }
            else if(i==p2_c1 && j==p2_c2){
                board[i].push_back(p2);
            }
            else{
                board[i].push_back(" ");
            }
        }
        board.push_back(board[i]);
    }*/

    board[p1_c1][p1_c2]=p1;
    board[p2_c1][p2_c2]=p2;

    return board;
}

vector<int> make_play(int size){
    string move;
    int move_x, move_y;
    bool validMove=false;

    while(!validMove){
        cout<<"input move:"<<endl;
        cin>>move;
        cout<<"move read"<<endl;
        if(move.length()==2){
            move_x = ((int)(move.at(0)))-65;
            move_y = (int)(move.at(1))-49;
            if((move_x >=0 && move_y<=size) || (move_x>=0 && move_y<=size)){
                validMove=true;
            }
            else{
                cout<<"invalid move!"<<endl;
            }
        }
    }
    
    vector<int> ret = {move_x,move_y};
    return ret;
}

bool eval_move(int move_x, int move_y, vector<vector<string>> board){
    return true;
}

void do_move(unsigned move_x, unsigned move_y, vector<vector<string>>& board){
    board[move_y][move_x]="O";
}

int checkBoard(vector<vector<string>> board){
    return 0;
}


int main(){
    //drawBoard({{"a","b","c"},{"d","e","f"},{"g","h","i"}});
    //figures={pawn,tower,horse,bishop,queen,king}
    int size;
    size = inputsize();
    vector<vector<string>> initialboard;
    vector<vector<string>> board;

    int n_pieces=2;
    initialboard=generateBoard(n_pieces,size);
    //if whole move wrong
    board=initialboard;
    int gameOver=0;
    vector<int> move;
    bool validMove = false;

    while(gameOver==0){
        while(!validMove){
            move = make_play(size);
            validMove = eval_move(move[0],move[1],board);
        }
        validMove=false;
        do_move(move[0],move[1],board);
        drawBoard(board);


        gameOver = checkBoard(board);
        if(gameOver==1){
            cout<<"Good job!"<<endl;
        }
        else if (gameOver==2){
            cout<<"Try again!"<<endl;
            board=initialboard;
        }
    }
    return 0;
}