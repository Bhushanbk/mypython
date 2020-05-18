cont={
        "jim":"973873",
        "cruz":"789456",
        "jacki":"777888",
        "chan":"999875"
        }
print(cont["jim"])
print(cont)
print("-----------")
print("length of the dic",len(cont))
sta="jim" in cont
print("sta is",sta)
sta1="me" in cont
print("sta1 is",sta1)
print("keys")
print(cont.keys())
print("values",cont.values())
print("jacki",cont.get("jacki"))
print("pcp",cont.pop("cruz"))
print(cont.popitem())
copy=cont.copy()
print("copy",copy)
