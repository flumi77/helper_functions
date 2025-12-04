import matplotlib.pyplot as plt
import numpy as np

def say_hello():
  print("Hello!")

'''Use default_timer from timeit to measure start and end time
from timeit import default_timer as timer

start = timer()
some code ...
end = timer()
print_train_time(start, end, device)
'''
def print_train_time(start: float, end: float, device: torch.device = None):
    total_time = end - start
    print(f"Train time on {device}: {total_time:.3f} seconds")
    return total_time
