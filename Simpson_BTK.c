/*
 * ============================================================================
 *
 *       Filename:  Simpson_BTK.c
 *
 *    Description:  Simpson_BTK function C wrapper for python.
 *
 *        Version:  1.0
 *        Created:  2019/01/19 17:27
 *
 *         Author:  Xia Chen
 *          Email:  xiachen@itp.ac.cn
 *
 * ============================================================================
 */

#include <stdlib.h>
#include <math.h>
#include <complex.h>

void c_BTK_Diff(double E[], int NE, double V[], int NV,
                double T, double Delta, double Gama,
                double Z, double P, double h, double G[])
{
    /* Calculate parameters */
    double *AN = (double *)malloc(sizeof(double)*NE);
    double *BN = (double *)malloc(sizeof(double)*NE);
    double *BP = (double *)malloc(sizeof(double)*NE);
    double *F_E = (double *)malloc(sizeof(double)*NE);
    complex double e_gama, egama2;
    double energy, Delta2, u02, v02, gama2;
    for (int i = 0; i < NE; ++i) {
        e_gama = E[i] - Gama * I;
        egama2 = e_gama * e_gama;
        Delta2 = Delta * Delta;
        energy = creal(csqrt((egama2 - Delta2) / egama2));
        u02 = 0.5 * (1 + energy);
        v02 = 0.5 * (1 - energy);
        gama2 = pow(u02 + Z*Z*energy, 2);
        if (cabs(e_gama) <= Delta) {
            AN[i] = creal(Delta2 / (egama2 + (Delta2 - egama2)*pow(1+2*Z*Z, 2)));
            BN[i] = 1 - AN[i];
            BP[i] = 1;
        } else {
            AN[i] = u02 * v02 / gama2;
            BN[i] = energy*energy * Z*Z * (1 + Z*Z)/gama2;
            BP[i] = BN[i];
        }
        F_E[i] = exp(11.5942*E[i]/T);
    }

    /* Integrate */
    double *II = (double *)malloc(sizeof(double)*NV);
    for (int i = 0; i < NV; ++i) {
        double sum_f_even = 0;
        double sum_f_odd = 0;
        double f0 = 0;
        double fn = 0;
        double F_V = exp(-11.5942*V[i]/T);
        for (int j = 0; j < NE; ++j) {
            double f_e = 1.0/(1+F_E[j]*F_V) - 1.0/(1+F_E[j]);
            double f = ((1-P) * (1 + AN[j] - BN[j]) + P*(1-BP[j]))*f_e;
            if (j == 0) f0 = f;
            else if (j == NE - 1) fn = f;
            else if (j%2 == 0) sum_f_even += f;
            else sum_f_odd += f;
        }
        II[i] = (h/3)*(f0+fn + 2*sum_f_even + 4*sum_f_odd);
    }

    /* Differential */
    G[0] = 1;
    double dInormal = II[NV-1] - II[NV-2];
    for (int i = 0; i < NV-1; ++i)
        G[i+1] = (II[i+1]-II[i]) / dInormal;

    free(AN);
    free(BN);
    free(BP);
    free(F_E);
    free(II);
}

// Linux: gcc -Wall -shared -O3 -lm -o libSimpson_BTK.so Simpson_BTK.c
