
import time
bar_len = 34

elements = ["-", "\\", "|", "/"]

message = "Runing ..."

for i in range(bar_len+1):
    frame = i % len(elements)
    print(f"\r{message},[{elements[frame]*i:=<{bar_len}}]", end="")
    time.sleep(0.2)
    
########

