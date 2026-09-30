# Build the final report in the same format used by the terminal output.
def build_report(hardware, capability, game, comparison, recommendation):
    lines = []
    lines.append("=" * 60)
    lines.append("              GAME PERFORMANCE REPORT")
    lines.append("=" * 60)

    lines.append("\nHARDWARE")
    lines.append(f"CPU: {hardware['cpu']}")
    lines.append(f"GPU: {hardware['gpu']}")
    lines.append(f"RAM: {hardware['ram']} GB")

    lines.append("\nHARDWARE CAPABILITY (DATABASE)")
    lines.append(f"CPU Tier: {capability['cpu_tier']}")
    lines.append(f"GPU Tier: {capability['gpu_tier']}")
    lines.append(f"GPU VRAM: {capability['vram']} GB")
    lines.append(f"Overall System Tier: {capability['system_tier']}")
    lines.append(f"Capability Summary: {capability['summary']}")

    lines.append("\nGAME CONFIGURATION")
    lines.append(f"Game: {game['name']}")
    lines.append(f"Resolution: {game['resolution']}")
    lines.append(f"Target FPS: {game['profile'].get('target_fps', 60)}")

    lines.append("\nBENCHMARK COMPARISON")
    lines.append("Quality   Avg FPS   Min FPS   Max FPS   Stability   Score   Rating")
    lines.append("-" * 60)
    for result in comparison["results"]:
        lines.append(
            f"{result['quality']:<9}"
            f"{result['average_fps']:<10.1f}"
            f"{result['minimum_fps']:<10.1f}"
            f"{result['maximum_fps']:<10.1f}"
            f"{result['stability']:<12.1f}"
            f"{result['score']:<8.1f}"
            f"{result['rating']}"
        )

    lines.append(f"\nHighest benchmark score: {comparison['best']['quality']}")
    lines.append(f"Likely limitation at that setting: {comparison['best']['bottleneck']}")

    lines.append("\nRECOMMENDATION")
    lines.append(f"Recommended Graphics: {recommendation['recommended_graphics']}")
    for suggestion in recommendation["suggestions"]:
        lines.append(f"- {suggestion}")

    lines.append("\nNote: Hardware information comes from the local database.")
    lines.append("Bottleneck results are only estimates based on the entered results.")
    lines.append("=" * 60)

    return "\n".join(lines)


# Display the completed report in the terminal.
def print_report(report_text):
    print("\n" + report_text)


# Save a copy so the results can be opened later.
def save_report(report_text, filename="performance_report.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report_text)
    return filename
