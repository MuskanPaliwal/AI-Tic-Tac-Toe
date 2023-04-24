# AI_Tic-Tac-Toe
Contains steps for the creation of an Artificial Bot which plays Tic-Tac-Toe intelligently. Try it:[AI_Tic-Tac-Toe](https://muskanpaliwal.github.io/AI-Tic-Tac-Toe)


# Tic-Tac-Toe-minimax
An implementation of Minimax AI Algorithm on Tic-Tac-Toe (or Noughts and Crosses) game.
<p align="center">
	<img src="preview/minimax_img.png"></img>
</p>

## What is Minimax?
Minimax is an artificial intelligence applied in two player games, such as tic-tac-toe, checkers, chess and go. These games are known as zero-sum games, because in a mathematical representation: one player wins (+1) and other player loses (-1) or none of them wins (0).

## How it works
The algorithm recursively search the best move that leads the *Max* player to win or not lose (draw). It considers the current state of the game and the available moves at that state, then for each valid move it plays (alternating *min* and *max*) until it finds a terminal state (win, draw or lose).

## Understanding the Algorithm
The algorithm was studied by the book Algorithms in a Nutshell (George Heineman; Gary Pollice; Stanley Selkow, 2009). Pseudocode (adapted):

```
minimax(state, depth, player)

	if (player = max) then
		best = [null, -infinity]
	else
		best = [null, +infinity]

	if (depth = 0 or gameover) then
		score = evaluate this state for player
		return [null, score]

	for each valid move m for player in state s do
		execute move m on s
		[move, score] = minimax(s, depth - 1, -player)
                undo move m on s

		if (player = max) then
			if score > best.score then best = [move, score]
		else
			if score < best.score then best = [move, score]

	return best
end
```

Next, we'll see each part of this pseudocode with Python implementation. The Python implementation is available at this repository. First of all, consider this:
> board = [
>	[0, 0, 0],
>	[0, 0, 0],
>	[0, 0, 0]
> ]

> MAX = +1

> MIN = -1

The MAX may be X or O and the MIN may be O or X, whatever it can be. The board is 3x3.

```python
def minimax(state, depth, player):
```
* **state**: the current board in tic-tac-toe (node)
* **depth**: index of the node in the game tree
* **player**: may be a *MAX* player or *MIN* player

```python
if player == MAX:
	return [-1, -1, -infinity]
else:
	return [-1, -1, +infinity]
```

Both players start with their worst score. If player is MAX, its score is -infinity. Else if player is MIN, its score is +infinity. **Note:** *infinity* is an alias for inf (from math module, in Python).

The best move on the board is [-1, -1] (row and column) for all.

```python
if depth == 0 or game_over(state):
	score = evaluate(state)
	return score
```

If the depth is equal to zero, then the board hasn't new empty cells to play. Or, if a player wins, then the game ended for MAX or MIN. So the score for that state will be returned.

* If MAX won: return +1
* If MIN won: return -1
* Else: return 0 (draw)

Now we'll see the main part of this code that contains recursion.

```python
for cell in empty_cells(state):
	x, y = cell[0], cell[1]
	state[x][y] = player
	score = minimax(state, depth - 1, -player)
	state[x][y] = 0
	score[0], score[1] = x, y
```

For each valid moves (empty cells):
* **x**: receives cell row index
* **y**: receives cell column index
* **state[x][y]**: it's like board[available_row][available_col] receives MAX or MIN player
* **score = minimax(state, depth - 1, -player)**:
  * state: is the current board in recursion;
  * depth -1: index of the next state;
  * -player: if a player is MAX (+1) will be MIN (-1) and vice versa.

The move (+1 or -1) on the board is undo and the row, column are collected.

The next step is compare the score with best.

```python
if player == MAX:
	if score[2] > best[2]:
		best = score
else:
	if score[2] < best[2]:
		best = score
```

For MAX player, a bigger score will be received. For a MIN player, a lower score will be received. And in the end, the best move is returned. Final algorithm will be:

```python
def minimax(state, depth, player):
	if player == MAX:
		best = [-1, -1, -infinity]
	else:
		best = [-1, -1, +infinity]

	if depth == 0 or game_over(state):
		score = evaluate(state)
		return [-1, -1, score]

	for cell in empty_cells(state):
		x, y = cell[0], cell[1]
		state[x][y] = player
		score = minimax(state, depth - 1, -player)
		state[x][y] = 0

		score[0], score[1] = x, y

		if player == MAX:
			if score[2] > best[2]:
				best = score
		else:
			if score[2] < best[2]:
				best = score

	return best
```

## Game Tree
Below, the best move is on the middle because the max value is on 2nd node on left.

<p align="center">
	<img src="preview/tic-tac-toe-minimax-game-tree.png"></img>
</p>

Take a look that the depth is equal the valid moves on the board. The complete code is available in **py_version/**.

Simplified game tree:

<p align="center">
	<img src="preview/simplified-g-tree.png"></img>
</p>

That tree has 11 nodes. The full game tree has 549.946 nodes! You can test it by putting a static global variable in your program and incrementing it for each minimax function call per turn.
## Tic-Tac-Toe with Reinforcement Learning
AI agent to play Tic-tac-toe using
reinforcement learning. Both the SARSA and Q-learning RL
algorithms are implemented. A user may teach the agent himself by
playing the game for a couple of rounds, or he may apply an automated
teacher agent. 

## Code Structure

#### Source Code

The directory `tictactoe` contains the core source code.
There are 3 main source code files:
1. game.py
2. agent.py
3. teacher.py

I have implemented two RL agents that learn to play the game of tic-tac-toe:
One follows the SARSA algorithm, and the other follows Q-learning.
These agents are trained by a teacher agent that knows the optimal strategy;
however, the teacher only follows this strategy with a given probability
p at each turn. The rest of the time this teacher chooses randomly
from the moves that are available, so that the agents are able to win on
occasion and learn from these wins. To initialize the learning agent Q values,
I make use of default dictionaries with default values of 0 such that the
value for every state-action pair is initialized to 0.

The Q-learning and SARSA agents are implemented in `agent.py`.
Each of the two learning agents inherit from a parent learner class; the key difference between the two is their Q-value update function. 

The Teacher agent is implemented in `teacher.py`. 
The teacher knows the optimal policy for each state presented; however, this agent only takes the optimal choice with a set probability.

In `game.py`, the main game class is found. 
The Game class holds the state of each particular game instance, and it contains the majority of the main game functionality. 
The main game loop can be found in the class's function playGame().

#### Game Script

To play the game (see "Running the Program" below for instructions) you will use the script called `play.py`. 
This script is organized as follows. 
The GameLearner class holds the state of the current game sequence, which will continue until the player choses to stop or the teacher has finished the designated number of episodes.

## Running the Program


To initialize a new agent and begin a new game loop, simply run:

    python play.py -a q                (Q-learner)
    python play.py -a s                (Sarsa-learner)

This will initialize the game and allow you to train the agent manually
by playing against the agent repeatedly. Be careful, however, as initializing
a new agent will delete the state of the previous agents that were stored for
the selected agent type. In the process of playing, you will be storing the
new agent state with each game iteration.

#### Train a new agent automatically (via teacher agent)
To initialize a new RL agent and train it automatically with a teacher agent,
use the flag '-t' followed by the number of game iterations you would like to
train for:

    python play.py -a q -t 5000        (Q-learner)
    python play.py -a s -t 5000        (Sarsa-learner)

Again, be careful as this will overwrite previously-existing agents.

#### Load a trained agent
To load existing agents and play against them, run:

    python play.py -a q -l             (Q-learner)
    python play.py -a s -l             (Sarsa-learner)


I have trained an instance of each the Q-learner and Sarsa-learner agents
and pickled them into .pkl files that are included here. These agents were
trained by a teacher of level 0.9 for 100000 episodes, and they have learned
to play considerably well. You can make use of these if you like, but they
will be overwritten if you have initialized new agents.

#### Load a trained agent and train it further
You can train existing agents further by loading them and teaching them, via
a combination of '-t' and '-l':

    python play.py -a q -l -t 5000     (Q-learner)
    python play.py -a s -l -t 5000     (Sarsa-learner)

#### Load a trained agent and view reward history plot
Finally, to load a stored agent and view a plot of its cumulative reward
history, use '-l' in combination with '-p':

    python play.py -a q -l -p          (Q-learner)
    python play.py -a s -l -p          (Sarsa-learner)

