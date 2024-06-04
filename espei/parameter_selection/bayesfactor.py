import numpy as np
from espei.analysis import truncate_arrays
from statistics import harmonic_mean
from decimal import *
import math

def harmonic_mean_estimator(trace_file, lnprob_file, nburn, log=False):
    trace = np.load(trace_file)
    lnprob = np.load(lnprob_file)
    trace, lnprob = truncate_arrays(trace, lnprob)
    samples = np.ascontiguousarray(lnprob[:,nburn:])
    samples_list=[]
    for i in range(0, len(samples)):
        for j in samples[i]:
            samples_list.append(Decimal(j).exp())
    if log == True:
        evidence=Decimal(harmonic_mean(tt)).ln()
        return evidence
    else:
        evidence=Decimal(harmonic_mean(tt))
        return evidence

def bayes_factor_selection(evidence_1, evidence_2, log=False):
    if log == True:
        K=evidence_1.exp()/evidence_2.exp()
        log10_K=math.log10(K)
        if log10_K < 0:
            print('Bayes factor is', log10_K)
            print('Model 2 is favored by data')
        if 0 <= log10_K < 0.5:
            print('Bayes factor is', log10_K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Not worth more than a bare mention')
        if 0.5 <= log10_K < 1:
            print('Bayes factor is', log10_K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Substantial')
        if 1 <= log10_K < 2:
            print('Bayes factor is', log10_K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Strong')
        if log10_K >= 2:
            print('Bayes factor is', log10_K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Decisive')
    else:
        K=evidence_1/evidence_2
        if K < 1:
            print('Bayes factor is', K)
            print('Model 2 is favored by data')
        if 1 <= K < 3.2:
            print('Bayes factor is', K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Not worth more than a bare mention')
        if 3.2 <= K < 10:
            print('Bayes factor is', K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Substantial')
        if 10 <= K < 100:
            print('Bayes factor is', K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Strong')
        if K >= 100:
            print('Bayes factor is', K)
            print('Model 1 is favored by data')
            print('Strength of evidence: Decisive')



