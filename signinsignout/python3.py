#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER maxSpan
#

def processLogs(logs, maxSpan):
    # Dictionary to store sign-in and sign-out times for each user
    user_sessions = {}
    for log in logs:
        parts = log.split()
        user_id, timestamp, action = parts[0], int(parts[1]), parts[2]
        if user_id not in user_sessions:
            user_sessions[user_id] = {'sign-in': None, 'sign-out': None}
        user_sessions[user_id][action] = timestamp
    result = []
    for user_id, session in user_sessions.items():
        sign_in = session['sign-in']
        sign_out = session['sign-out']
        # Debug print removed
        if sign_in is not None and sign_out is not None:
            if 0 < (sign_out - sign_in) <= maxSpan:
                result.append(user_id)
    # Sort numerically
    result.sort(key=lambda x: int(x))
    return result

if __name__ == '__main__':
    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    maxSpan = int(input().strip())

    result = processLogs(logs, maxSpan)

    for user_id in result:
        print(user_id)
