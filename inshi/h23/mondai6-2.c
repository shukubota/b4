#include<stdio.h>
#include<math.h>

int main(void){
  double r;
  double theta;
  double dtheta=1.e-2;
  double a=1.;
  int num=220;
  FILE *filename;
  int i,j,k;
  double c=1.e0;
  double omega=1.2;

  theta=0.;
  r=a;
  filename=fopen("mondai6-2.dat","w");

  for(i=0;i<num;i++){
    theta=i*dtheta;
    r=a/cos(sqrt(1.+c/(a*a*a*a*omega*omega))*theta);
    fprintf(filename,"%15.10e %15.10e\n",r,theta);
  }
  fclose(filename);

  return 0;
}
