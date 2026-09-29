def generate_recommendation(hardware, game, tests, comparison):
    target = game["profile"].get("target_fps", 60)
    playable = [test for test in tests if test["average_fps"] >= target]

    if playable:
        recommended = playable[-1]["quality"]
    else:
        recommended = "Low"

    suggestions = []
    recommended_result = next(
        result for result in comparison["results"]
        if result["quality"] == recommended
    )

    if recommended_result["average_fps"] < target:
        suggestions.append("Lower the resolution or graphics settings further.")
    if recommended_result["stability"] < 65:
        suggestions.append("Reduce shadows and heavy visual effects.")
    if hardware["ram"] <= 8:
        suggestions.append("Close unnecessary background applications.")
    if not suggestions:
        suggestions.append("Current benchmark results meet the target FPS.")

    return {
        "recommended_graphics": recommended,
        "target_fps": target,
        "suggestions": suggestions
    }
