# Brief Report: "AI Agent Battle - Tic-Tac-Toe"

## 1. Objective :-
The objective of this assignment is to build two Tic-Tac-Toe AI agents using Minimax, Alpha-Beta pruning and heuristic evaluation.The experiments study the effect of search depth and different heuristic functions.

## 2. Agents:-
### NEXUS
- Algorithm: Minimax + Alpha-Beta pruning
- Search depth: 3
- Heuristic: H1
- H1 considers winning lines, center control and corner control.

### TITAN
- Algorithm: Minimax + Alpha-Beta pruning
- Search depth: 3
- Heuristic: H2
- H2 gives stronger importance to immediate threats and center control.

## 3. Experiment 1 - Search Depth :-
The same general AI approach was tested at depths 1, 2, 3 and 4. The actual results are below.

| Depth | Winner | Nodes Evaluated | Nodes Pruned | Time (seconds) |
|---:|---|---:|---:|---:|
| 1 | DRAW | 45 | 0 | 0.000218 |
| 2 | DRAW | 285 | 0 | 0.000725 |
| 3 | DRAW | 951 | 554 | 0.002024 |
| 4 | DRAW | 3321 | 1267 | 0.007687 |

### Observation :
The table shows the effect of changing only search depth. A deeper search allows the AI to inspect more future positions. This can increase the number of evaluated nodes and execution time. The conclusion should be based on these measured values.

## 4. Experiment 2 - 10 Game Agent Battle:-
NEXUS and TITAN played 10 games. The starting player was alternated to reduce first-player bias.

| Result | Number of Games |
|---|---:|
| NEXUS wins | 0 |
| TITAN wins | 0 |
| Draws | 10 |

## 5. Game-by-Game Results:-
| Game | First | Winner | Moves | NEXUS Nodes | TITAN Nodes | NEXUS Pruned | TITAN Pruned | Time |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | NEXUS | DRAW | 9 | 550 | 371 | 381 | 203 | 0.00203 |
| 2 | TITAN | DRAW | 9 | 376 | 575 | 198 | 356 | 0.002033 |
| 3 | NEXUS | DRAW | 9 | 557 | 387 | 374 | 187 | 0.002089 |
| 4 | TITAN | DRAW | 9 | 364 | 561 | 210 | 370 | 0.002008 |
| 5 | NEXUS | DRAW | 9 | 568 | 386 | 363 | 188 | 0.002042 |
| 6 | TITAN | DRAW | 9 | 376 | 575 | 198 | 356 | 0.002026 |
| 7 | NEXUS | DRAW | 9 | 537 | 367 | 394 | 207 | 0.002176 |
| 8 | TITAN | DRAW | 9 | 383 | 594 | 191 | 337 | 0.002316 |
| 9 | NEXUS | DRAW | 9 | 537 | 367 | 394 | 207 | 0.002025 |
| 10 | TITAN | DRAW | 9 | 384 | 583 | 190 | 348 | 0.00222 |

## 6. Analysis:-
1. **Search depth:** The depth experiment shows how changing search depth changes the amount of search performed.
2. **Execution time:** The measured execution times are recorded in `depth_experiment.csv`.
3. **Evaluated nodes:** The number of nodes increases or changes according to the search depth and available game positions.
4. **Alpha-Beta pruning:** The program counts pruned branches, showing that unnecessary branches can be skipped.
5. **Different decisions:** NEXUS and TITAN use different heuristic functions, so they may evaluate the same board differently.
6. **Heuristic influence:** H1 gives balanced importance to winning lines, center and corners. H2 gives stronger importance to immediate threats and center control.
7. **First-player effect:** The starting player is alternated across the 10 games, allowing both agents to start five games.
8. **Battle result:** In this run, NEXUS won 0 games, TITAN won 0 games, and 10 games were draws.
9. **Computational cost:** The recorded node counts and times can be compared with the game results to discuss the trade-off between decision quality and computation.

## 7. Conclusion:-
This project demonstrates that an AI's decision depends on both the search algorithm and the heuristic used to evaluate positions. Increasing search depth allows the AI to look further ahead but can increase computational cost.
The final observations above are based on the actual program execution and saved CSV results. No game results were hard-coded.
