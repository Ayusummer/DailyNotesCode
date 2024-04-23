package main

import (
	xkcd "GoLearning/Chapter/ch4/ch4_5_json/ex4_11/xkcd"
	"encoding/json"
	"fmt"
	"log"
	"os"
	"regexp"
	"strings"
	"time"
)

func rangeInt(start, end int) []int {
	var result []int
	for i := start; i < end; i++ {
		result = append(result, i)
	}
	return result
}

func getAndSaveMangaInfo() {
	var manga_num_list = rangeInt(571, 580)

	// 漫画信息列表, 存储漫画信息
	var manga_info_list []*xkcd.XkcdInfo = make([]*xkcd.XkcdInfo, 10)

	for i, manga_num := range manga_num_list {
		result, err := xkcd.SearchXkcdInfo(manga_num)
		if err != nil {
			log.Fatal(err)
		}
		log.Printf("Xkcd #%d: %s\n", manga_num, result.Title)
		manga_info_list[i] = result
		// 延时 1 秒
		time.Sleep(1 * time.Second)
	}

	// 将漫画信息保存到 xkcd.json 文件中
	xkcd_json_path := "xkcd.json"
	// 将漫画信息保存到 xkcd.json 文件中
	file, err := os.Create(xkcd_json_path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	err = encoder.Encode(manga_info_list)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Xkcd info has been saved to %s\n", xkcd_json_path)
}

// 从 json 数据中模糊查询漫画名称对应的 img 地址
func searchMangaImg(manga_name string, manga_info_list []*xkcd.XkcdInfo) string {
	for _, manga_info := range manga_info_list {
		if manga_info != nil {
			match, err := regexp.MatchString(manga_name, strings.ToLower(manga_info.Title))
			if err != nil {
				log.Fatal(err)
			}

			if match {
				return manga_info.Image
			}
		}
	}
	return ""
}

func main() {
	// 获取当前文件路径
	currentPath, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}
	// 读取 xkcd.json 文件中的漫画信息
	xkcd_json_path := currentPath + "/xkcd.json"
	file, err := os.Open(xkcd_json_path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	decoder := json.NewDecoder(file)
	var manga_info_list []*xkcd.XkcdInfo
	err = decoder.Decode(&manga_info_list)
	if err != nil {
		log.Fatal(err)
	}

	// 模糊查询漫画名称对应的 img 地址
	manga_name := "sleep"
	fmt.Printf("The img url of %s is %s\n", manga_name, searchMangaImg(manga_name, manga_info_list))

}
