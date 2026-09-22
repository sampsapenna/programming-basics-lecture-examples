"""Examples for formatting floating point numbers."""


import math
PI = math.pi


print(f"{PI}")
print(f"{PI:f}")
print(f"{PI:10.8f}")
print(f"{PI:6.4f}")
print(f"{PI:4.3f}")
print(f"{PI:3.2f}")

print("\n\n\n")

print(f"{PI:010.8f}")
print(f"{PI:010.4f}")
print(f"{PI:010.3f}")
print(f"{PI:010.2f}")

print(f"{PI:>10.8f}")
print(f"{PI:>10.4f}")
print(f"{PI:>10.3f}")
print(f"{PI:>10.2f}")

print("\n\n\n")
print(f"{PI:>10.4e}")
print(f"{9.6127768415641315641274517854254:>10.4e}")
print(f"{456.6127768415641315641274517854254:>10.5e}")
print(f"{798412.6127768415641315641274517854254:>10.3e}")
print(f"{468868746564.897416545646854687685415632:>10.2e}")
print(f"{0.000015213232:>10.4e}")
