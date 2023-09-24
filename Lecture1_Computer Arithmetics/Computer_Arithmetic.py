import sys
import math

class MachinePrecisionExperiment:
    def __init__(self):
        self.tiny       = 1.0
        self.emin       = 2 ** (-1022 - 52)
        self.eps        = 1.0
        self.sudoeps    = pow(2, -52 - 1)
        self.maxval     = sys.float_info.max
        self.bigStep    = 0.49 * pow(2, 1023 - 52)
        self.biggerStep = 0.50 * pow(2, 1023 - 52)
        self.pluszero   = 1.0
        self.minuszero  = -1.0

    def showcase_machine_precision(self):
        print("Showcasing Machine precision.\n")
        while 0 < self.tiny / 2 and self.tiny < 2:
            self.tiny = self.tiny / 2

        print("tiny................. =", self.tiny)
        print("2^{emin-p}tiny....... =", self.emin)
        print("2^{emin-p}tiny....... =", self.tiny / 2 * 2)
        print("2^{emin-p}tiny....... =", self.tiny * 2 / 2)
        print("--" * 40)

    def experiment_on_machine_precision(self):
        print("Experiment on Machine precision.\n")
        while 1 + self.eps > 1 and 1 + 2 * self.eps > 1 + self.eps:
            self.eps = self.eps / 2.0
        print("epsilon.............. =",         self.eps)
        print("2^{-(p+1)}........... =",         self.sudoeps)
        print("1+epsilon............ =", 1 +     self.eps)
        print("1+2*epsilon.......... =", 1 + 2 * self.eps)
        print("1+3*epsilon.......... =", 1 + 3 * self.eps)
        print("1+4*epsilon.......... =", 1 + 4 * self.eps)
        print("1+5*epsilon.......... =", 1 + 5 * self.eps)
        print("1+6*epsilon.......... =", 1 + 6 * self.eps)
        print("1+7*epsilon.......... =", 1 + 7 * self.eps)
        print("--" * 40)

    def experiment_on_max_value(self):
        print("Experiment on MAX_VALUE.\n")
        print("maxValue............. =",   self.maxval)
        print("maxValue + 10000..... =",  (self.maxval + 10000))  # No change
        print("bigStep.............. =",   self.bigStep)
        print("biggerStep........... =",   self.biggerStep)
        print("maxValue + bigStep... =",  (self.maxval + self.bigStep))
        print("maxValue + biggerStep =",  (self.maxval + self.biggerStep))  # Changes to a constant
        print("--" * 40)

    def experiment_on_special_values(self):
        print("Experiment on Special Values.\n")
        while self.pluszero > 0:
            self.pluszero = self.pluszero / 2
        print("pluszero............. =", self.pluszero)

        while self.minuszero < 0:
            self.minuszero = self.minuszero / 2
        print("minuszero............ =", self.minuszero)

        print("+0 == 0  ............ =", self.pluszero == self.minuszero)

        positive_infinity = float('inf')
        negative_infinity = -float('inf')

        print("+Inf - maxval........ =", positive_infinity - self.maxval)
        print("+Inf + Inf........... =", positive_infinity + positive_infinity)
        print("+Inf + -Inf.......... =", positive_infinity + negative_infinity)
        print("--" * 40)

    def experiment_on_loss_of_significance(self):
        print("Experiment on Loss of Significance.\n")
        p = -10000000.0
        q = 1.0

        def get_smallest_root_of_quadratic_equation1(p, q):
            return -p / 2 - math.sqrt(p * p / 4 - q)

        def get_smallest_root_of_quadratic_equation2(p, q):
            return q / (-p / 2 + math.sqrt(p * p / 4 - q))

        x1 = get_smallest_root_of_quadratic_equation1(p, q)
        x2 = get_smallest_root_of_quadratic_equation2(p, q)

        print("....................p =", p)
        print("....................q =", q)
        print("smallest root x1..... =", x1)

        print("x1*x1 + p*x1 + q...... =", (x1 * x1 + p * x1 + q))
        print("\n")

        print("....................p =", p)
        print("....................q =", q)
        print("smallest root x2..... =", x2)
        print("x1*x1 + p*x1 + q...... =", (x2 * x2 + p * x2 + q))


experiment = MachinePrecisionExperiment()

experiment.showcase_machine_precision()
experiment.experiment_on_machine_precision()
experiment.experiment_on_max_value()
experiment.experiment_on_special_values()
experiment.experiment_on_loss_of_significance()
