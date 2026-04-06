# matrix-calculations-python
About: This is the python implemenation of my linear algebra project that is dedicated towards evaluating an urban revitalization policy. It uses a transition matrix, a matrix that contains the probability of transitioning between different zones. With the use of python and the sympy library, evaluating these plans using matrices and linear algebra has becomes easier and faster. There are four tasks in this python implementation to give results that are useful in interpreting the efficacy of this plan.

Constraints: For this python code to as intended, it must be a 4x4 matrix that is column stochastic (Every element in each column adds to 0), and contains of elements between 0 and 1. 

Here is a quick overview of what each task does and how its results are interpreted

Task 1 (Finding whether an eigenvaluie of 1 exists) - If an eigenvalue of 1 exists, the matrix can be considering an equlibrium population distribution, where there is a population distribution so that if the transition matrix is applied to the population distribution, it does not change the population distribution. This guarantees that the transition matrix will stabilize into a set amount of people within each zone, which is important to evaluate long term effects.

Task 2 (Finding the steady state vector) - A steady state vector represents the population caused by a many, many transitions. The vector will provide the final population distribution, which is useful because it represents the expected change in each zone caused by the plan, so that the goal of revitalizing parts of the city may be achieved. 

Task 3 (Sensitivity Analysis) - If we implement a new transportation plan, we want to know what effects it will have compared to if we did not. This is done by calculating the change in the transition probability between zones. Moving out of a zone will also affect the probability of staying in the zone. Hence, we adjust the matrix to compensate for the change in transitions so that it remains stochastic. We repeat task 2 and get a new steady state vector, that can be compared with the old steady state vector to evaluate changes in population distribution caused by this transportation plan.

Task 4 (Rate of Convergence) - By finding the biggest eigenvalue that is not 1 for a transition matrix, we can determine the speed at which we approach a long term population. Knowing this second largest eigenvalue will allow us to finetune the revitalization plan in order to change the speed at which people settle into the zones without a massive shift in population.

