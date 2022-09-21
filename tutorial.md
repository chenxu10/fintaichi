# How I used Taichi Language to Conquer Blackjack

When I was reading the legandary Ed Thop's autobiography A Man for All Markets, I was deeply impressed by how he conquered the blackjack, a casino game popular in las vegas with dynamic programming and card counting system.

Since I happened to know Taichi Lang has great features in optimizing the dynamic programming problems significantly, I decided to use it to create a winning table for gamblers aiming to get an edge in blackjack game.

## Rules of the Game
The rules of the game is simple. We have a dealer and a gambler. Each player has two cards in the first round. The gambler can choose to either hit or stand. If the sum of either party exceeds 21, that party loses its game. If both are less than 21, he who with larger sum wins.

The dealer follows a deterministic strategy, he always chooses to stand when cards in his hands are larger than or equal to 17, otherwise he hits one more card.

For example, if a dealer gets 8 and 9 in his hands and a gambler has 12 and 5 in his heads. He decides to hits 2 rounds and gets 12,5,2,1 the sum of the gambler is less than 21 and larger than the dealer and he wins. If two cards he gets are 2 and 8 then the sum exceeds 21 and he loses.

Of course, beating the house is a complicated adventure requires cheat detecting, card counting so for education purposes, we simplify this problem into a "pefect information" blackjack. In a perfect information blackjack, we assume you know the order of all 52 cards in advance(imaging you have an insider man or X-ray visiosn). In this case, we can use dynmaic programming to implement a dominant strategy to play perfectly against the house. 

We also assume when you win one round, you get 1$, when you lose one round, you get -1$, and 0$ for a tie.

## How to approach this problem?
When we are given a list of cards with known order, we should develop an algorithm to return 
a score dictionary and a pointer dictionary. The score dictionary shows when the deck starts 
at specific card, how many dollars you will win. The pointer dictionary shows when the deck starts
at specific card, how many hits you should take.

## The Algorithm
We first finding out the subproblems of this problem. It will be given we have played out some cards, 
what's the best play of remaining cards starting from index i. We define it as BJ(i),

We second need to define what choices we have, in this case, how many hits we will draw.

The third step will building a conncetion between BJ(i) and BJ(i + cards_played):
It will be BJ(i) = max(outcome belongs to (-1,0,1) + BJ(i + # cards_played) for # in 0,1 ... if valid play

## Simple Python Realization
```python
def perfect_blackjack(deck):
  best_scores = {52: -float('inf')}
  best_hits = {}
  for i in range(51, -1, -1):
    scores = {} #start with card whats the score
    for hits in range(0, 52 - i):
      cards_played, game_score = round_outcome(deck, i, hits)
      if best_scores[i + cards_played] != -float('inf'):
        game_score += best_scores[i + cards_played]
      if game_score not in scores:
        scores[game_score] = hits
    best_scores[i] = max(scores)
    best_hits[i] = scores[max(scores)]
  return best_scores, best_hits
```
## Taichi Acceleration
To be completed, can be reafactored from some classic dynamic programming algorithms
such as longest common subsequence

## Examples
[Feeback](https://docs.taichi-lang.org/blog/accelerate-python-code-100x)
[Feedback](https://docs.taichi-lang.org/zh-Hans/blog/how-i-created-the-tranquil-autumn-air-within-99-lines-of-python-code)