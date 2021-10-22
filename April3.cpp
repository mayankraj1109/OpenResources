#include<bits/stdc++.h>
using namespace std;

int main()
{

    int t;
    cin>>t;
    int n,k;
    cin>>n>>k;
    string s;
    cin>>s;
    string m="";
    m=string(k,'*');
    while(t--)
    {

        if(s.find(m)==-1)
            cout<<"No";
        else
            cout<<"Yes";
    }
}
