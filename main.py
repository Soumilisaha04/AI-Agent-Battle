from experiment import run_depth_experiment, run_battle, save_results


def main():
    print("AI AGENT BATTLE - TIC-TAC-TOE")
    print("=" * 40)

    depth_results = run_depth_experiment()
    battle_results = run_battle()
    save_results(depth_results, battle_results)

    print("\nDepth Experiment")
    for row in depth_results:
        print(row)

    print("\nAgent Battle")
    for row in battle_results:
        print(row)

    print("\nAll results have been saved to results/.")


if __name__ == "__main__":
    main()
