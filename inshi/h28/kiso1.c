#include<stdio.h>
#include<math.h>
#include<complex.h>

int main(void){
  double t,dt;
  double complex s;
  double S;
  int i,j,k;
  int num=1000000000;
  double R=2000.;
  double complex z;
  double pi=4.*atan(1.);

  S=0.;
 dt=R/num;

  for(i=0;i<num;i++){
    t=i*dt;
    S+=dt*1./(1.+t*t*t*t);
  }

  printf("%f\n%f\n",S,0.5/sqrt(2.)*pi);

  return 0;
}
