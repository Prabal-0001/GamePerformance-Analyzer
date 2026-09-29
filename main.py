from hardware import get_hardware, get_hardware_capability
from game import get_game
from performance import get_performance_tests
from analyzer import compare_benchmarks
from recommender import generate_recommendation
from report import build_report, print_report, save_report


def main():
    print("=" * 55)
    print("          GAME PERFORMANCE ANALYZER")
    print("=" * 55)

    hardware = get_hardware()
    capability = get_hardware_capability(hardware)
    game = get_game()
    tests = get_performance_tests()

    comparison = compare_benchmarks(hardware, game, tests)
    recommendation = generate_recommendation(
        hardware, game, tests, comparison
    )

    report = build_report(
        hardware, capability, game, comparison, recommendation
    )
    print_report(report)

    filename = save_report(report)
    print(f"\nReport saved as: {filename}")


if __name__ == "__main__":
    main()
