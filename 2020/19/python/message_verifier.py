import collections

class MessageVerifier:

    def verify_messages(self, rules, messages):

        # I can use Trie here for optimizations of memory
        intersected = self.__backtrack_messages(rules, '0') & messages 

        return len(intersected)
    
    def __backtrack_messages(self, rules, current_rule):
        # Base case
        if current_rule.isalpha():
            return set(current_rule)

        result = set()
        for branch_of_rules in rules[current_rule]:
            
            candidates = set()
            for next_rule in branch_of_rules:

                downstream_candidates = self.__backtrack_messages(rules, next_rule) 
                
                '''
                Combine the previous calculated candidates with the next ones:

                Example:
                0: 3 1 -> [bab, bba]
                1: 2 3 | 3 2 -> [ab, ba]
                2: a -> [a]
                3: b -> [b]

                '''
                if candidates:
                    candidates = set([c1 + c2 for c1 in candidates for c2 in downstream_candidates])
                else:
                    candidates = downstream_candidates

            result |= candidates

        return result