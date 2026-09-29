def calculate_stability(average_fps, minimum_fps):
    if average_fps <= 0:
        return 0
    return (minimum_fps / average_fps) * 100


def fps_score(fps):
    score = (fps / 60) * 100
    return min(score, 100)


def calculate_performance_score(test):
    avg = fps_score(test["average_fps"])
    minimum = fps_score(test["minimum_fps"])
    stability = calculate_stability(
        test["average_fps"], test["minimum_fps"]
    )

    return (avg * 0.50) + (minimum * 0.30) + (stability * 0.20)


def classify_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Moderate"
    elif score >= 40:
        return "Low"
    return "Poor"


def analyze_bottleneck(hardware, game, test, stability):
    gpu = hardware["gpu_data"]
    cpu = hardware["cpu_data"]
    graphics = test.get("quality", game["graphics"])

    if gpu is None and cpu is None:
        return "Unknown hardware limitation"

    if test["average_fps"] < 40 and graphics in ["High", "Ultra"]:
        return "Possible GPU limitation"

    if test["average_fps"] < 30 and hardware["ram"] < 8:
        return "Possible RAM/resource limitation"

    if stability < 65 and graphics in ["Low", "Medium"]:
        return "Possible CPU or system-resource limitation"

    if test["average_fps"] >= 60 and stability >= 80:
        return "No major limitation indicated"

    return "No clear bottleneck indicated"


def analyze_performance(hardware, game, test):
    stability = calculate_stability(
        test["average_fps"], test["minimum_fps"]
    )
    score = calculate_performance_score(test)
    rating = classify_score(score)
    bottleneck = analyze_bottleneck(hardware, game, test, stability)

    return {
        "stability": stability,
        "score": score,
        "rating": rating,
        "bottleneck": bottleneck
    }


def compare_benchmarks(hardware, game, tests):
    results = []

    for test in tests:
        analysis = analyze_performance(hardware, game, test)
        results.append({
            "quality": test["quality"],
            "average_fps": test["average_fps"],
            "minimum_fps": test["minimum_fps"],
            "maximum_fps": test["maximum_fps"],
            "stability": analysis["stability"],
            "score": analysis["score"],
            "rating": analysis["rating"],
            "bottleneck": analysis["bottleneck"]
        })

    best = max(results, key=lambda item: item["score"])
    return {
        "results": results,
        "best": best
    }
