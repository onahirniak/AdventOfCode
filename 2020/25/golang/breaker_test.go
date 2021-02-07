package main 

import (
	"./breaker"
	"testing"
)

func TestShouldPassWithExampleInput(t *testing.T){
	breaker := breaker.ComboBreaker{MOD: 20201227, MAX_LOOP_COUNT: 20201227}
	
	var privateKey, _ = breaker.Decrypt(7, 5764801, 17807724)

	if privateKey == 14897079 {
		t.Log("PASSED breaker.Decrypt(7, 5764801, 17807724)")
	} else {
		t.Errorf("FAILED breaker.Decrypt(7, 5764801, 17807724), expected value %d", 14897079)
	}
}

func TestShouldPassWithGivenInput(t *testing.T){
	breaker := breaker.ComboBreaker{MOD: 20201227, MAX_LOOP_COUNT: 20201227}
	
	door_private_key, _ := breaker.Decrypt(7, 2069194, 16426071)
	card_private_key, _ := breaker.Decrypt(7, 16426071, 2069194)

	if door_private_key == card_private_key {
		t.Log("PASSED breaker.Decrypt(7, 2069194, 16426071)")
	} else {
		t.Errorf("FAILED breaker.Decrypt(7, 2069194, 16426071), expected value %d", 14897079)
	}
}


func TestShouldFailWithBadInput(t *testing.T){
	breaker := breaker.ComboBreaker{MOD: 20201227, MAX_LOOP_COUNT: 20201227}
	
	_, e := breaker.Decrypt(10, 0, 0)

	if e != nil {
		t.Logf("PASSED with captured error %d", e)
	} else {
		t.Errorf("FAILED with no error")
	}
}