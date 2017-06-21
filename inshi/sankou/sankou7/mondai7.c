#include<stdio.h>
int main(void){
  int n;
  double sum=0.;
  int i;

  printf("input natural number\n");
  scanf("%d",&n);


  for(i=1;i<=n;i++){
    sum+=1./i;
  }

  printf("sigma1_%d=%f\n",n,sum);
  return 0;
}
