import sys
from collections import deque

class ProductInventory:
    def __init__(self):
        self.dq = deque()

    def _clean_expired(self, current_timestamp):
        while self.dq and self.dq[0][1] <= current_timestamp:
            self.dq.popleft()

    def add_product(self, current_timestamp, id, expires_in):
        expiry = current_timestamp + expires_in
        self.dq.append((id, expiry))

    def sell_product(self, current_timestamp):
        self._clean_expired(current_timestamp)


        while self.dq and self.dq[-1][1] <= current_timestamp:
            self.dq.pop()  

        if self.dq:
            product_id, _ = self.dq.pop() 
            return product_id

        return -1

    def get_inventory(self, current_timestamp):
        self._clean_expired(current_timestamp)

        result = []
        for pid, expiry in reversed(self.dq):
            if current_timestamp < expiry:
                result.append(pid)
        return result


inventory = ProductInventory()

input_data = sys.stdin.read().split('\n')
output = []

for line in input_data:
    if not line.strip():
        continue
    parts = line.split()
    func = parts[0]

    if func == "add_product":
        ts = int(parts[1])
        pid = int(parts[2])
        exp = int(parts[3])
        inventory.add_product(ts, pid, exp)

    elif func == "sell_product":
        ts = int(parts[1])
        output.append(str(inventory.sell_product(ts)))

    elif func == "get_inventory":
        ts = int(parts[1])
        inv = inventory.get_inventory(ts)
        output.append("[" + ", ".join(map(str, inv)) + "]")

print('\n'.join(output))