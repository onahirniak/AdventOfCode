class RulesReader:

    '''
    The function reads the data with rules and convert each line to following schema:
    1: 2 3 | 4 4 -> { '1': [('2','3'), ('4','4')] }
    '''
    def read_rules(self, filename):
        rules = []

        with open(filename) as f:
            rules = f.readlines()   
        
        return self.__normalize_rules(rules)
        
    def __normalize_rules(self, rules):
        d = {}

        for rule in rules:
            from_rule, to_rules_branches = rule.split(':')

            converted_rules = []
            for to_rule in to_rules_branches.split('|'):
                converted_rules.append(tuple([r.rstrip('\n').strip('"') for r in to_rule.split(' ') if r]))

            d[from_rule] = converted_rules

        return d
        
