from typing import List, Dict

def calculate_distance_since_last(current_odometer: float, previous_odometer: float) -> float:
    return current_odometer - previous_odometer

def calculate_unit_price(total_amount: float, liters: float) -> float:
    if liters <= 0:
        raise ValueError("Liters must be greater than zero.")
    return total_amount / liters

def calculate_consumption_l_per_100km(liters: float, distance: float) -> float:
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    return (liters / distance) * 100

def calculate_mpg(distance: float, gallons: float) -> float:
    if gallons <= 0:
        raise ValueError("Gallons must be greater than zero.")
    return distance / gallons

def calculate_cost_per_km(total_amount: float, distance: float) -> float:
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    return total_amount / distance

def calculate_rolling_average(data: List[float]) -> float:
    if not data:
        return 0.0
    return sum(data) / len(data)

def calculate_totals(entries: List[Dict[str, float]]) -> Dict[str, float]:
    total_spend = sum(entry['total'] for entry in entries)
    total_distance = sum(entry['distance'] for entry in entries)
    return {
        'total_spend': total_spend,
        'total_distance': total_distance
    }