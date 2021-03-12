class MessageReader:

    def read_messages(self, filename):
        messages = set()

        with open(filename) as f:
            # I can use Trie here for optimizations of memory
            messages = set([m.rstrip('\n').strip(' ') for m in f.readlines()])
        
        return messages