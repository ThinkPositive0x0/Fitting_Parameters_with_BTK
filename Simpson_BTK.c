/*
 * ============================================================================
 *
 *       Filename:  Simpson_BTK.c
 *
 *    Description:  C version of Simpson_BTK.py
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
#include "BTK.h"

void calculate_parameters(double E[], int n, double Delta, double Gama, double Z, double T,
                          double AN[], double BN[], double BP[], double F_E[])
{
    complex double e_gama, egama2;
    double energy, Delta2, u02, v02, gama2;
    int i;
    for (i = 0; i < n; ++i) {
        e_gama = E[i] - Gama * I;
        egama2 = e_gama * e_gama;
        Delta2 = Delta * Delta;
        energy = creal(csqrt((egama2 - Delta2) / egama2));
        u02 = 0.5 * (1 + energy);
        v02 = 0.5 * (1 - energy);
        gama2 = u02 + Z*Z*energy*energy;
        if (cabs(e_gama) <= Delta) {
            AN[i] = creal(Delta2 / (egama2 + (Delta2 - egama2)*pow(1+2*Z*Z, 2)));
            BN[i] = 1 - AN[i];
            BP[i] = 1;
        } else {
            AN[i] = u02 * v02 / gama2



