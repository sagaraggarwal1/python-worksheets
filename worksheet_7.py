#sagar aggarwal 
# =========================
# PROJECT 1: TIC TAC TOE
# =========================

def print_board(board):
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")

def check_winner(board, player):
    win_combinations = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie(board):
    return " " not in board

def get_player_input(player, board):
    while True:
        pos = input(f"Player {player}, enter position (1-9): ")
        if pos.isdigit():
            pos = int(pos) - 1
            if 0 <= pos <= 8 and board[pos] == " ":
                return pos
        print("Invalid move. Try again.")

def play_game():
    while True:
        board = [" "] * 9
        current_player = "X"
        while True:
            print_board(board)
            move = get_player_input(current_player, board)
            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_tie(board):
                print_board(board)
                print("Game is a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        replay = input("Play again? (y/n): ")
        if replay.lower() != "y":
            break

# play_game()


# =========================
# PROJECT 2: TO-DO LIST
# =========================

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks):
        print(i, task)

def delete_task():
    view_tasks()
    idx = input("Enter index to delete: ")
    if idx.isdigit():
        idx = int(idx)
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Task deleted.")
            return
    print("Invalid index.")

def todo_app():
    while True:
        print("\n1.Add  2.View  3.Delete  4.Exit")
        choice = input("Choose option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

# todo_app()


# =========================
# PROJECT 3: ROBOT PATH PLANNING (A*)
# =========================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import heapq

def astar(grid, start, goal):
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    def h(p):
        return abs(p[0]-goal[0]) + abs(p[1]-goal[1])

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor] == 1:
                    continue
                temp_g = g_score[current] + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    g_score[neighbor] = temp_g
                    f = temp_g + h(neighbor)
                    heapq.heappush(open_set, (f, neighbor))
                    came_from[neighbor] = current
    return None

def robot_path_planner():
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))
    grid = np.zeros((rows, cols), dtype=int)

    obs = int(input("Number of obstacles: "))
    for _ in range(obs):
        r, c = map(int, input("Obstacle position (r c): ").split())
        grid[r][c] = 1

    start = tuple(map(int, input("Start (r c): ").split()))
    goal = tuple(map(int, input("Goal (r c): ").split()))

    print(pd.DataFrame(grid))

    path = astar(grid, start, goal)

    if path is None:
        print("No valid path found.")
        return

    for p in path:
        grid[p] = 2

    plt.imshow(grid, cmap="tab10")
    plt.scatter(start[1], start[0], c="green", s=100)
    plt.scatter(goal[1], goal[0], c="blue", s=100)
    plt.title("Robot Path Planning")
    plt.show()

# robot_path_planner()
