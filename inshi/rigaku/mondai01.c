//H28 1-1

#include<stdio.h>
#include<math.h>

int main(void){

  double t;
  double sum;
  double result1,result2;
  double dt;
  int step=1000000;
  int i,j,k;
  
  dt=4./step;
  sum=0.;

  for(i=0;i<step;i++){
    t=dt*i;
    sum+=pow(7,sqrt(t))*dt;
  }

  result1=sum;
  result2=196./log(7.)-96./(log(7.)*log(7.));

  printf("%15.10e \n%15.10e\n",result1,result2);

  return 0;
}
  
