import owlready2
import factory
import navigator

ontology = owlready2.get_ontology("ontologies/evm.owl").load()
f = factory.Factory(ontology)
nav = navigator.OntologyNavigator(ontology)


for j, i in enumerate(ontology.world.rules()):
    if j == 4:
        print(i)


a = f.nepAgent("a")
ap = f.nepAgentPlan("ap")
pa = f.nepPlanAction("pa")
ac = f.nepAgentAction("ac")
e = f.nepEnvironment("e")
s = f.nepSituation("s")
s.nepis_perception_of.append(e)
e.nepis_perceived_by.append(a)
a.nepintends_to_realize.append(s)
ap.nepcontains.append(pa)
pa.nepis_implemented_by.append(ac)
ac.tloaffects.append(e)


owlready2.sync_reasoner_hermit(infer_property_values=True, debug=True)


"""
nepAgent(?a)
nepAgentPlan(?ap)
nepPlanAction(?pa)
nepAgentAction(?ac)
nepEnvironment(?e)
nepSituation(?s)
nepis_perception_of(?s, ?e)
nepis_perceived_by(?e, ?a)
nepintends_to_realize(?a, ?s)
nepcontains(?ap, ?pa)
nepis_implemented_by(?pa, ?ac)
tloaffects(?ac, ?e)
-> nepapplies(?a, ?ap), nepexecutes(?a, ?pa)
"""
