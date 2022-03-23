import os

purr = ["examples/" + f for f in os.listdir("examples") if f[-5:] == ".purr"]
for f in purr:
    os.system(f"python -m skiio c -i {f} -o {f[:-5]}")