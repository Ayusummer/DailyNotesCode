package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"log"
	"math"
	"math/rand"
	"net/http"
	"strconv"
	"time"
)

var palette = []color.Color{color.White, color.Black}

const (
	whiteIndex = 0 // first color in palette
	blackIndex = 1 // next color in palette
)

func lissajous(out io.Writer, cyclesInt int) {
	const (
		res     = 0.001 // angular resolution
		size    = 100   // image canvas covers [-size..+size]
		nframes = 64    // number of animation frames
		delay   = 8     // delay between frames in 10ms units
	)
	/* rand.Float64() 返回一个 64 位也即小数点后保留 16 位的浮点数 f，
	0.0 <= f < 1.0*/
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		cycles := float64(cyclesInt)
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5),
				blackIndex)
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	// EncodeAll 函数将生成的  gif anim 写入到 out 中
	gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}

func handler(w http.ResponseWriter, r *http.Request) {
	rand.Seed(time.Now().UTC().UnixNano())
	// 从 r 中接收 URL Query 参数 cycles
	cyclesStr := r.URL.Query().Get("cycles")
	cyclesInt, err := strconv.Atoi(cyclesStr)
	if err != nil {
		log.Print(err)
	}
	lissajous(w, cyclesInt)
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}
