import pyomo.environ as pyo


model = pyo.ConcreteModel()

model.x = pyo.Var([1, 2], domain=pyo.Reals)
model.OBJ = pyo.Objective(expr=model.x[1] ** 2 + model.x[2] ** 2 - 5 * model.x[1] - 6 * model.x[2] + 15,
                          sense=1)  # Objective sense must be set to one of 'minimize' (1) or 'maximize' (-1).

model.Constraint1 = pyo.Constraint(
    expr=2 * model.x[1] ** 2 + 2 * model.x[2] ** 2 - 3 * model.x[1] - 3 * model.x[2] - 2 == 0)
model.Constraint2 = pyo.Constraint(expr=model.x[1] ** 2 + model.x[2] ** 2 - 4 * model.x[1] - 3 * model.x[2] + 8 >= 2)
model.Constraint3 = pyo.Constraint(expr=model.x[1] ** 2 + model.x[2] ** 2 - 4 * model.x[1] - 3 * model.x[2] + 8 <= 3)

solver = pyo.SolverFactory('bonmin', executable=r"C:\py-dss-interface_Examples\bonmin")
solver.solve(model)
model.display()