package xkcd

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
)

const XKCDURL = "https://xkcd.com/"

type XkcdInfo struct {
	Month      string `json:"month"`
	Num        int    `json:"num"`
	Link       string `json:"link"`
	Year       string `json:"year"`
	News       string `json:"news"`
	SafeTitle  string `json:"safe_title"`
	Transcript string `json:"transcript"`
	Alt        string `json:"alt"`
	Image      string `json:"img"`
	Title      string `json:"title"`
	Day        string `json:"day"`
}

func SearchXkcdInfo(manga_num int) (*XkcdInfo, error) {
	// url := url.QueryEscape(XKCDURL + string(manga_num) + "/info.0.json")
	url := XKCDURL + strconv.Itoa(manga_num) + "/info.0.json"
	resp, err := http.Get(url)
	defer resp.Body.Close()
	// resp, err := http.Get("https://xkcd.com/571/info.0.json")

	if err != nil {
		return nil, err
	}

	if resp.StatusCode != http.StatusOK {
		resp.Body.Close()
		return nil, fmt.Errorf("search query failed: %s", resp.Status)
	}

	var result XkcdInfo
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		resp.Body.Close()
		return nil, err
	}

	return &result, nil
}
