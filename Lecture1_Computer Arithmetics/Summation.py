class AverageCalculator:
    def __init__(self, value, numberOfValues):
        self.value          = value
        self.numberOfValues = numberOfValues

    def calculate_Average(self):
        sum_ = 0.0  # Avoid using 'sum' as a variable name; it's a built-in Python function
        for i in range(self.numberOfValues):
            sum_ += self.value  # As we add a small number to a large number => relative error (error becomes larger)

        average = sum_ / self.numberOfValues
        return average
    
    #Kahan Algorithm
    def kahan_Average(self):
        sum_  = 0.0
        error = 0.0
        for i in range(self.numberOfValues):
            newValue  = value    - error
            new_Sum   = sum_     + newValue
            error     = (new_Sum - sum_)     - newValue
            sum_      = new_Sum
        return sum_/self.numberOfValues

# Create an instance of the AverageCalculator class
value = 0.1
numberOfValues = 10000000
calculator = AverageCalculator(value, numberOfValues)

# Calculate and print the average
averageClassical = calculator.calculate_Average()
averageKahanAveg = calculator.kahan_Average()

print("average using classical ........... =", averageClassical)

print("average using Kahan ............... =", averageKahanAveg)
