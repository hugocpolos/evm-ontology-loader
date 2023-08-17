from evm_instances import EvmInstances


class MyOntologyReader:
    evmEventCausation_instances = None
    evmResponsibilityAscription_instances = None
    evmAscriptionJustelification_instances = None
    evmGroundsForAscription_instances = None
    evmAgentAccountability_instances = None
    evmNormViolationIncident_instances = None
    evmEthicalBehaviorMonitor_instances = None
    evmNormViolation_instances = None
    evmSocioTechnologyGovernance_instances = None
    evmLiabilitySanction_instances = None
    evmLegalResponsibilityAscription_instances = None
    evmgovernance_levels_instances = None
    evmresponsibility_extent_instances = None
    evmAccountablePerson_instances = None
    evmDistributedResponsibility_instances = None
    evmEnumDataTypes_instances = None
    evmEthicalResponsibilityAscription_instances = None
    evmlegal_liabilities_instances = None

    def __init__(self, ontology):
        for cls in ontology.world.classes():
            self._initialize_ontology_class(cls)

    def _initialize_ontology_class(self, cls):
        name = cls.name
        if name == 'evmEventCausation':
            self.evmEventCausation_instances = EvmInstances(cls)
        elif name == 'evmResponsibilityAscription':
            self.evmResponsibilityAscription_instances = EvmInstances(cls)
        elif name == 'evmAscriptionJustification':
            self.evmAscriptionJustelification_instances = EvmInstances(cls)
        elif name == 'evmGroundsForAscription':
            self.evmGroundsForAscription_instances = EvmInstances(cls)
        elif name == 'evmAgentAccountability':
            self.evmAgentAccountability_instances = EvmInstances(cls)
        elif name == 'evmNormViolationIncident':
            self.evmNormViolationIncident_instances = EvmInstances(cls)
        elif name == 'evmEthicalBehaviorMonitor':
            self.evmEthicalBehaviorMonitor_instances = EvmInstances(cls)
        elif name == 'evmNormViolation':
            self.evmNormViolation_instances = EvmInstances(cls)
        elif name == 'evmSocioTechnologyGovernance':
            self.evmSocioTechnologyGovernance_instances = EvmInstances(cls)
        elif name == 'evmLiabilitySanction':
            self.evmLiabilitySanction_instances = EvmInstances(cls)
        elif name == 'evmLegalResponsibilityAscription':
            self.evmLegalResponsibilityAscription_instances = EvmInstances(cls)
        elif name == 'evmgovernance_levels':
            self.evmgovernance_levels_instances = EvmInstances(cls)
        elif name == 'evmresponsibility_extent':
            self.evmresponsibility_extent_instances = EvmInstances(cls)
        elif name == 'evmAccountablePerson':
            self.evmAccountablePerson_instances = EvmInstances(cls)
        elif name == 'evmDistributedResponsibility':
            self.evmDistributedResponsibility_instances = EvmInstances(cls)
        elif name == 'evmEnumDataTypes':
            self.evmEnumDataTypes_instances = EvmInstances(cls)
        elif name == 'evmEthicalResponsibilityAscription':
            self.evmEthicalResponsibilityAscription_instances = EvmInstances(cls)
        elif name == 'evmlegal_liabilities':
            self.evmlegal_liabilities_instances = EvmInstances(cls)

        elif name == 'nepAgent':
            self.nepAgent_intances = EvmInstances(cls)
        elif name == 'nepAgentAction':
            self.nepAgentAction_instances = EvmInstances(cls)
        elif name == 'nepGovernment':
            self.nepGovernment_instances = EvmInstances(cls)
        elif name == 'nepAgentRole':
            self.nepAgentRole_instances = EvmInstances(cls)
        elif name == 'nepNorm':
            self.nepNorm_instances = EvmInstances(cls)
        elif name == 'nepSituation':
            self.nepSituation_instances = EvmInstances(cls)
        elif name == 'nepRobot':
            self.nepRobot_instances = EvmInstances(cls)
        elif name == 'nepTeam':
            self.nepTeam_instances = EvmInstances(cls)
        elif name == 'nepPlanAction':
            self.nepPlanAction_instances = EvmInstances(cls)
        elif name == 'nepEthicalPrinciple':
            self.nepEthicalPrinciple_instances = EvmInstances(cls)
        elif name == 'nepDerogation':
            self.nepDerogation_instances = EvmInstances(cls)
        elif name == 'nepAgentPlan':
            self.nepAgentPlan_instances = EvmInstances(cls)
        elif name == 'nepnorm_category':
            self.nepnorm_category_instances = EvmInstances(cls)
        elif name == 'nepEthicalDilemma':
            self.nepEthicalDilemma_instances = EvmInstances(cls)
        elif name == 'nepEthicalTheory':
            self.nepEthicalTheory_instances = EvmInstances(cls)
        elif name == 'nepSituationPlanRepertoire':
            self.nepSituationPlanRepertoire_instances = EvmInstances(cls)
        elif name == 'nepTaskAssignment':
            self.nepTaskAssignment_instances = EvmInstances(cls)
        elif name == 'nepSocialCollection':
            self.nepSocialCollection_instances = EvmInstances(cls)
        elif name == 'nepEnvironment':
            self.nepEnvironment_instances = EvmInstances(cls)
        elif name == 'nepAnswer':
            self.nepAnswer_instances = EvmInstances(cls)
        elif name == 'nepQuery':
            self.nepQuery_instances = EvmInstances(cls)
        elif name == 'nepActionRationale':
            self.nepActionRationale_instances = EvmInstances(cls)
        elif name == 'nepDilemmaMitigationPrinciple':
            self.nepDilemmaMitigationPrinciple_instances = EvmInstances(cls)
        elif name == 'nepnorm_states':
            self.nepnorm_states_instances = EvmInstances(cls)
        elif name == 'nepteam_types':
            self.nepteam_types_instances = EvmInstances(cls)
        elif name == 'nepCommunity':
            self.nepCommunity_instances = EvmInstances(cls)
        elif name == 'nepCompany':
            self.nepCompany_instances = EvmInstances(cls)
        elif name == 'nepConsequentialistNorm':
            self.nepConsequentialistNorm_instances = EvmInstances(cls)
        elif name == 'nepDeontologicalNorm':
            self.nepDeontologicalNorm_instances = EvmInstances(cls)
        elif name == 'nepDepartment':
            self.nepDepartment_instances = EvmInstances(cls)
        elif name == 'nepEnumDataTypes':
            self.nepEnumDataTypes_instances = EvmInstances(cls)
        elif name == 'nepExplanation':
            self.nepExplanation_instances = EvmInstances(cls)
        elif name == 'nepObligation':
            self.nepObligation_instances = EvmInstances(cls)
        elif name == 'nepOrganization':
            self.nepOrganization_instances = EvmInstances(cls)
        elif name == 'nepPermission':
            self.nepPermission_instances = EvmInstances(cls)
        elif name == 'nepProhibition':
            self.nepProhibition_instances = EvmInstances(cls)
        elif name == 'nepVirtuousNorm':
            self.nepVirtuousNorm_instances = EvmInstances(cls)
        elif name == 'nepautonomous_action_principles':
            self.nepautonomous_action_principles_instances = EvmInstances(cls)
        elif name == 'nepdilemma_mitigation_principles':
            self.nepdilemma_mitigation_principles_instances = EvmInstances(cls)
        elif name == 'nepethical_principles':
            self.nepethical_principles_instances = EvmInstances(cls)
        elif name == 'nepethical_theories':
            self.nepethical_theories_instances = EvmInstances(cls)
