class Factory:
    def __init__(self, ontology):
        for cls in ontology.world.classes():
            self._initialize_ontology_factory(cls)

    def _initialize_ontology_factory(self, cls):
        name = cls.name
        if name == 'evmEventCausation':
            self.evmEventCausation = cls
        elif name == 'evmResponsibilityAscription':
            self.evmResponsibilityAscription = cls
        elif name == 'evmAscriptionJustification':
            self.evmAscriptionJustification = cls
        elif name == 'evmGroundsForAscription':
            self.evmGroundsForAscription = cls
        elif name == 'evmAgentAccountability':
            self.evmAgentAccountability = cls
        elif name == 'evmNormViolationIncident':
            self.evmNormViolationIncident = cls
        elif name == 'evmEthicalBehaviorMonitor':
            self.evmEthicalBehaviorMonitor = cls
        elif name == 'evmNormViolation':
            self.evmNormViolation = cls
        elif name == 'evmSocioTechnologyGovernance':
            self.evmSocioTechnologyGovernance = cls
        elif name == 'evmLiabilitySanction':
            self.evmLiabilitySanction = cls
        elif name == 'evmLegalResponsibilityAscription':
            self.evmLegalResponsibilityAscription = cls
        elif name == 'evmgovernance_levels':
            self.evmgovernance = cls
        elif name == 'evmresponsibility_extent':
            self.evmresponsibility = cls
        elif name == 'evmAccountablePerson':
            self.evmAccountablePerson = cls
        elif name == 'evmDistributedResponsibility':
            self.evmDistributedResponsibility = cls
        elif name == 'evmEnumDataTypes':
            self.evmEnumDataTypes = cls
        elif name == 'evmEthicalResponsibilityAscription':
            self.evmEthicalResponsibilityAscription = cls
        elif name == 'evmlegal_liabilities':
            self.evmlegal = cls

        elif name == 'nepAgent':
            self.nepAgent = cls
        elif name == 'nepAgentAction':
            self.nepAgentAction = cls
        elif name == 'nepGovernment':
            self.nepGovernment = cls
        elif name == 'nepAgentRole':
            self.nepAgentRole = cls
        elif name == 'nepNorm':
            self.nepNorm = cls
        elif name == 'nepSituation':
            self.nepSituation = cls
        elif name == 'nepRobot':
            self.nepRobot = cls
        elif name == 'nepTeam':
            self.nepTeam = cls
        elif name == 'nepPlanAction':
            self.nepPlanAction = cls
        elif name == 'nepEthicalPrinciple':
            self.nepEthicalPrinciple = cls
        elif name == 'nepDerogation':
            self.nepDerogation = cls
        elif name == 'nepAgentPlan':
            self.nepAgentPlan = cls
        elif name == 'nepnorm_category':
            self.nepnorm = cls
        elif name == 'nepEthicalDilemma':
            self.nepEthicalDilemma = cls
        elif name == 'nepEthicalTheory':
            self.nepEthicalTheory = cls
        elif name == 'nepSituationPlanRepertoire':
            self.nepSituationPlanRepertoire = cls
        elif name == 'nepTaskAssignment':
            self.nepTaskAssignment = cls
        elif name == 'nepSocialCollection':
            self.nepSocialCollection = cls
        elif name == 'nepEnvironment':
            self.nepEnvironment = cls
        elif name == 'nepAnswer':
            self.nepAnswer = cls
        elif name == 'nepQuery':
            self.nepQuery = cls
        elif name == 'nepActionRationale':
            self.nepActionRationale = cls
        elif name == 'nepDilemmaMitigationPrinciple':
            self.nepDilemmaMitigationPrinciple = cls
        elif name == 'nepnorm_states':
            self.nepnorm = cls
        elif name == 'nepteam_types':
            self.nepteam = cls
        elif name == 'nepCommunity':
            self.nepCommunity = cls
        elif name == 'nepCompany':
            self.nepCompany = cls
        elif name == 'nepConsequentialistNorm':
            self.nepConsequentialistNorm = cls
        elif name == 'nepDeontologicalNorm':
            self.nepDeontologicalNorm = cls
        elif name == 'nepDepartment':
            self.nepDepartment = cls
        elif name == 'nepEnumDataTypes':
            self.nepEnumDataTypes = cls
        elif name == 'nepExplanation':
            self.nepExplanation = cls
        elif name == 'nepObligation':
            self.nepObligation = cls
        elif name == 'nepOrganization':
            self.nepOrganization = cls
        elif name == 'nepPermission':
            self.nepPermission = cls
        elif name == 'nepProhibition':
            self.nepProhibition = cls
        elif name == 'nepVirtuousNorm':
            self.nepVirtuousNorm = cls
        elif name == 'nepautonomous_action_principles':
            self.nepautonomous = cls
        elif name == 'nepdilemma_mitigation_principles':
            self.nepdilemma = cls
        elif name == 'nepethical_principles':
            self.nepethical = cls
        elif name == 'nepethical_theories':
            self.nepethical = cls

        elif name == 'tloAgentCommunication':
            self.tloAgentCommunication = cls
        elif name == 'tloMethod':
            self.tloMethod = cls
        elif name == 'tloAgent':
            self.tloAgent = cls
        elif name == 'tloProcess':
            self.tloProcess = cls
        elif name == 'tloPlan':
            self.tloPlan = cls
        elif name == 'tloInformationArtifact':
            self.tloInformationArtifact = cls
        elif name == 'tloRole':
            self.tloRole = cls
        elif name == 'tloEnumDataTypes':
            self.tloEnumDataTypes = cls
        elif name == 'tloContinuant':
            self.tloContinuant = cls
        elif name == 'tloSituation':
            self.tloSituation = cls
        elif name == 'tloCollective':
            self.tloCollective = cls
        elif name == 'tloPhysical':
            self.tloPhysical = cls
        elif name == 'tloAbstract':
            self.tloAbstract = cls
        elif name == 'tloActionEvent':
            self.tloActionEvent = cls
        elif name == 'tloEntity':
            self.tloEntity = cls
        elif name == 'tloDescription':
            self.tloDescription = cls
        elif name == 'tloEvent':
            self.tloEvent = cls
        elif name == 'tloTime':
            self.tloTime = cls
        elif name == 'tloevmObject':
            self.tloevmObject = cls
        elif name == 'tloProperty':
            self.tloProperty = cls
        elif name == 'tloSpatioTemporalPlace':
            self.tloSpatioTemporalPlace = cls
        elif name == 'tloEnvironmentalEvent':
            self.tloEnvironmentalEvent = cls
        elif name == 'tloAttribute':
            self.tloAttribute = cls
        elif name == 'tloManner':
            self.tloManner = cls
        elif name == 'tloOccurrent':
            self.tloOccurrent = cls
        elif name == 'tloInteractionProcess':
            self.tloInteractionProcess = cls
        elif name == 'tloSchema':
            self.tloSchema = cls
        elif name == 'tloSocialInteractionProcess':
            self.tloSocialInteractionProcess = cls

    def get_factory_by_name(self, name):
        a = dict(
            evmEventCausation=self.evmEventCausation,
            evmResponsibilityAscription=self.evmResponsibilityAscription,
            evmAscriptionJustification=self.evmAscriptionJustification,
            evmGroundsForAscription=self.evmGroundsForAscription,
            evmAgentAccountability=self.evmAgentAccountability,
            evmNormViolationIncident=self.evmNormViolationIncident,
            evmEthicalBehaviorMonitor=self.evmEthicalBehaviorMonitor,
            evmNormViolation=self.evmNormViolation,
            evmSocioTechnologyGovernance=self.evmSocioTechnologyGovernance,
            evmLiabilitySanction=self.evmLiabilitySanction,
            evmLegalResponsibilityAscription=self.evmLegalResponsibilityAscription,
            evmgovernance_levels=self.evmgovernance,
            evmresponsibility_extent=self.evmresponsibility,
            evmAccountablePerson=self.evmAccountablePerson,
            evmDistributedResponsibility=self.evmDistributedResponsibility,
            evmEnumDataTypes=self.evmEnumDataTypes,
            evmEthicalResponsibilityAscription=self.evmEthicalResponsibilityAscription,
            evmlegal_liabilities=self.evmlegal,
            nepAgent=self.nepAgent,
            nepAgentAction=self.nepAgentAction,
            nepGovernment=self.nepGovernment,
            nepAgentRole=self.nepAgentRole,
            nepNorm=self.nepNorm,
            nepSituation=self.nepSituation,
            nepRobot=self.nepRobot,
            nepTeam=self.nepTeam,
            nepPlanAction=self.nepPlanAction,
            nepEthicalPrinciple=self.nepEthicalPrinciple,
            nepDerogation=self.nepDerogation,
            nepAgentPlan=self.nepAgentPlan,
            nepnorm_category=self.nepnorm,
            nepEthicalDilemma=self.nepEthicalDilemma,
            nepEthicalTheory=self.nepEthicalTheory,
            nepSituationPlanRepertoire=self.nepSituationPlanRepertoire,
            nepTaskAssignment=self.nepTaskAssignment,
            nepSocialCollection=self.nepSocialCollection,
            nepEnvironment=self.nepEnvironment,
            nepAnswer=self.nepAnswer,
            nepQuery=self.nepQuery,
            nepActionRationale=self.nepActionRationale,
            nepDilemmaMitigationPrinciple=self.nepDilemmaMitigationPrinciple,
            nepnorm_states=self.nepnorm,
            nepteam_types=self.nepteam,
            nepCommunity=self.nepCommunity,
            nepCompany=self.nepCompany,
            nepConsequentialistNorm=self.nepConsequentialistNorm,
            nepDeontologicalNorm=self.nepDeontologicalNorm,
            nepDepartment=self.nepDepartment,
            nepEnumDataTypes=self.nepEnumDataTypes,
            nepExplanation=self.nepExplanation,
            nepObligation=self.nepObligation,
            nepOrganization=self.nepOrganization,
            nepPermission=self.nepPermission,
            nepProhibition=self.nepProhibition,
            nepVirtuousNorm=self.nepVirtuousNorm,
            nepautonomous_action_principles=self.nepautonomous,
            nepdilemma_mitigation_principles=self.nepdilemma,
            nepethical_principles=self.nepethical,
            nepethical_theories=self.nepethical,
            tloAgentCommunication=self.tloAgentCommunication,
            tloMethod=self.tloMethod,
            tloAgent=self.tloAgent,
            tloProcess=self.tloProcess,
            tloPlan=self.tloPlan,
            tloInformationArtifact=self.tloInformationArtifact,
            tloRole=self.tloRole,
            tloEnumDataTypes=self.tloEnumDataTypes,
            tloContinuant=self.tloContinuant,
            tloSituation=self.tloSituation,
            tloCollective=self.tloCollective,
            tloPhysical=self.tloPhysical,
            tloAbstract=self.tloAbstract,
            tloActionEvent=self.tloActionEvent,
            tloEntity=self.tloEntity,
            tloDescription=self.tloDescription,
            tloEvent=self.tloEvent,
            tloTime=self.tloTime,
            tloevmObject=self.tloevmObject,
            tloProperty=self.tloProperty,
            tloSpatioTemporalPlace=self.tloSpatioTemporalPlace,
            tloEnvironmentalEvent=self.tloEnvironmentalEvent,
            tloAttribute=self.tloAttribute,
            tloManner=self.tloManner,
            tloOccurrent=self.tloOccurrent,
            tloInteractionProcess=self.tloInteractionProcess,
            tloSchema=self.tloSchema,
            tloSocialInteractionProcess=self.tloSocialInteractionProcess,
        )
        return a.get(name)
