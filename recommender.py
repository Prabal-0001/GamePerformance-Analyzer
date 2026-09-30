# Choose the highest tested setting that still reaches the target FPS.
def generate_recommendation(hardware, game, tests, comparison):
    target = game["profile"].get("target_fps", 60)
    # A setting is considered playable when its average FPS reaches the target.
    playable = [test for test in tests if test["average_fps"] >= target]

    if playable:
        recommended = playable[-1]["quality"]
    else:
        recommended = "Low"

    # Add a few practical suggestions based on the selected result.
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
