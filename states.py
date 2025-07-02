import sys

states = []
capitals = []

for arg in sys.argv[1:]:
    state, capital = arg.split()
    states.append(state)
    capitals.append(capital)

print("STATE      CAPITAL")
print("-------------------")

for i in range(len(states)):
    print(f"{states[i]:<10} {capitals[i]}")
