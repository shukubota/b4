//sinz/z^2の複素積分 2pi*Iになるはず

#include<stdio.h>
#include<complex.h>
#include<math.h>

int main(void){
  double complex z;
  double theta;
  double pi=4.*atan(1.);
  int i,j,k;
  int num=10000;
  double dtheta=2.*pi/num;
  FILE*filename;
  double complex S=0.;

  for(i=0;i<num;i++){
    theta=(i+1)*dtheta;
    z=cexp(I*theta);
    S+=I*csin(z)/z*dtheta;
  }
  printf("S=%f+%f i\n",creal(S),cimag(S));

  return 0;
}