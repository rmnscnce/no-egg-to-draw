import os
from typing import List

entries: List[str] = []

for path, _, file in os.walk("identities"):
    for f in file:
        if f != ".keep":
            with open(os.path.join(path, f), "r") as singleton:
                entries.append(singleton.read().strip())

with open("identities_finalized.txt", "w") as muxed:
    muxed.write("\n".join(entries))
