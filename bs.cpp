#include<bits/stdc++.h>
using namespace std;

int bs(int arr[],int l,int r,int k)
{


    if(r>=l){

            int mid=(l+r)/2;
    if(arr[mid]==k){
       return mid;
    }
    if(arr[mid]>k){
          return bs(arr,l,mid-1,k);
          }
    else{
         return bs(arr,mid+1,r,k);
    }

    }

  return -1;
}

int main()
{

    int arr[]={5,6,7,9,10,45};
    int n=sizeof(arr)/sizeof(arr[0]);

    cout<<bs(arr,0,n-1,9);
}
