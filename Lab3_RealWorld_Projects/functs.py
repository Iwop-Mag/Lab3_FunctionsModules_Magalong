"""Reusable functions for Exercise 3 telemetry monitoring."""

from functools import wraps


def identity_number(last_name, favorite_artist, seed_num):
    """Build the identity number used to generate the telemetry stream."""
    return sum(ord(char) for char in last_name + favorite_artist) + seed_num


def telemetry_stream(last_name, favorite_artist, seed_num, count=12):
    """Yield the deterministic telemetry readings for the configured student."""
    base = identity_number(last_name, favorite_artist, seed_num)
    for index in range(count):
        if index == 4:
            yield 'sensor-disconnected'
        elif index == 9:
            yield None
        else:
            yield round(20 + ((base + index * 37) % 230) / 5 + (index % 3) * 2, 2)


def monitor(function):
    """Record how many times a monitored function is called and its last result."""
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        wrapper.last_result = function(*args, **kwargs)
        return wrapper.last_result

    wrapper.calls = 0
    wrapper.last_result = None
    return wraps(function)(wrapper)


def trace_abnormal(value, threshold, depth=0):
    """Recursively describe how an abnormal value approaches its threshold."""
    if value <= threshold or depth >= 3:
        return [f'Boundary reached at depth {depth}: {value:.2f}']
    next_value = value - threshold / 2
    return [f'Depth {depth}: {value:.2f} exceeds {threshold:.2f}'] + trace_abnormal(next_value, threshold, depth + 1)


@monitor
def process_telemetry(values):
    """Classify telemetry values and return a diagnostic report."""
    processed = valid = invalid = abnormal = 0
    traces = []
    for raw_value in values:
        processed += 1
        try:
            if not isinstance(raw_value, (int, float)):
                raise ValueError('telemetry must be numeric')
            value = float(raw_value)
            if value < 0:
                raise ValueError('telemetry cannot be negative')
            valid += 1
            if value > 40:
                abnormal += 1
                traces.append(trace_abnormal(value, 40))
        except (TypeError, ValueError):
            invalid += 1
    return {'processed': processed, 'valid': valid, 'invalid': invalid, 'abnormal': abnormal, 'status': 'UNSAFE' if invalid or abnormal else 'NORMAL', 'traces': traces}
