# GA-vs-DE-Comparitive-Study_v1
GE vs DA comparative study across 8 benchmark functions

conduct a comparative study, DE vs. GA, over the given Benchmark functions.

You need to conduct a comparative study, DE vs. GA, over the given Benchmark functions.

Control Parameter Settings For DE, let us have Np=100, Cr=0.9, F=0.8 (canonical scheme: DE/rand/1/bin). For GA: Np=100, Cr=0.9, pm=0.01 (single-point crossover) Problems’ dimensions: D=2, 10, 20 Range of variables: [-10,10] Number of runs: 31 Termination condition: Max_NFC= 3000*D

You need to report:

Performance plots (DE and GA, “best fitness error so far” vs. NFCs (over 31 runs), step-size=NP, three plots for D=2,10, 20)
Three tables (for D=2, 10, 20) to compare DE and GA in terms of mean, best, and Std of the collected errors over 31 runs.
You need to submit a PDF file as a report and your codes. Make sure you include a “Conclusion & Discussion” section written by you.
You need to report the best solution (and its fitness value) over 31 runs.
You need to compare DE and GA performances.
Function name Optimal value (f*=f(x*)) Properties

High Conditioned Elliptic Function 100 Unimodal Non-separable Quadratic ill-conditioned
Bent Cigar Function 200 Unimodal Non-separable Smooth but narrow ridge
Discus Function 300 Unimodal Non-separable With one sensitive direction
Rosenbrock’s Function 400 Multi-modal Non-separable Having a very narrow valley from local optimum to global optimum
Ackley’s Function 500 Multi-modal Non-separable
Weierstrass Function 600 Multi-modal Non-separable Continuous but differentiable only on a set of points
Griewank’s Function 700 Multi-modal Rotated Non-separable
Rastrigin’s Function 800 Multi-modal Separable Local optima’s number is huge
