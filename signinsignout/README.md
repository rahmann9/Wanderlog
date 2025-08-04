# Wanderlog Assessment: Sign-in Sign-out Logs

## Problem Statement

Application logs are used in analysis of interactions with an application and may be used to detect specific actions.

A log file is provided as a string array where each entry is in the form:

```
user_id timestamp action
```
Each value is separated by a space.

- `user_id` and `timestamp` consist only of digits, are at most 9 digits long, and start with a non-zero digit.
- `timestamp` represents the time in seconds since the application was last launched.
- `action` will be either `sign-in` or `sign-out`.

Given a log with entries in no particular order, return an array of strings that denote user_id's of users who signed out in `maxSpan` seconds or less after signing in.

---

## Function Description

Complete the function `processLogs` in `python3.py`.

**Parameters:**
- `logs (string[])`: each `logs[i]` denotes the i-th entry in the logs
- `maxSpan (int)`: the maximum difference in seconds between when a user logs in and logs out for the user to be included in the result

**Returns:**
- `string[]`: a string array of user id's, sorted ascending by numeric value

---

## Constraints
- 1 ≤ n, maxSpan ≤ n
- 1 ≤ maxSpan ≤ n
- Each user_id contains only characters in the range ascii['0'-'9'], is at most 9 digits long and starts with a non-zero digit.
- Each timestamp contains only characters in the range ascii['0'-'9'] and begins with a non-zero digit
- 0 < timestamp
- Each action is either `sign-in` or `sign-out`.
- Each user_id's sign-in timestamp < sign-out timestamp
- Each user signs in for only 1 session.
- The result will contain at least one element.

---

## Input Format (for custom testing)
- The first line contains an integer, n, the size of logs.
- Each of the next n lines contains a log file entry, logs[i].
- The last line contains a single integer, maxSpan.

---

## Sample Case 1
**Input**
```
6
99 1 sign-in
100 10 sign-in
50 20 sign-in
100 15 sign-out
50 26 sign-out
99 2 sign-out
5
```
**Output**
```
99
100
```
**Explanation:**
| ID  | Sign in | Sign out | Time delta |
|-----|---------|----------|------------|
| 50  | 20      | 26       | 6          |
| 99  | 1       | 2        | 1          |
| 100 | 10      | 15       | 5          |

The users with id's 99 and 100 were not signed in for more than maxSpan = 5 seconds. In sorted numerical order, the return array is `["99", "100"]`.

---

## Sample Case 2
**Input**
```
4
60 12 sign-in
80 20 sign-out
10 20 sign-in
60 20 sign-out
100
```
**Output**
```
60
```
**Explanation:**
| ID  | Sign in | Sign out | Time delta |
|-----|---------|----------|------------|
| 10  | 20      |          |            |
| 60  | 12      | 20       | 8          |
| 80  |         | 20       |            |

Only user id 60 has signed out and was not signed in for more than maxSpan = 100 seconds. The return array is `["60"]`.

---

## Example
Given:
```
n = 7
logs = ["30 99 sign-in", "30 105 sign-out", "12 100 sign-in", "20 80 sign-in", "12 120 sign-out", "20 101 sign-out", "21 110 sign-in"]
maxSpan = 20
```
| ID  | Sign in | Sign out | Time delta |
|-----|---------|----------|------------|
| 30  | 99      | 105      | 6          |
| 12  | 100     | 120      | 20         |
| 20  | 80      | 101      | 21         |
| 21  | 110     |          |            |

The users with id's 30 and 12 were not signed in for more than maxSpan = 20 seconds. In sorted numerical order, the return array is `["12", "30"]`. 