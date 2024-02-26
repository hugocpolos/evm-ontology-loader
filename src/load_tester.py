import owlready2
import factory
import navigator

from show_functions import show_all_rules

ontology = owlready2.get_ontology("ontologies/evm.owl").load()
f = factory.Factory(ontology)
nav = navigator.OntologyNavigator(ontology)
show_all_rules(nav)

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

