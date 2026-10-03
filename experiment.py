import csv
import time
from game import TicTacToe
from agents import Agent
from heuristic import heuristic_h1, heuristic_h2


def run_game(agent_x, agent_o):
    game = TicTacToe()
    current_player = "X"
    total_nodes = {agent_x.name: 0, agent_o.name: 0}
    total_pruned = {agent_x.name: 0, agent_o.name: 0}
    move_count = 0
    start = time.perf_counter()

    while not game.is_terminal():
        agent = agent_x if current_player == "X" else agent_o
        move, stats = agent.choose_move(game.board, current_player)
        game.make_move(move, current_player)

        total_nodes[agent.name] += stats.nodes
        total_pruned[agent.name] += stats.pruned
        move_count += 1

        current_player = "O" if current_player == "X" else "X"

    elapsed = time.perf_counter() - start
    winner_symbol = game.check_winner()

    if winner_symbol == "X":
        winner = agent_x.name
    elif winner_symbol == "O":
        winner = agent_o.name
    else:
        winner = "DRAW"

    return {
        "winner": winner,
        "moves": move_count,
        "nodes_x": total_nodes[agent_x.name],
        "nodes_o": total_nodes[agent_o.name],
        "pruned_x": total_pruned[agent_x.name],
        "pruned_o": total_pruned[agent_o.name],
        "time": elapsed
    }


def run_depth_experiment():
    rows = []
    # Same agent/heuristic; only search depth changes.
    for depth in [1, 2, 3, 4]:
        agent_x = Agent("DEPTH_TEST", depth, heuristic_h1)
        agent_o = Agent("OPPONENT", depth, heuristic_h1)
        result = run_game(agent_x, agent_o)
        rows.append({
            "depth": depth,
            "winner": result["winner"],
            "nodes_evaluated": result["nodes_x"] + result["nodes_o"],
            "nodes_pruned": result["pruned_x"] + result["pruned_o"],
            "time_seconds": round(result["time"], 6)
        })
    return rows


def run_battle():
    nexus = Agent("NEXUS", 3, heuristic_h1)
    titan = Agent("TITAN", 3, heuristic_h2)
    rows = []

    for game_no in range(1, 11):
        if game_no % 2 == 1:
            first_name = "NEXUS"
            result = run_game(nexus, titan)
        else:
            first_name = "TITAN"
            result = run_game(titan, nexus)

        rows.append({
            "game": game_no,
            "first": first_name,
            "winner": result["winner"],
            "moves": result["moves"],
            "nexus_nodes": result["nodes_x"] if first_name == "NEXUS" else result["nodes_o"],
            "titan_nodes": result["nodes_o"] if first_name == "NEXUS" else result["nodes_x"],
            "nexus_pruned": result["pruned_x"] if first_name == "NEXUS" else result["pruned_o"],
            "titan_pruned": result["pruned_o"] if first_name == "NEXUS" else result["pruned_x"],
            "time_seconds": round(result["time"], 6)
        })
    return rows


def save_results(depth_rows, battle_rows):
    with open("results/depth_experiment.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["depth", "winner", "nodes_evaluated",
                           "nodes_pruned", "time_seconds"]
        )
        writer.writeheader()
        writer.writerows(depth_rows)

    with open("results/results.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f, fieldnames=["game", "first", "winner", "moves",
                           "nexus_nodes", "titan_nodes",
                           "nexus_pruned", "titan_pruned", "time_seconds"]
        )
        writer.writeheader()
        writer.writerows(battle_rows)


if __name__ == "__main__":
    depth_rows = run_depth_experiment()
    battle_rows = run_battle()
    save_results(depth_rows, battle_rows)

    print("Depth Experiment")
    for row in depth_rows:
        print(row)

    print("\n10 Game Battle")
    for row in battle_rows:
        print(row)

    print("\nResults saved in the results/ folder.")
