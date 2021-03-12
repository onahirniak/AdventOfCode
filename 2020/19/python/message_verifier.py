import collections

class MessageVerifier:

    def verify_messages_part_two(self, rules, messages):

        messages_from_42 = self.__backtrack_messages(rules, '42') 
        messages_from_31 = self.__backtrack_messages(rules, '31')

        filtered_messages = self.__filter_messages(messages, messages_from_42, messages_from_31)

        return len(filtered_messages)

    def verify_messages_part_one(self, rules, messages):

        # I can use Trie here for optimizations of memory
        messages_to_verify = self.__backtrack_messages(rules, '0') 

        return len(messages_to_verify & messages)
    
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

    def __filter_messages(self, total_messages, messages_from_42, messages_from_31):
        result = []
        
        # REFACTOR
        for message in total_messages:
            if len(message) % 8 != 0: continue
            if message[:8] not in messages_from_42: continue
            if message[-8:] not in messages_from_31: continue

            isAllBlocksValid = True
            message_blocks_in_42 = 0
            message_blocks_in_31 = 0
            for i in range(0, len(message), 8):
                message_block = message[i:i + 8]

                if message_block in messages_from_42:
                    message_blocks_in_42 += 1
                if message_block in messages_from_31:
                    message_blocks_in_31 += 1

                if message_block in messages_from_31:
                    if len(message) - i >= 16:
                        next_message_block =  message_block = message[i + 8:i + 16]
                        if next_message_block in messages_from_42:
                            isAllBlocksValid = False
                            break

            if not isAllBlocksValid: continue
            if message_blocks_in_42 <= message_blocks_in_31: continue
            
            result.append(message)

        return result