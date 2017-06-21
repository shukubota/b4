#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main(void){
  int i,j;
  double t;
  FILE*filename,*filename2;
  double v=2.,a=5.;
  double dt=0.01;
  double pi=4.*atan(1.);
  double omega=pi/10.;
  double x,y;

  
  filename=fopen("test.dat","w");
  for(i=0;i<1000;i++){
    t=0.+i*dt;
    x=(a-v*t)*cos(omega*t);
    y=(a-v*t)*sin(omega*t);
    fprintf(filename,"%15.10e %15.10e\n",x,y);
  }
  fclose(filename);

  return 0;
}
