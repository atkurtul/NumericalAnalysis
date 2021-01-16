ran=[]
for _ in range(10):
    ran.append(random.random()*50 - 25)
ran=sorted(ran)
print("[")
for f in ran:
    print(f, end=", ")
print("]")