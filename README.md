# Tic-Tac-Toe-game
This Tic-Tac-Toe game is a graphical desktop application built using Python's standard Tkinter GUI library. The application replaces the traditional paper-and-pencil setup with an interactive 3x3 grid of clickable buttons.

Key Features

• Interactive GUI: Features a clean, responsive layout consisting of a status label to track active turns and a main button grid built using Tkinter's grid() geometry manager.
• Turn-Based Logic: Seamlessly toggles between players (typically 'X' and 'O') with every click, updating the button's text dynamically.
• Automatic Win & Draw Detection: Continuously evaluates all 8 horizontal, vertical, and diagonal combinations after every move. It immediately stops the game and triggers a popup or label message when a player wins or when the board fills up in a tie.
• Game Reset: Includes a "Play Again" or "Reset" feature to clear the board and start a new match without restarting the application.
