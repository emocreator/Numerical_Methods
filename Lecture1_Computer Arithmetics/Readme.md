# Python Numerical Precision and Averaging Experiments

This Python project consists of two classes that demonstrate numerical precision and averaging experiments:

1. **AverageCalculator Class**

   The `AverageCalculator` class provides two methods for calculating the average of a given value over a specified number of values. It includes both a classical averaging method and the Kahan algorithm for improved precision.

   - `calculate_Average`: This method calculates the average using the classical method, where values are summed, and the result is divided by the number of values.

   - `kahan_Average`: This method calculates the average using the Kahan algorithm, which reduces rounding errors in the sum.

   To use this class, create an instance of `AverageCalculator` with the desired value and number of values, then call the appropriate method to calculate the average.

2. **MachinePrecisionExperiment Class**

   The `MachinePrecisionExperiment` class showcases experiments related to machine precision and numerical behavior. It includes experiments on machine epsilon, the maximum representable value, special values, and loss of significance.

   - `showcase_machine_precision`: Demonstrates machine precision by showcasing how tiny values behave when divided repeatedly.

   - `experiment_on_machine_precision`: Conducts experiments on machine epsilon and its behavior in various arithmetic operations.

   - `experiment_on_max_value`: Investigates the behavior of the maximum representable value and arithmetic operations involving large values.

   - `experiment_on_special_values`: Explores special values such as positive zero, negative zero, and infinity.

   - `experiment_on_loss_of_significance`: Demonstrates the concept of loss of significance in numerical computations by solving a quadratic equation with two different methods.

   To use this class, create an instance of `MachinePrecisionExperiment` and call the various experiment methods to observe the behavior of numerical values and operations.

## Summation

1. **Class Definition**:

   - Define a class `AverageCalculator` that takes two parameters, `value` (the value to be averaged) and `numberOfValues` (the number of values to average).

2. **Initialization**:

   - `value`: The value to be averaged.
   - `numberOfValues`: The total number of values to be averaged.

3. **Average Calculation**:

   - To calculate the average, initialize a sum variable, `sum_`, to zero.
   - For each value in the range from 0 to `numberOfValues - 1`, add the `value` to the `sum_`.
   - Calculate the average by dividing the `sum_` by `numberOfValues`.

    Mathematical Notation:

   - Given `value` and `numberOfValues`, the average `averageClassical` can be calculated as follows:

    ```![AverageClassical](https://latex.codecogs.com/svg.image?averageClassical&space;=&space;\sum_{i=0}^{N-1}&space;x_i(1&plus;\delta_i))```

4. **Kahan Algorithm for Average**:

   - Initialize `sum_` and `error` variables to zero.
   - For each value in the range from 0 to `numberOfValues - 1`, perform the following steps:
     - Calculate `newValue` as `value - error`.
     - Calculate `new_Sum` as `sum_ + newValue`.
     - Calculate `error` as `(new_Sum - sum_) - newValue`.
     - Update `sum_` to be `new_Sum`.
   - Calculate the average by dividing `sum_` by `numberOfValues`.

    Mathematical Notation:

   - Given `value` and `numberOfValues`, the average `averageKahanAveg` using the Kahan algorithm can be expressed as follows:

    ![AverageKahan](https://latex.codecogs.com/svg.image?averageKahan&space;=&space;\sum_{i=0}^{N-1}&space;x_i(1&plus;\delta_i)&space;&plus;&space;\left(\mathcal{O}(N\epsilon^2)&space;\cdot&space;\sum_{i=0}^{N-1}&space;|x_i|\right))

This mathematical notation describes the two methods for calculating the average in the `AverageCalculator` class, one using the classical method and the other using the Kahan algorithm.

## Usage

You can use these classes to explore and understand numerical precision in Python and how different averaging methods can affect the accuracy of results. Follow the examples provided in the code to run experiments and analyze the results.

## Dependencies

- Python 3.x
- NumPy (for numerical operations, if needed)