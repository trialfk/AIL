# ------------------------------------------------------------
# Bayesian Network using pgmpy
# Structure: R -> S -> A -> W also connect R->A 
# Goal: Compute P(S | R=0, W=1)

# ------------------------------------------------------------

from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
# Step 1: Define the structure of the Bayesian Network
model = DiscreteBayesianNetwork([
    ('R', 'S'),
    ('S', 'A'),
    ('A', 'W')
])
# P(R)
cpd_R = TabularCPD(
    variable='R',
    variable_card=2,
    values=[[0.70], [0.30]]
)
# P(S | R)
cpd_S_given_R = TabularCPD(
    variable='S',
    variable_card=2,
    values=[
        [0.90, 0.20],  # P(S=0 | R)
        [0.10, 0.80]   # P(S=1 | R)
    ],
    evidence=['R'],
    evidence_card=[2]
)
# P(A | S)
cpd_A_given_S = TabularCPD(
    variable='A',
    variable_card=2,
    values=[
        [0.995, 0.95],  # P(A=0 | S)
        [0.005, 0.05]   # P(A=1 | S)
    ],
    evidence=['S'],
    evidence_card=[2]
)
# P(W | A)
cpd_W_given_A = TabularCPD(
    variable='W',
    variable_card=2,
    values=[
        [0.98, 0.01],  # P(W=0 | A)
        [0.02, 0.99]   # P(W=1 | A)
    ],
    evidence=['A'],
    evidence_card=[2]
)
# Step 3: Add CPDs to the model
model.add_cpds(cpd_R, cpd_S_given_R, cpd_A_given_S, cpd_W_given_A)
# Step 4: Validate the model
assert model.check_model()
# Step 5: Perform inference
inference = VariableElimination(model)
print("\nInference: Calculating P(S | R=0, W=1)\n")
# Compute P(S | R=0, W=1)
# The probability that the road is slippery (S = 1) given that it is not raining (R = 0) but there is a report (W = 1).
posterior = inference.query(variables=['S'], evidence={'R': 0, 'W': 1})
# Step 6: Display results
print(posterior)
