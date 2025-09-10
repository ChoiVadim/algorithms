# Algorithms Learning Repository

This repository contains implementations of various algorithms and data structures for educational purposes. It's designed to help understand fundamental algorithmic concepts through practical Python implementations.

## 📁 Repository Structure

```
src/
├── backtracking/          # Backtracking algorithms
├── branch_n_bound/        # Branch and bound algorithms
├── divide_n_conquer/      # Divide and conquer algorithms
├── dynamic_programming/   # Dynamic programming solutions
├── else/                  # Miscellaneous algorithms
└── greedy_algorithms/     # Greedy algorithm implementations
```

## 🔍 Algorithm Categories

### Backtracking
- **4queens_algo.py** - 4-Queens problem solver
- **m_coloring.py** - Graph M-coloring problem
- **n_queens_algo.py** - N-Queens problem solver

### Branch and Bound
- **0_1_knapsack_bb.py** - 0/1 Knapsack using branch and bound
- **TSP_BB.py** - Traveling Salesman Problem using branch and bound

### Divide and Conquer
- **ternary_search.py** - Ternary search algorithm
- **tree_way_megre_sort.py** - Three-way merge sort

### Dynamic Programming
- **0_1_knapsack_algo.py** - 0/1 Knapsack using dynamic programming
- **floyd_algo.py** - Floyd-Warshall shortest path algorithm
- **obtimal_bst.py** - Optimal Binary Search Tree
- **recursive_algorithm_solving.py** - Recursive vs iterative vs memoized solutions
- **travelling_salesman_problem.py** - TSP using dynamic programming

### Greedy Algorithms
- **graph_coloring.py** - Graph coloring using greedy approach
- **huffman_algo.py** - Huffman coding algorithm
- **knapsack_algo.py** - Knapsack using greedy approach
- **kruskal_algo.py** - Kruskal's minimum spanning tree
- **prim_algo.py** - Prim's minimum spanning tree

### Other Algorithms
- **fib_const.py** - Fibonacci in constant time with unit tests
- **fib_matrix.py** - Fibonacci using matrix exponentiation
- **sort_algo.py** - Various sorting algorithms

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd algorithms
   ```

2. Run any algorithm:
   ```bash
   python src/dynamic_programming/floyd_algo.py
   python src/backtracking/n_queens_algo.py
   ```

3. Run tests (where available):
   ```bash
   python src/else/fib_const.py
   ```

## 📚 Learning Objectives

This repository covers fundamental algorithmic paradigms:

- **Backtracking**: Systematic exploration of solution spaces
- **Branch and Bound**: Optimization technique for combinatorial problems
- **Divide and Conquer**: Breaking problems into smaller subproblems
- **Dynamic Programming**: Optimal substructure and overlapping subproblems
- **Greedy Algorithms**: Making locally optimal choices

## 🎯 Purpose

This collection is purely for educational purposes to:
- Understand algorithm design patterns
- Practice implementation skills
- Compare different approaches to similar problems
- Learn time and space complexity analysis

## 📝 Notes

- All implementations are in Python for clarity and readability
- Code includes comments explaining key concepts
- Some algorithms include complexity analysis
- Examples and test cases are provided where applicable

---

*This repository is maintained for learning purposes. Feel free to explore, modify, and experiment with the code!*
