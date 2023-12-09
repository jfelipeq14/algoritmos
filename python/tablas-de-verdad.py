v = True
f = False
print()
print(f"Tabla de verdad con '^' = 'y'")
print(f"{v} y {v} : {v and v}")
print(f"{v} y {f} : {v and f}")
print(f"{f} y {v} : {f and v}")
print(f"{f} y {f} : {f and f}")
print()
print(f"Tabla de verdad con 'v' = 'o'")
print(f"{v} o {v} : {v or v}")
print(f"{v} o {f} : {v or f}")
print(f"{f} o {v} : {f or v}")
print(f"{f} o {f} : {f or f}")