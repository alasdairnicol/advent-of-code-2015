package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"strings"
)

var problemInput = "yzbqklnj"

func findNumber(problemInput string, numZeroes int) (number int) {
	number = 0
	zeroes := strings.Repeat("0", numZeroes)

	var trial string
	for {
		number += 1
		trial = fmt.Sprintf("%s%d", problemInput, number)
		hash := GetMD5Hash(trial)
		if strings.HasPrefix(hash, zeroes) {
			return number
		}
	}
}

func GetMD5Hash(text string) string {
	hash := md5.Sum([]byte(text))
	return hex.EncodeToString(hash[:])
}

func main() {
	fiveZeroes := findNumber(problemInput, 5)
	sixZeroes := findNumber(problemInput, 6)
	fmt.Printf("The hash for %d starts with 5 zeroes\n", fiveZeroes)
	fmt.Printf("The hash for %d starts with 6 zeroes\n", sixZeroes)
}

// `>>> i=0
// >>> while True:
// ...     i+=1
// ...     hex = md5(b'yzbqklnj%d' % i).hexdigest()
// ...     if hex.startswith('00000'):
// ...         break
// ...
// >>> i
// 282749
// >>> i=0
// >>> while True:
// ...     i+=1
// ...     hex = md5(b'yzbqklnj%d' % i).hexdigest()
// ...     if hex.startswith('000000'):
// ...         break
// ...`
