#include <stdio.h>
#include<math.h>
#include<complex.h>

int main(void){
  double dt,t;
  double complex z;
  double complex J;
  int i;
  int num=10;
  double pi=4.*atan(1.);

  dt=1./num;
  J=0.;

  for(i=0;i<num;i++){
    t=i*dt;
    J+=16.*pi*I*cexp(6.*pi*I*t)/(1.+8.*cexp(6.*pi*I*t))*dt;
  }
  printf("%f\n%f\n",creal(J),cimag(J));

  return 0;
}
