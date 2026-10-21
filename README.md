# Event Scheduler in Python

An event scheduling implementation that detects overlapping events and calculates the minimum number of rooms required.

## Features

- Detects whether all events can be attended without overlap
- Calculates minimum room requirements using a min-heap
- Supports unsorted input and adjacent events
- Validates event intervals and handles zero-duration events
- Includes tests for normal cases and edge cases

## Algorithms

Events are sorted by start time. A min-heap tracks room end times so that rooms can be reused as soon as their events finish.

## Run

```bash
python event_scheduler.py
```

## Complexity

- `can_attend_all`: O(n log n) time
- `min_rooms_required`: O(n log n) time
- Space: O(n)

## Technologies

Python 3, Sorting, Min-Heap, `heapq`