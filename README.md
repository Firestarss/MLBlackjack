# Reinforcement Learning Blackjack #

For this project, we wanted to experiment with using machine learning to find the optimal way to play a card game. We settled on using the card game Blackjack as it can be reduced to fairly simplistic rules and you can immediately know if a decision (hit or stand) resulted in a positive or negative outcome. This, combined with the fact that there are relatively few states for the player to react to (only 180), made this game a very good candidate to use Q-Learning for.

## What is Q-Learning? ##

Q-Learning is a reinforcement learning algorithm that generates a table the includes the estimated costs of applying each action or policy to that state. This table, called the Q-Value Function, includes estimated costs for every state. We used the Monte-Carlo Control approach to generate and optimize the Q-value function.

## What is the Monte-Carlo Control approach? ##

The Monte-Carlo Control approach to Q-Learning basically means that the model will attempt to find the optimal values for the Q-value function by playing multiple rounds, or episodes, of Blackjack and changing the Q-value function based on the outcome of the episode. For example, if the player hit and won that hand, the Q-value for the hit action at that specific state would increase slightly to represent a favorable outcome happened with that action. Had the player lost instead, the Q-value would be slightly decreased. After several instances of this state being simulated, the Q-value function would indicate the optimal action for that state.

## Setting Up the Environment ##

The first thing we needed to do to build our model was set up our environment for it to learn in. The environment defines all of the rules and constraints for the game. Our version of Blackjack is heavily simplified and follows the following rules:

  - There is no betting in our implementation.
  - Cards are assigned a value equal to their rank.
    - Face cards are worth 10.
    - Aces can be either worth 1 or 11.
  - The Player and the Dealer are dealt 2 cards each.
    - The Player's cards are dealt face up while only one of the Dealer's cards are dealt face up.
  - The Player can choose to **Hit** or **Stand**.
    - If the Player Hits, they are given an additional card. If the sum of their hand is greater than 21, they bust and the Dealer wins the hand.
    - If the Player Stands, their turn ends and it becomes the Dealer's turn.
  - The Dealer must Hit if the value of their hand is less than 17. Otherwise they must Stand. If the Dealer goes over 21, they bust and the Player wins the hand.

## Training the Model ##

The Q-value function is initialized with the starting policy being **Hit**. As more and more episodes are simulated, this policy will change to **Stand** where it is the optimal action.

After simulating all episodes, the resulting Q-value function can be visualized. The below figures show a visualization of the Q-value function after n episodes.

### n = 100 ###

![Q-value function after 100 episodes](media/nequals100.png)

### n = 1,000 ###

![Q-value function after 100 episodes](media/nequals1000.png)

### n = 10,000 ###

![Q-value function after 100 episodes](media/nequals10000.png)

### n = 100,000 ###

![Q-value function after 100 episodes](media/nequals100000.png)

