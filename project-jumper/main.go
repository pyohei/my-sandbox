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
	"os"
	"os/exec"
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
	nd := v.Output()
	fmt.Println(p.Size())
	fmt.Println(nd)
	eee := os.Chdir("/")
	if eee != nil {
		println("Errordayo----jj-")
		fmt.Println(eee)
	}
	mydir, rr := os.Getwd()
	if rr == nil {
		fmt.Println(mydir)
	}
	cmd := exec.Command("cd")
	cmd.Dir = "/tmp" // or whatever directory it's in
	out, err := cmd.Output()
	if err != nil {
		panic(err)
	} else {
		fmt.Printf("%s", out)
	}

	er := exec.Command("cd /tmp").Run()
	if er != nil {
		panic(er)
	} else {
		fmt.Printf("%s", out)
	}

	if err2 != nil {
		println("Errordayo-")
		fmt.Println(err2)
	}
}
