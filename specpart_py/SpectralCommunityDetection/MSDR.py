"""Return a placeholder metric used in some spectral heuristics."""


def msdr(values) -> float:
    if not values:
        return 0.0
    return max(values) - min(values)

