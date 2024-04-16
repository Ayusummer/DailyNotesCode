package main

import (
	"image"
	"image/color"
	"image/png"
	"math/cmplx"
	"os"
)

func main() {
	f, err := os.Create("mandelbrot.png")
	if err != nil {
		panic(err)
	}

	const (
		xmin, ymin, xmax, ymax = -2, -2, +2, +2
		width, height          = 1024, 1024
	)

	img := image.NewRGBA(image.Rect(0, 0, width, height))
	for py := 0; py < height; py++ {
		y := float64(py)/height*(ymax-ymin) + ymin
		for px := 0; px < width; px++ {
			x := float64(px)/width*(xmax-xmin) + xmin
			// calculate the average color of four sub-pixels
			var r, g, b uint32
			for i := 0; i < 2; i++ {
				for j := 0; j < 2; j++ {
					z := complex(x+float64(i)/width*(xmax-xmin), y+float64(j)/height*(ymax-ymin))
					red, green, blue, _ := mandelbrot(z).RGBA()
					r += uint32(red)
					g += uint32(green)
					b += uint32(blue)
				}
			}
			img.Set(px, py, color.RGBA{uint8(r / 4 >> 8), uint8(g / 4 >> 8), uint8(b / 4 >> 8), 255})
		}
	}
	png.Encode(f, img)
}

func mandelbrot(z complex128) color.Color {
	const iterations = 200
	const contrast = 15

	var v complex128
	for n := uint8(0); n < iterations; n++ {
		v = v*v + z
		if cmplx.Abs(v) > 2 {
			return color.RGBA{
				R: uint8(contrast * n % 255),
				G: uint8(255 - contrast*n%255),
				B: uint8((contrast * n / 2) % 255),
				A: 255,
			}
		}
	}
	return color.RGBA{0, 0, 0, 255}
}
