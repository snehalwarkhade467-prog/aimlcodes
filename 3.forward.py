# Rule-Based Expert System: Forward & Backward Chaining

class Rule:
    def __init__(self, premises, conclusion):
        self.premises, self.conclusion = premises, conclusion


# Knowledge Base
rules = [
    Rule(["Fever", "Cough"], "Flu"),
    Rule(["Flu", "BodyPain"], "ViralInfection"),
    Rule(["ViralInfection"], "Medicine"),
    Rule(["Sneezing"], "Cold"),
    Rule(["Cold"], "Rest")
]


# Forward Chaining
def forward_chaining(facts, rules):
    known_facts = set(facts)
    print("\nInitial Facts:", known_facts)
    changed = True

    while changed:
        changed = False
        for rule in rules:
            if all(p in known_facts for p in rule.premises):
                if rule.conclusion not in known_facts:
                    known_facts.add(rule.conclusion)
                    print("Rule Fired:", rule.premises, "->", rule.conclusion)
                    changed = True
    return known_facts


# Backward Chaining
def backward_chaining(goal, facts, rules, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:
        print(goal, "is a known fact.")
        return True
    if goal in visited:
        return False

    visited.add(goal)

    for rule in rules:
        if rule.conclusion == goal:
            print("\nTrying Rule:", rule.premises, "->", rule.conclusion)
            if all(backward_chaining(p, facts, rules, visited)
                   for p in rule.premises):
                print("Goal", goal, "proved.")
                return True
    return False


# Main Program
facts = {"Fever", "Cough", "BodyPain"}

print("===== FORWARD CHAINING =====")
result = forward_chaining(facts, rules)

print("\nFinal Facts")
for fact in sorted(result):
    print(fact)

print("\n============================")
goal = "Medicine"

print("\n===== BACKWARD CHAINING =====")
if backward_chaining(goal, facts, rules):
    print("\nGoal Achieved:", goal)
else:
    print("\nGoal Cannot be Proved")