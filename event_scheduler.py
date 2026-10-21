import heapq


def _validate_events(events):
    for event in events:
        if not isinstance(event, (tuple, list)) or len(event) != 2:
            raise ValueError(
                "Each event must contain a start and end time."
            )

        start, end = event

        if (
            isinstance(start, bool)
            or isinstance(end, bool)
            or not isinstance(start, (int, float))
            or not isinstance(end, (int, float))
        ):
            raise TypeError("Event times must be numeric.")

        if end < start:
            raise ValueError("End time cannot precede start time.")


def can_attend_all(events):
    _validate_events(events)

    intervals = sorted(
        (start, end)
        for start, end in events
        if start < end
    )

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


def min_rooms_required(events):
    _validate_events(events)

    intervals = sorted(
        (start, end)
        for start, end in events
        if start < end
    )

    room_end_times = []
    maximum_rooms = 0

    for start, end in intervals:
        while room_end_times and room_end_times[0] <= start:
            heapq.heappop(room_end_times)

        heapq.heappush(room_end_times, end)
        maximum_rooms = max(maximum_rooms, len(room_end_times))

    return maximum_rooms


def test_event_scheduler():
    adjacent = [(9, 10), (10, 11), (11, 12)]
    assert can_attend_all(adjacent) is True
    assert min_rooms_required(adjacent) == 1

    overlapping = [(9, 11), (10, 12)]
    assert can_attend_all(overlapping) is False
    assert min_rooms_required(overlapping) == 2

    unsorted = [(13, 14), (9, 11), (10, 12)]
    assert can_attend_all(unsorted) is False
    assert min_rooms_required(unsorted) == 2

    assert can_attend_all([]) is True
    assert min_rooms_required([]) == 0

    assert can_attend_all([(5, 5), (5, 7)]) is True
    assert min_rooms_required([(5, 5), (5, 7)]) == 1

    assert min_rooms_required([(5, 5), (8, 8)]) == 0

    try:
        min_rooms_required([(10, 9)])
        assert False, "Expected ValueError"
    except ValueError:
        pass

    print("Event Scheduler tests passed.")