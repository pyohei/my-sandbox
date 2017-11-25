// Read file
// Filtering with peco
// go to directory
// Build in Linux, Mac, WIndows
// ccccc
package main

import (
	"bytes"
	"context"
	"fmt"
	"github.com/peco/peco"
	"io/ioutil"
	"reflect"
	"strings"
)

func main() {
	// Hacking from peco library.
	content, err := ioutil.ReadFile(".pj")
	if err != nil {
		println(err)
	}
	//fmt.Printf("%s", content)
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	cli := peco.New()
	r := strings.NewReader(string(content))
	//r := strings.NewReader("abcdefghijk")
	cli.Stdin = r
	b := &bytes.Buffer{}
	cli.Stdout = b
	err2 := cli.Run(ctx)
	s := b.String()
	fmt.Println(s)
	fmt.Println(cli.Stdout)
	p := cli.CurrentLineBuffer()
	v, _ := p.LineAt(cli.Location().LineNumber())
	fmt.Println(reflect.TypeOf(v))
	// Get selected row
	fmt.Println(v.Output())
	fmt.Println(p.Size())

	if err2 != nil {
		println("Errordayo-")
		fmt.Println(err2)
	}
}
