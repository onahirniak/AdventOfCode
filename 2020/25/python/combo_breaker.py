class ComboBreaker:
    
    def __init__(self, max_loop_count = 20201227, mod = 20201227):
        self.__max_loop_count = max_loop_count
        self.__mod = mod

    def decrypt(self, subject, card_pub_key, door_pub_key):

        try:
            card_loop_size = self.__get_loop_size(subject, card_pub_key)

            print(f'Success to get loop size! card_loop_size={card_loop_size}', )
        
            private_key = self.__get_private_key(card_loop_size, door_pub_key)

            return private_key
        except Exception:
            print(f'Error! Check the parameters: subject={subject}, card_pub_key={card_pub_key}, door_pub_key={door_pub_key}')
            raise;

    def __get_private_key(self, loop_size, pub_key):
        private_key = 1

        for _ in range(loop_size):
            private_key = (private_key * pub_key) % self.__mod
        
        return private_key

    def __get_loop_size(self, subject, pub_key):
        generated_pub_key = subject

        for loopSize in range(1, self.__max_loop_count):
            generated_pub_key = (generated_pub_key * subject) % self.__mod
            if generated_pub_key == pub_key: 
                return loopSize + 1

        raise Exception(f'Could not find loop size. subject={subject}, pub_key={pub_key}')