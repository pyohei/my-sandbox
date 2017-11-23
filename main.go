// Read file
// Filtering with peco
// go to directory
// Build in Linux, Mac, WIndows
// ccccc
package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	content, err := ioutil.ReadFile(".pj")
	if err != nil {
		println(err)
	}
	fmt.Printf("%s", content)
	println("This is test")
}
