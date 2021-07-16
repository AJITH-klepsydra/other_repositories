//ANES :- AN Encryption System
// Niranjanprof & Ajith_Klepsydra
//You Can Encrypt and Decrypt a Word using This Code

// Security Key Should be under 84


//Have Fun
//Queries : -Mailme @ niranjannb7777@gmail.com

# include<iostream>
# include<string.h>
using namespace std;
unsigned long long int fact(int); //For Finding Factorial
int assign(char);   //For Converting Character to corresponding Number
char charassign(int);//For Converting Number to corresponding Character
int keycheck(int); //To Check Key Validity
int key;
void en(){ //Encoding the Message
    char message[20]={},encrypted[20]={};
    unsigned long long int TaylorC,Rem,Quo,secret[20]={};
    cout<<"Enter a Word you want to encrypt: ";
    cin>>message;
    Bac:
    cout<<"Enter a Security Key(Not More Than 84): ";
    cin>>key;
    if(keycheck(key)){
        goto Bac;
    }
    for(int i = 0;i<strlen(message);i++){
        TaylorC = assign(message[i])*fact(i+3); //Converting the Message to Taylor Series Constants
        Rem = TaylorC%key; //Finding Remainder to make Encrypted Message

        Quo = TaylorC/key; //Finding Quotient to Make Secret Key
        encrypted[i]=charassign(Rem);//Coverting Remainders to Encrypted Message Keys
        secret[i]=Quo;//Storing the Secret Key
    }
    cout<<"The Encrypted Message is: ";
    cout<<encrypted;
    cout<<endl;
    cout<<"The Secret Key: ";
    for(int i=0;i<strlen(message);i++)
        cout<<secret[i]<<" ";
        
    cout<<endl;;
}
void de(){ //Decoding the Message
    char message[20]={},encrypted[20]={};
    unsigned long long int TaylorC,secret[20]={};
    cout<<"Enter a Decrypted Text: ";
    cin>>encrypted;
    back:
    cout<<"Enter a Security Key used for Encryption(Not More Than 84): ";
    cin>>key;
    if(keycheck(key)){
        goto back;
    }
    cout<<"Enter the Secret Key: ";
    for(int i = 0;i<strlen(encrypted);i++){
        cin>>secret[i];
    }
    for(int i = 0;i<strlen(encrypted);i++){
        TaylorC = key*secret[i]+assign(encrypted[i]);//Finding The Taylor Series Coefficient
        message[i]=charassign(TaylorC/fact(i+3));//Storing the Decoded Message
    }
    cout<<message;
}
int main(){
    int n;
    cout<<"Welcome to                 ________  ________  "<<endl;
    cout<<"     /\\        |\\     |   |         |        " <<endl;
    cout<<"    /  \\       | \\    |   |         |        " <<endl;
    cout<<"   /    \\      |  \\   |   |_____    |________" <<endl;
    cout<<"  /      \\     |   \\  |   |                 |" <<endl;
    cout<<" /--------\\    |    \\ |   |                 |" <<endl;
    cout<<"/          \\   |     \\|   |_______  ________|" <<endl;
    cout<<"                             Klepsydra & Prof"<<endl;
    Start:
    cout<<"Click\n1.Encryption\n2.Decryption"<<endl;
    cin>>n;
    if(n==1){
        en();
    }
    if(n==2){
        de();
    }
    if(n!=1 && n!=2){
        cout<<"Invalid Input"<<endl;
        goto Start;
    }
    cout<<endl;
    cout<<"Hope YOU enjoyed"<<endl<< "Enter 1 To Repeat  ";
    cout<<"Enter any other key to EXIT: ";
    int flag;
    cin>>flag;
    if(flag==1){
        goto Start;
    }
    return 0;
}
unsigned long long int fact(int n){
    if(n==1)
        return 1;
    return (n*fact(n-1));
}
int keycheck(int valid){
    if(valid>84){
        cout<<"Invalid Key(Valid Key Below 84)"<<endl;
        return 1;
    }
    return 0;
}
int assign(char c){
    switch(c){
        case 'A': return 0;
        case 'B': return 1;
        case 'C': return 2;
        case 'D': return 3;
        case 'E': return 4;
        case 'F': return 5;
        case 'G': return 6;
        case 'H': return 7;
        case 'I': return 8;
        case 'J': return 9;
        case 'K': return 10;
        case 'L': return 11;
        case 'M': return 12;
        case 'N': return 13;
        case 'O': return 14;
        case 'P': return 15;
        case 'Q': return 16;
        case 'R': return 17;
        case 'S': return 18;
        case 'T': return 19;
        case 'U': return 20;
        case 'V': return 21;
        case 'W': return 22;
        case 'X': return 23;
        case 'Y': return 24;
        case 'Z': return 25;
        case 'a': return 26;
        case 'b': return 27;
        case 'c': return 28;
        case 'd': return 29;
        case 'e': return 30;
        case 'f': return 31;
        case 'g': return 32;
        case 'h': return 33;
        case 'i': return 34;
        case 'j': return 35;
        case 'k': return 36;
        case 'l': return 37;
        case 'm': return 38;
        case 'n': return 39;
        case 'o': return 40;
        case 'p': return 41;
        case 'q': return 42;
        case 'r': return 43;
        case 's': return 44;
        case 't': return 45;
        case 'u': return 46;
        case 'v': return 47;
        case 'w': return 48;
        case 'x': return 49;
        case 'y': return 50;
        case 'z': return 51;
        case '!': return 52;
        case '"': return 53;
        case '#': return 54;
        case '$': return 55;
        case '%': return 56;
        case '&': return 57;
        case '\'': return 58;
        case '(': return 59;
        case ')': return 60;
        case '*': return 61;
        case '+': return 62;
        case ',': return 63;
        case '-': return 64;
        case '.': return 65;
        case '/': return 66;
        case ':': return 67;
        case ';': return 68;
        case '<': return 69;
        case '=': return 70;
        case '>': return 71;
        case '?': return 72;
        case '@': return 73;
        case '[': return 74;
        case '\\': return 75;
        case ']': return 76;
        case '^': return 77;
        case '_': return 78;
        case '`': return 79;
        case '{': return 80;
        case '|': return 81;
        case '}': return 82;
        case '~': return 83;
        case ' ': return 84;
    }
    return 0;
}
char charassign(int c){
    switch(c){
        case 0: return 'A';
        case 1: return 'B';
        case 2: return 'C';
        case 3: return 'D';
        case 4: return 'E';
        case 5: return 'F';
        case 6: return 'G';
        case 7: return 'H';
        case 8: return 'I';
        case 9: return 'J';
        case 10: return 'K';
        case 11: return 'L';
        case 12: return 'M';
        case 13: return 'N';
        case 14: return 'O';
        case 15: return 'P';
        case 16: return 'Q';
        case 17: return 'R';
        case 18: return 'S';
        case 19: return 'T';
        case 20: return 'U';
        case 21: return 'V';
        case 22: return 'W';
        case 23: return 'X';
        case 24: return 'Y';
        case 25: return 'Z';
        case 26: return 'a';
        case 27: return 'b';
        case 28: return 'c';
        case 29: return 'd';
        case 30: return 'e';
        case 31: return 'f';
        case 32: return 'g';
        case 33: return 'h';
        case 34: return 'i';
        case 35: return 'j';
        case 36: return 'k';
        case 37: return 'l';
        case 38: return 'm';
        case 39: return 'n';
        case 40: return 'o';
        case 41: return 'p';
        case 42: return 'q';
        case 43: return 'r';
        case 44: return 's';
        case 45: return 't';
        case 46: return 'u';
        case 47: return 'v';
        case 48: return 'w';
        case 49: return 'x';
        case 50: return 'y';
        case 51: return 'z';
        case 52: return '!';
        case 53: return '"';
        case 54: return '#';
        case 55: return '$';
        case 56: return '%';
        case 57: return '&';
        case 58: return '\'';
        case 59: return '(';
        case 60: return ')';
        case 61: return '*';
        case 62: return '+';
        case 63: return ',';
        case 64: return '-';
        case 65: return '.';
        case 66: return '/';
        case 67: return ':';
        case 68: return ';';
        case 69: return '<';
        case 70: return '=';
        case 71: return '>';
        case 72: return '?';
        case 73: return '@';
        case 74: return '[';
        case 75: return '\\';
        case 76: return ']';
        case 77: return '^';
        case 78: return '_';
        case 79: return '`';
        case 80: return '{';
        case 81: return '|';
        case 82: return '}';
        case 83: return '~';
        case 84: return ' ';
    }
    return 0;
}
