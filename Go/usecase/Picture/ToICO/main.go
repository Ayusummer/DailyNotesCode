package main

import (
	"flag"
	"image"
	"image/draw"
	"image/jpeg"
	"image/png"
	"os"
	"strconv"
	"strings"

	ico "github.com/Kodeworks/golang-image-ico"
	"github.com/nfnt/resize"
)

var inputFile = flag.String("i", "", "input file")
var outputFile = flag.String("o", "", "output file")
var size = flag.Uint("size", 0, "icon size")

func main() {
	flag.Parse()

	file, err := os.Open(*inputFile)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var img image.Image
	if strings.HasSuffix(*inputFile, ".png") {
		img, err = png.Decode(file)
	} else if strings.HasSuffix(*inputFile, ".jpg") || strings.HasSuffix(*inputFile, ".jpeg") {
		img, err = jpeg.Decode(file)
	}
	if err != nil {
		panic(err)
	}

	bounds := img.Bounds()
	m := image.NewRGBA(image.Rect(0, 0, bounds.Dx(), bounds.Dy()))
	draw.Draw(m, m.Bounds(), img, bounds.Min, draw.Src)

	// 默认 ico 分辨率列表 16x16, 32x32, 48x48, 64x64, 128x128, 256x256
	var iconSizes = []uint{16, 32, 48, 64, 128, 256}

	// 如果指定了 icon size, 则只生成指定大小的 icon
	if *size != 0 {
		iconSizes = []uint{*size}
	}

	for _, size := range iconSizes {
		resizedImage := resize.Resize(size, size, m, resize.Lanczos3)
		m, ok := resizedImage.(*image.RGBA)
		if !ok {
			m = image.NewRGBA(image.Rect(0, 0, resizedImage.Bounds().Dx(), resizedImage.Bounds().Dy()))
			draw.Draw(m, m.Bounds(), resizedImage, resizedImage.Bounds().Min, draw.Src)
		}

		iconFile, err := os.Create(*outputFile + "_" + strconv.Itoa(int(size)) + ".ico")
		if err != nil {
			panic(err)
		}
		defer iconFile.Close()

		ico.Encode(iconFile, m)
	}
}
