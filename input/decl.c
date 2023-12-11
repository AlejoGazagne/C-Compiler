int f(int i, int t);

int main(){
    int i = 3, o; 
    double t = 2;
    o = f(i, t);
    i = 5;
    i = t;
}

int f(int i, int t){
    return i * t;
}
