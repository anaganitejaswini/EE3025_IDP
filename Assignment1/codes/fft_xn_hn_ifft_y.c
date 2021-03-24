#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <complex.h>
#include <string.h>

#define PI 3.14159265358979323846

void fft_radix(double* x, double complex* X, unsigned int N, unsigned int s) {
    unsigned int k;
    double complex t;

    // BASE CASE
    if (N == 1) {
        X[0] = x[0];
        return;
    }

    // recursively split in two, then combine beneath.
    fft_radix(x, X, N/2, 2*s);
    fft_radix(x+s, X + N/2, N/2, 2*s);

    for (k = 0; k < N/2; k++) {
        t = X[k];
        X[k] = t + cexp(-2 * PI * I * k / N) * X[k + N/2];
        X[k + N/2] = t - cexp(-2 * PI * I * k / N) * X[k + N/2];
    }
}

//FFT
void fft(double* x, double complex* X, unsigned int N) {
    fft_radix(x, X, N, 1);
}

void ifft_radix(double complex* x, double complex* X, unsigned int N, unsigned int s) {
    unsigned int k;
    double complex t;

    // BASE CASE
    if (N == 1) {
        X[0] = x[0];
        return;
    }

    // recursively split in two, then combine beneath.
    ifft_radix(x, X, N/2, 2*s);
    ifft_radix(x+s, X + N/2, N/2, 2*s);

    for (k = 0; k < N/2; k++) {
        t = X[k];
        X[k] = t + cexp(2 * PI * I * k / N) * X[k + N/2];
        X[k + N/2] = t - cexp(2 * PI * I * k / N) * X[k + N/2];
    }
}

//IFFT
void ifft(double complex* x, double complex* X, unsigned int N) {
    ifft_radix(x, X, N, 1);
}

int main(){
    int n= (1<<20);
    double* x = (double*)malloc(n * sizeof(double));
    double* h = (double*)malloc(n * sizeof(double));
    
    double complex* X = (double complex*)malloc(n * sizeof(double complex));
    double complex* H = (double complex*)malloc(n * sizeof(double complex));
    double complex* Y = (double complex*)malloc(n * sizeof(double complex));
    double complex* ifft_Y = (double complex*)malloc(n * sizeof(double complex));
    
    FILE *fin1,*fin2,*fout1,*fout2,*fout3;

    fin1 = fopen("../data/x.dat","r");
    int count=0;
	while (!feof(fin1) && count < n) 
    {
        fscanf(fin1, "%lf", &(x[count++]));
    }
    fft(x,X,n);
    fout1 = fopen("../data/Xfft.dat","w");
    for(int i=0;i<n;i++){
        fprintf(fout1,"%lf+%lfi \n",creal(X[i]),cimag(X[i]));
    }


    fin2 = fopen("../data/hn.dat","r");
    count=0;
    while (!feof(fin2) && count < n) 
    {
        fscanf(fin2, "%lf", &(h[count++]));

    }

    fft(h,H,n);
    fout2 = fopen("../data/Hfft.dat","w");
    for(int i=0;i<n;i++){
        fprintf(fout2,"%lf+%lfi \n",creal(H[i]),cimag(H[i]));
    }

    for(int i=0;i<n;i++)
	{
		Y[i] = H[i]*X[i];
	}

    ifft(Y,ifft_Y,n);
    fout3 = fopen("../data/ifft_y.dat","w");
    for(int i=0;i<n;i++){
        fprintf(fout3,"%lf \n",creal(ifft_Y[i]/n));
    }

    fclose(fin1);
    fclose(fin2);
    fclose(fout1);
    fclose(fout2);
    fclose(fout3);
    return 0;
    
}