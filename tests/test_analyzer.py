from analyzer import calculate_stability, classify_score

assert round(calculate_stability(80, 72), 2) == 90.00
assert classify_score(95) == "Excellent"
assert classify_score(80) == "Good"
assert classify_score(65) == "Moderate"
assert classify_score(50) == "Low"
assert classify_score(20) == "Poor"

print("All analyzer tests passed.")
