package main

import (
	"./breaker"
	"fmt"
)

func main() {
	breaker := breaker.ComboBreaker{MOD :20201227, MAX_LOOP_COUNT: 20201227}
	
	var privateKey, _ = breaker.Decrypt(7, 5764801, 17807724)

	fmt.Println(privateKey)

}
