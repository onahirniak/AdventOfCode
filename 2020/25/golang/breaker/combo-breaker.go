package breaker;

import (
	"fmt"
	"errors"
)

type ComboBreaker struct {
	MOD, MAX_LOOP_COUNT int
}

func (breaker ComboBreaker) GetLoopSize(subject int, pubKey int) (int, error) {
	generated_pub_key := subject
	for i := 1; i < breaker.MAX_LOOP_COUNT; i++ {
		generated_pub_key = (generated_pub_key * subject) % breaker.MOD
		if generated_pub_key == pubKey {
			return i + 1, nil
		}
	}
	return 0, errors.New(fmt.Sprintf("Could not find loop size. subject=%d, pub_key=%d", subject, pubKey))

}

func (breaker ComboBreaker) GetPrivateKey(loopSize int, pubKey int) int {
	private_key := 1

	for i := 0; i < loopSize; i++ {
		private_key = (private_key * pubKey) % breaker.MOD
	}
	
	return private_key
}

func (breaker ComboBreaker) Decrypt(subject int, cardPubKey int, doorPubKey int) (int, error) {

	var cardLoopSize, e = breaker.GetLoopSize(subject, cardPubKey)

	fmt.Println("Card loop size: ", cardLoopSize)

	if e != nil {
		return 0, e
	}

	privateKey := breaker.GetPrivateKey(cardLoopSize, doorPubKey)

	return privateKey, nil;
}
