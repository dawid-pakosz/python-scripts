import time
from tqdm import tqdm


for _ in tqdm(range(100), desc="Processing", unit="item"):
    time.sleep(0.1)  # Simulate work being done
