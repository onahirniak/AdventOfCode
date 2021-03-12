### Thoughts:

First of all I take an example from the problem:
Input:
card pub key: 5764801
door pub key: 17807724

Output:
encryption key (private key): 14897079

The input has confused me because I expected that the subject number will be provided there. 
So, I decided that I need to generate the subject number on my own. The first version of code became very complex I decided that it was the wrong direction.
I reviewed the problem statement one more time and explored that there were additional data that can help me:

Subject number: 7
Card loop size: 8
Door loop size: 11

So, I've taken the example and write the first test. 
Also, I tried to get loop count of private key (14897079) and explored that it's 88 = 8 * 11 (that seems like card_loop_size * door_loop_size)

### Approach

1. Write for loop with transforming the subject number till find the card loop size
2. Take a card loop size and transform door pub key card loop size times 
(OR we can get loop size of door as well and than transform subject card_loop_size * door_loop_size times BUT it will be much much slower)
3. Profit!
