package gzipper

import (
	"compress/gzip"
	"io"
	"os"
	"path/filepath"
	"regexp"
	"sync"
)

type Work struct {
	FilePath string
}

func FileNameGen(dir string, pattern *regexp.Regexp) <-chan Work {
	out := make(chan Work)
	go func() {
		defer close(out)
		entries, err := os.ReadDir(dir)
		if err != nil {
			return
		}
		for _, entry := range entries {
			if entry.IsDir() {
				continue
			}
			if pattern.MatchString(entry.Name()) && entry.Name() != "input.txt" && entry.Name() != "output.txt" {
				fullPath := filepath.Join(dir, entry.Name())
				out <- Work{FilePath: fullPath}
			}
		}
	}()
	return out
}

func compress(jobs <-chan Work) {
	var wg sync.WaitGroup
	for job := range jobs {
		wg.Add(1)
		go func(job Work) {
			defer wg.Done()
			inFile, err := os.Open(job.FilePath)
			if err != nil {
				return
			}
			defer inFile.Close()

			outPath := job.FilePath + ".gz"
			outFile, err := os.Create(outPath)
			if err != nil {
				return
			}
			defer outFile.Close()

			gzWriter := gzip.NewWriter(outFile)
			defer gzWriter.Close()

			io.Copy(gzWriter, inFile)
		}(job)
	}
	wg.Wait()
}
