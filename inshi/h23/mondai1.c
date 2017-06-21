#include<stdio.h>
#include<math.h>

int main (void){
  double start,end;
  double num=10000000.;
  double n=1000000.;
  double S=0;
  int i,j,k;
  double dx;
  double x;

  start=0.;
  end=1./n;

  dx=(end-start)/num;

  for(i=0;i<num;i++){
    x=i*dx;
    S+=n*n*exp(-x*x)*sin(x)*dx;
  }

  printf("S=%lf\n",S);

  return 0;
}
