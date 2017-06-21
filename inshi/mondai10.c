//数学参考10

#include<stdio.h>
#include<math.h>

double fx1(double x1,double x2, double x3){
  return x2*x3;
}

double fx2(double x1,double x2, double x3){
  return -x1*x3;
}

double fx3(double x1,double x2, double x3){
  double k=0.5;
  return -k*k*x1*x2;
}



int main (void){

  double t,x1,x2,x3,v1,v2,v3;
  double kkk;
  double dt=0.01;
  double px1[4],px2[4],px3[4];
  int timestep=1300;
  FILE*filename;
  char name[]="mondai10.dat";
  int i,j,k;

  //initial condition
  t=0.;
  x1=0.;
  x2=1.;
  x3=1.;
  

  

  //time step 
  filename=fopen(name,"w");

  fprintf(filename,"%15.10e %15.10e %15.10e %15.10e\n",t,x1,x2,x3);

  for(i=0;i<timestep;i++){


    v1=fx1(x1,x2,x3);
    v2=fx2(x1,x2,x3);
    v3=fx3(x1,x2,x3);

    px1[0]=v1;
    px2[0]=v2;
    px3[0]=v3;

    px1[1]=fx1(x1+dt/2.*px1[0],x2+dt/2.*px2[0],x3+dt/2.*px3[0]);
    px2[1]=fx2(x1+dt/2.*px1[0],x2+dt/2.*px2[0],x3+dt/2.*px3[0]);
    px3[1]=fx3(x1+dt/2.*px1[0],x2+dt/2.*px2[0],x3+dt/2.*px3[0]);

    px1[2]=fx1(x1+dt/2.*px1[1],x2+dt/2.*px2[1],x3+dt/2.*px3[1]);
    px2[2]=fx2(x1+dt/2.*px1[1],x2+dt/2.*px2[1],x3+dt/2.*px3[1]);
    px3[2]=fx3(x1+dt/2.*px1[1],x2+dt/2.*px2[1],x3+dt/2.*px3[1]);

    px1[3]=fx1(x1+dt*px1[2],x2+dt*px2[2],x3+dt*px3[2]);
    px2[3]=fx2(x1+dt*px1[2],x2+dt*px2[2],x3+dt*px3[2]);
    px3[3]=fx3(x1+dt*px1[2],x2+dt*px2[2],x3+dt*px3[2]);

    x1+=1./6.*dt*(px1[0]+2.*px1[1]+2.*px1[2]+px1[3]);
    x2+=1./6.*dt*(px2[0]+2.*px2[1]+2.*px2[2]+px2[3]);
    x3+=1./6.*dt*(px3[0]+2.*px3[1]+2.*px3[2]+px3[3]);
    

    t+=dt;

    fprintf(filename,"%15.10e %15.10e %15.10e %15.10e\n",t,x1,x2,x3);

  }

  kkk=sqrt(1.+fx3(1.,1.,1.));
  printf("%15.10e\n",kkk);
  return 0;
}
