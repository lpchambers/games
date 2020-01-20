#!/usr/bin/python3
import math

class PillType:
    INITIAL_INCOME = 0  # The first level of income
    INITIAL_COST = 0    # The fist cost
    INCOME_SCALE = 1    # How much each income scales
    COST_SCALE = 1      # How much each cost scales (should be < INCOME_SCALE)
    def __init__(self, name):
        self.name = name
        self.income = 0
        self.cost = 0
        self.research_level = 0

    def render(self):
        print(f"Pill:           {self.name}")
        print(f"Income:         {self.income}")
        print(f"Research Level: {self.research_level}")
        print("Research")
        print(f"Research Cost: {self.next_cost}")
        print(f"New Income:    {self.next_income}")

    @property
    def next_cost(self):
        if self.cost == 0:
            return self.INITIAL_COST
        return math.ceil(self.cost * self.COST_SCALE)

    @property
    def next_income(self):
        if self.income == 0:
            return self.INITIAL_INCOME
        return math.ceil(self.income * self.INCOME_SCALE)

class PengPill(PillType):
    def __init__(self):
        PillType.__init__(self, "Peng Pill")


class PengPillPlus(PillType):
    def __init__(self):
        PillType.__init__(self, "Peng Pill Plus")

class PengPillPlusPlus(PillType):
    def __init__(self):
        PillType.__init__(self, "Peng Pill Plus +")

class PengPillLiquid(PillType):
    def __init__(self):
        PillType.__init__(self, "Peng Pill Liquid Capsule")

class PengPillLiquidPlus(PillType):
    def __init__(self):
        PillType.__init__(self, "Peng Pill Plus Liquid Capsule")

PILL_ORDER = [
    PengPill(),
    PengPillPlus(),
    PengPillPlusPlus(),
]

