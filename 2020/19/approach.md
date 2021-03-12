### Thoughts:

Seems like the problem can be solved by DFS. Basically, I have a DAG here and need to traverse it.
Also, the question: how can I check quickly if we still match to possible answer or not.
Probably we can try to use Trie for it and traverse the Trie using our rules. 

Need to check the idea...

A few moments later.

I came up with the idea of backtracking. 


### Approach:

1. Read messages from the file using MessageReader
2. Read rules from the file using RulesReader
3. Pass to MessageVerifier the data. 
  3.1 Start to backtrack from 0 rule
  3.2 After reaching out the rule with a letter(e.g 'a') return the first (base case) candidate
  3.3 Combine candidates of the current level and the previous one
4. Profit.
  
### Optimizations
I tried the backtracking solution and it worked for me, BUT I believe that I can optimize the solution (memory) using Trie. 
Also, by using Trie probably I can cut off the recursion branches that can produce no valid answer. Investigating...
