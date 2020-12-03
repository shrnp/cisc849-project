import pandas as pd
from itertools import combinations
from functools import reduce
import random

def overall_exposure(p_values):
    p_values = list(map(float, p_values))
    overall_prob = sum(p_values)
    for i in range(1, len(p_values)):
        combos = list(combinations(p_values, i + 1))
        for comb in combos:
            overall_prob += pow(-1, i)*reduce((lambda x, y: x*y), comb)
    return overall_prob

class Household:
    social_eagerness = 0
    exposure_chance = 0
    risk_factor = 0
    
    def __init__(self, s, e, r, c):
        self.social_eagerness = s
        self.exposure_chance = e
        self.risk_factor = r
        self.coalition_id = c

    def value(self):
        return 1/(self.social_eagerness * self.exposure)

    def coalition_payoff(self, members):
        exposures_list = [o.exposure_chance for o in members.append(self)]
        coalition_exposure = overall_exposure(exposures_list)
        return pow(self.social_eagerness, 1 - risk_factor) / pow(coalition_exposure, risk_factor)

    def set_preferred_coaliton(self, coalition_set):
        max_coalition_payoff = -1
        for a in agent_set:
            payoff = 0 # Need to finish this function
        return None

class Coalition:
    members = []

    def __init__(self, m):
        self.members = m

    def merge(self, other):
        self.members += other.members

class World:
    agent_set = []
    coalition_set = []

    def __init__(self, a, c):
        self.agent_set = a
        self.coalition_set = c
        
NUM_AGENTS = 20
MAX_TIMESTEPS = 500

MIN_SOC = 0
MAX_SOC = 1
MIN_EX = 0.01
MAX_EX = 0.10
MIN_RISK = 0
MAX_RISK = 1

agent_set = []
for i in range(0, NUM_AGENTS):
    agent_set.append(Household(random.uniform(MIN_SOC,  MAX_SOC),
                               random.uniform(MIN_EX,   MAX_EX),
                               random.uniform(MIN_RISK, MAX_RISK)))

    
for i in range(0, MAX_TIMESTEPS):
    
    
assert overall_exposure(0.5, 0.2) == 0.6
assert overall_exposure(0.5, 0.2, 0.3) == 0.72
