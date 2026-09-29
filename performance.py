def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative.")
        except ValueError:
            print("Enter a valid number.")


def get_one_benchmark(quality):
    print(f"\n--- {quality.upper()} BENCHMARK ---")

    average = get_non_negative_float("Average FPS: ")
    minimum = get_non_negative_float("Minimum FPS: ")
    maximum = get_non_negative_float("Maximum FPS: ")

    if minimum > average:
        print("Minimum FPS cannot exceed average FPS. Setting minimum = average.")
        minimum = average

    if maximum < average:
        print("Maximum FPS cannot be below average FPS. Setting maximum = average.")
        maximum = average

    try:
        duration = float(input("Test duration (minutes): "))
        if duration <= 0:
            raise ValueError
    except ValueError:
        print("Invalid duration. Using 10 minutes.")
        duration = 10.0

    return {
        "quality": quality,
        "average_fps": average,
        "minimum_fps": minimum,
        "maximum_fps": maximum,
        "duration": duration
    }


def get_performance_tests():
    print("\n--- GRAPHICS BENCHMARK ---")
    print("Enter the FPS results for all four graphics settings.")

    levels = ["Low", "Medium", "High", "Ultra"]
    tests = []

    for quality in levels:
        tests.append(get_one_benchmark(quality))

    return tests


def get_performance_test():
    return get_one_benchmark("Current")
