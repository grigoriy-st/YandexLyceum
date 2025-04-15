package gzipper

import "regexp"

type Work struct {
	Filepath string
}

func FileNameGen(dir string,
	pattern *regexp.Regexp) <-chan Work {

}

func compress(jobs <-chan Work) {

}

func main() {

}
