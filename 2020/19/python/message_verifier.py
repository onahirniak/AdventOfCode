import collections

class MessageVerifier:

    def verify_messages(self, rules, messages):

        intersected = self.__backtrack_messages(rules, '0') & messages 

        return len(intersected)
    
    def __backtrack_messages(self, rules, current_rule):
        if current_rule.isalpha():
            return set(current_rule)

        result = set()
        for branch_of_rules in rules[current_rule]:
            
            candidates = set()
            for next_rule in branch_of_rules:

                downstream_candidates = self.__backtrack_messages(rules, next_rule) 
                
                if candidates:
                    candidates = set([c1 + c2 for c1 in candidates for c2 in downstream_candidates])
                else:
                    candidates = downstream_candidates

            result |= candidates

        return result