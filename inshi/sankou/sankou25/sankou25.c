#include<stdio.h>
#include<math.h>

int main(void){

  double dt,t,J;
  int i,j,k;
  double pi=4.*atan(1.);
  int num=1000;

  dt=2.*pi/num;
  J=0.;

  for(i=0;i<num;i++){
    t=i*dt;
    J+=1./(3.+2.*sin(t))*dt;
  }
  printf("%f\n",J);
  printf("2pi/sqrt(13)=%f\n",2.*pi/sqrt(13.));
  printf("2pi/sqrt(5)=%f\n",2.*pi/sqrt(5.));

  return 0;
}
