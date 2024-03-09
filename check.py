import os

for path, _, file in os.walk("identities"):
    for f in file:
        if f != ".keep":
            with open(os.path.join(path, f), "r") as singleton:
                content = singleton.read().strip()
                if not content:
                    print(f"File {f} is empty or contains only whitespace")
                    exit(1)
                if len(content.split("\n")) > 1:
                    print(f"File {f} contains more than one line")
                    exit(1)
