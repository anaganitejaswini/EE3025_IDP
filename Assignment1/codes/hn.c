# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>

int main(){
	int n = (1<<20);
	FILE *fout;
    // when input is impulse output(y) is h(n).
	double* y = (double*)malloc(n * sizeof(double)); 
	double a[] = {1,-2.52,2.56,-1.206,0.22013};
	double b[] = {0.00345,0.0138,0.020725,0.0138,0.00345};
	int count=0;
	
    y[0] = (b[0]/a[0]);
	y[1] = (1/a[0])*(b[1] - a[1]*y[0]);
	y[2] = (1/a[0])*(b[2]- a[1]*y[1]-a[2]*y[0]);
	y[3] = (1/a[0])*(b[3] - a[1]*y[2]-a[2]*y[1]-a[3]*y[0]);
	y[4] = (1/a[0])*(b[4] - a[1]*y[3]-a[2]*y[2]-a[3]*y[1]-a[4]*y[0]);
    for(int i=5;i<n;i++){
		y[i] = (1/a[0])*(0 - a[1]*y[i-1]-a[2]*y[i-2]-a[3]*y[i-3]-a[4]*y[i-4]);
	}
    fout  = fopen("../data/hn.dat", "w");
    for(int i = 0; i < n; i++){
        fprintf(fout, "%lf \n", y[i]);
        //printf("%lf", y[i]);
    }
    fclose(fout);
    
    return 0;
}