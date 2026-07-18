# Urban Revitalization Policy Matrix Calculator

This Python program uses linear algebra to explore how an urban revitalization policy could affect the long-term distribution of people across four city zones. It models movement between the zones with a **transition matrix** and provides four calculations: checking for an eigenvalue of 1, finding a steady-state distribution, testing a change to the policy, and estimating the rate of convergence.

This is an educational model. Its results describe what happens under the probabilities entered by the user; they do not prove that a real policy will succeed.

## Table of Contents

- [How the model works](#how-the-model-works)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the program](#running-the-program)
- [Input format](#input-format)
- [The four tasks](#the-four-tasks)
- [Understanding the code](#understanding-the-code)
- [Interpreting the results](#interpreting-the-results)
- [Limitations](#limitations)

## How the Model Works

The city is divided into four zones. A population distribution is represented by a column vector:

```text
x = [population share in Zone 1,
     population share in Zone 2,
     population share in Zone 3,
     population share in Zone 4]
```

The program accepts a 4 x 4 transition matrix `A`. The entry `A[i, j]` is the probability that a person currently in Zone `j` will be in Zone `i` after one time step. A time step could represent a month, year, or another period chosen for the study.

The next population distribution is:

```text
x_next = A x
```

Because the model uses column vectors, `A` must be **column-stochastic**:

- every entry must be at least 0;
- every entry represents a probability; and
- the entries in each column must add up to 1.

Each column therefore describes all possible destinations for people starting in one zone.

## Features

- Validates a nonnegative, column-stochastic 4 x 4 matrix
- Checks whether the matrix has an eigenvalue equal to 1
- Calculates a normalized steady-state population vector
- Changes one transition probability and adjusts the corresponding stay-in-place probability
- Reports a second eigenvalue to help discuss convergence
- Provides an interactive command-line menu

## Requirements

- Python 3
- [NumPy](https://numpy.org/)

## Installation

Clone or download this repository, open a terminal in the project folder, and install NumPy:

```bash
python -m pip install numpy
```

## Running the Program

Run:

```bash
python main.py
```

The program first asks for four rows of matrix values. It then displays a menu where tasks 1 through 4 can be selected. After a task finishes, enter `R` to return to the menu or `Q` to quit.

## Input Format

Enter each matrix row as four decimal numbers separated by spaces. For example:

```text
0.70 0.10 0.10 0.05
0.10 0.60 0.20 0.05
0.10 0.20 0.60 0.20
0.10 0.10 0.10 0.70
```

In this example, every column adds to `1.00`. The first column means that, among people starting in Zone 1, 70% remain in Zone 1 and 10% move to each of the other three zones.

The program rejects a matrix if it contains a negative number or if any column does not add to 1 (allowing for small floating-point rounding differences).

## The Four Tasks

### 1. Check for an Eigenvalue of 1

The program calculates the eigenvalues of `A` with `numpy.linalg.eigvals()` and checks for the value 1 after rounding.

An eigenvalue of 1 means there may be a nonzero vector `v` such that:

```text
A v = v
```

Applying the transition matrix does not change this vector. For a finite stochastic matrix, 1 is expected to be an eigenvalue, although floating-point calculations can produce a value extremely close to 1 instead of exactly 1.

### 2. Find the Steady-State Vector

The steady-state vector `v` satisfies:

```text
A v = v
```

Rearranging gives:

```text
(A - I) v = 0
```

This system alone does not choose a scale, so the code replaces its last equation with:

```text
v1 + v2 + v3 + v4 = 1
```

It then uses `numpy.linalg.solve()` to find a normalized vector. Each result can be read as a long-run share of the modeled population. For example, `0.35` for Zone 2 represents 35% of the population, not 35 people.

Some transition matrices have more than one steady state. In that case, the modified system can be singular and the program may report that it cannot find one unique solution.

### 3. Revise the Matrix and Compare Outcomes

This task models a policy change, such as a transportation project that changes movement from one zone to another. The user chooses one matrix entry and supplies a new probability.

To keep that column's total unchanged, the program applies the opposite change to the diagonal entry in the same column. The diagonal represents the probability of remaining in the starting zone. It then calculates the revised steady-state vector.

Compare the new vector with the result from Task 2:

- an increase for a zone means its modeled long-run population share grows;
- a decrease means its modeled long-run share shrinks; and
- a small change suggests that the long-run distribution is not very sensitive to that particular probability change.

The program prints the revised vector but does not automatically print the numerical difference or validate the entire adjusted matrix again.

### 4. Find the Second-Largest Eigenvalue

The eigenvalue with magnitude 1 describes steady-state behavior. Other eigenvalues help describe how quickly repeated transitions approach that behavior. In the usual Markov-chain interpretation, a smaller **second-largest eigenvalue magnitude** generally means faster convergence, while a value close to 1 generally means slower convergence.

The current code sorts the real eigenvalues by their numerical value and prints the second-largest one. This is a simple classroom approximation. A more general implementation should sort eigenvalues by absolute value and handle complex eigenvalues.

## Understanding the Code

The project currently contains one source file, `main.py`:

1. NumPy and its linear-algebra module are imported.
2. A 4 x 4 NumPy array is filled from user input.
3. `A.sum(axis=0)` calculates column sums, while `np.all(A >= 0)` and `np.allclose(...)` validate the matrix.
4. A loop displays the task menu until the user quits.
5. NumPy calculates eigenvalues or solves the steady-state system for the selected task.

Important variables include:

| Variable | Purpose |
|---|---|
| `A` | Original transition matrix |
| `I` | 4 x 4 identity matrix |
| `B` | Equation matrix based on `A - I` |
| `b` | Right-hand-side vector used to normalize the solution |
| `C` | Copy of `A` used for the policy-change calculation |

## Interpreting the Results

The mathematics can help answer questions such as:

- Does the model contain a stable population distribution?
- Which zones receive larger or smaller long-run population shares?
- How does one proposed transportation change affect those shares?
- Does the system approach its long-run distribution quickly or slowly?

A result should always be connected back to the assumptions used to build the matrix. If the transition probabilities are estimates, then the final distribution is also an estimate. A zone gaining population share is not automatically evidence of successful revitalization: affordability, displacement, housing quality, employment, public services, and residents' experiences also matter.

## Limitations

- The model always uses exactly four zones.
- Transition probabilities are assumed to remain constant over time.
- People within the same zone are treated as one group.
- The program models population shares, not births, deaths, migration into the city, or total population growth.
- Task 3 changes only one transition and one stay-in-place probability; some valid policy scenarios require several coordinated changes.
- Task 3 can produce an invalid negative diagonal probability if the requested increase is too large.
- Task 4 is reliable only for matrices whose eigenvalues can be converted to real numbers and does not use eigenvalue magnitude.
- A steady state is not necessarily unique, and convergence to it requires additional mathematical conditions.

## Possible Future Improvements

- Support any square matrix size
- Move each task into a separate function
- Add automated tests and clearer error handling
- Compare original and revised steady states automatically
- Validate the revised matrix before solving it
- Calculate the second-largest eigenvalue by magnitude
- Load transition data from a CSV file and create charts of zone changes

## License

No license has been added to this repository. Add one before others reuse or distribute the code.
