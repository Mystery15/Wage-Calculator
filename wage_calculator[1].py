from dataclasses import dataclass

@dataclass
class WageCalculator:
    __input_hour: int
    __input_rate: float

    @property
    def CalculateWage(self):
        return(self.__input_hour * self.__input_rate)

wage = WageCalculator(10, 3.5)

print(wage.CalculateWage)
