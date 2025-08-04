#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'groupTransactions' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY transactions as parameter.
#

def groupTransactions(transactions):
    # Count occurrences of each transaction item
    from collections import Counter
    counts = Counter(transactions)
    # Sort by descending count, then ascending name
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    # Format as required
    return [f"{item} {count}" for item, count in sorted_items]

if __name__ == '__main__':
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        exit()
    transactions_count = int(lines[0])
    transactions = lines[1:1+transactions_count]
    result = groupTransactions(transactions)
    for line in result:
        print(line)
