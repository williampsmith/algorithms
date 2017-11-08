from pulp import *


def player():
    prob = LpProblem("Rambis Game Player Problem", LpMaximize)
    x1 = LpVariable("Probability of choosing a Jack", 0, 1)
    x2 = LpVariable("Probability of choosing a Queen", 0, 1)
    x3 = LpVariable("Probability of choosing a King", 0, 1)

    # Add Objective Function
    prob += min(
        -10*x1 + 4*x2 + 6*x3,
        3*x1 - x2 - 9*x3,
        3*x1 - 3*x2 + 2*x3,
    )

    # Add constraints
    prob += -10*x1 + 4*x2 + 6*x3 + min(
        -10*x1 + 4*x2 + 6*x3,
        3*x1 - x2 - 9*x3,
        3*x1 - 3*x2 + 2*x3,
    ) <= 0, 'Jack requirement'

    prob += 3*x1 - x2 - 9*x3 + min(
        -10*x1 + 4*x2 + 6*x3,
        3*x1 - x2 - 9*x3,
        3*x1 - 3*x2 + 2*x3,
    ) <= 0, 'Queen requirement'

    prob += 3*x1 - 3*x2 + 2*x3 + min(
        -10*x1 + 4*x2 + 6*x3,
        3*x1 - x2 - 9*x3,
        3*x1 - 3*x2 + 2*x3,
    ) <= 0, 'King requirement'

    prob += x1 + x2 + x3 == 1, 'Total probability requirement'

    prob.writeLP("RambisGameModel.lp")

    prob.solve()

    print("Status:", LpStatus[prob.status])

    for v in prob.variables():
        print(v.name, " = ", v.varValue)

def dealer():
    prob = LpProblem("Rambis Game Dealer Problem", LpMinimize)
    y1 = LpVariable("Probability of choosing a Jack", 0, 1)
    y2 = LpVariable("Probability of choosing a Queen", 0, 1)
    y3 = LpVariable("Probability of choosing a King", 0, 1)

    # Add Objective Function
    prob += max(
        -10*y1 + 3*y2 + 3*y3,
        4*y1 - y2 - 3*y3,
        6*y1 - 9*y2 + 2*y3,
    )

    # Add constraints
    prob += -10*y1 + 3*y2 + 3*y3 + max(
        -10*y1 + 3*y2 + 3*y3,
        4*y1 - y2 - 3*y3,
        6*y1 - 9*y2 + 2*y3,
    ) >= 0, 'Jack requirement'

    prob += 4*y1 - y2 - 3*y3 + max(
        -10*y1 + 3*y2 + 3*y3,
        4*y1 - y2 - 3*y3,
        6*y1 - 9*y2 + 2*y3,
    ) >= 0, 'Queen requirement'

    prob += 6*y1 - 9*y2 + 2*y3 + max(
        -10*y1 + 3*y2 + 3*y3,
        4*y1 - y2 - 3*y3,
        6*y1 - 9*y2 + 2*y3,
    ) >= 0, 'King requirement'

    prob += y1 + y2 + y3 == 1, 'Total probability requirement'

    prob.writeLP("RambisGameModel.lp")

    prob.solve()

    print("Status:", LpStatus[prob.status])

    for v in prob.variables():
        print(v.name, " = ", v.varValue)
