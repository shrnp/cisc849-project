import pandas as pd
from itertools import combinations
from functools import reduce
import random

def overall_exposure(p_values):
    p_values = list(map(float, p_values))
    if len(p_values) == 1:
        return p_values[0]
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
    
    def __init__(self, s, e, r):
        self.social_eagerness = s
        self.exposure_chance = e
        self.risk_factor = r

    def value(self):
        return self.risk_factor/(self.social_eagerness * self.exposure)

    def coalition_payoff(self, coalition):
        members = coalition.members
        if len(members) == 1 and members[0] == self:
            return self.value()
        else:
            exposures_list = [o.exposure_chance for o in list(set().union(members, [self]))]
            coalition_exposure = overall_exposure(exposures_list)
            return pow(self.social_eagerness, 1 - risk_factor) / pow(coalition_exposure, risk_factor)

class Coalition:
    members = []
    idnum = -1

    def __init__(self, m, i):
        self.members = m
        self.idnum = i
    
class World:
    agent_set = []
    coalition_set = []

    def __init__(self):
        self.agent_set = []
        for i in range(0, NUM_AGENTS):
            self.agent_set.append(Household(random.uniform(MIN_SOC,  MAX_SOC),
                                            random.uniform(MIN_EX,   MAX_EX),
                                            random.uniform(MIN_RISK, MAX_RISK)))
        self.coalition_set = []
        for a in self.agent_set:
            self.coalition_set.append(Coalition([a], i))

    def move_to(self, agent, coalition_id):
        for c in self.coalition_set:
            if c.idnum == coalition_id:
                if agent not in c.members:
                    c.members.append(agent)
            elif agent in c.members:
                c.members.remove(agent)
        return None

    def current_coalition(self, agent):
        for c in coalition_set:
            if agent in c.members:
                return c
        return None
    
    def best_coalition(self, agent):
        active_coalitions = []
        for c in self.coalition_set:
            if c.members:
                active_coalitions.append(c)
        best_coalition_id = -1
        max_payoff = -1
        for c in active_coalitions:
            cur_payoff = agent.coalition_payoff(c)
            if cur_payoff > max_payoff:
                best_coalition_id = c.idnum
                max_payoff = cur_payoff
        return best_coalition_id
                
    def simulate(self):
        for i in range(0, MAX_TIMESTEPS):
            # simulation main loop
            random.shuffle(self.agent_set)
            for a in self.agent_set:
                best = self.best_coalition(a)
                cur = self.current_coalition(a)
                if best != cur:
                    self.move_to(a, best)
                # determine coalition with the highest value
                # compare highest value to self.
                # if self is best, leave coalition/stay alone
                # if a coalition is best, join it/stay if already there
            if i % 15 == 0:
                print(self.coalition_set)
        
NUM_AGENTS = 20
MAX_TIMESTEPS = 500

MIN_SOC = 0
MAX_SOC = 1
MIN_EX = 0.01
MAX_EX = 0.10
MIN_RISK = 0
MAX_RISK = 1    
    
assert overall_exposure([0.5, 0.2]) == 0.6
assert overall_exposure([0.5, 0.2, 0.3]) == 0.72

world_1 = World()
world_1.simulate()

