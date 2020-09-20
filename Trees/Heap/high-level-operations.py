import heapq
import datetime


# the following is an example of priority queues used to merge sort sequences
def email(frequency, details):
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details

fast_email = email(datetime.timedelta(minutes=15), "fast email") # this is a GENERATOR
slow_email = email(datetime.timedelta(minutes=40), "slow mail") # this is a GENERATOR

# a GENERATOR is something that produces a sequence of values

print(fast_email)

unified = heapq.merge(fast_email, slow_email)

for _ in range(10):
   print(next(unified))