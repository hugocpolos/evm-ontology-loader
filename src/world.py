from factory import Factory
from enum import Enum
from my_logging import logging


class WorldScenario(Enum):
    scenario_one = 1
    scenario_two = 2
    scenario_three = 3


class World:
    def __init__(self, factory: Factory, scenario: WorldScenario):
        self.f = factory
        self.p = prop_factory
        if scenario == WorldScenario.scenario_one:
            self._scenario_1()
        else:
            logging.error("invalid world scenario")

    def _scenario_1(self):
        self.robot = self.f.nepRobot('robot')

        self.norm_a = self.f.nepNorm('Not allowed to touch the walls')
        self.norm_violation_a = self.f.evmNormViolation('hit the wall')

        self.monitor_a = self.f.evmEthicalBehaviorMonitor('monitor 1')

        self.norm_violation_a.evmis_violation_of.append(self.norm_a)

        self.responsibility_ascription_a = self.f.evmResponsibilityAscription('test')
        self.norm_violation_a.evmelicits.append(self.responsibility_ascription_a)
