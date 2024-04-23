// 修改issues程序，根据问题的时间进行分类，比如不到一个月的、不到一年的、超过一年。
package main

import (
	"fmt"
	"log"
	"time"

	github "GoLearning/Chapter/ch4/ch4_5_json/github"
)

func main() {
	// 获取当前时间(年月日)
	currentDate := time.Now()
	// 一个月前的时间
	oneMonthAgo := currentDate.AddDate(0, -1, 0)
	// 一年前的时间
	oneYearAgo := currentDate.AddDate(-1, 0, 0)

	classifyIssues := map[string][]*github.Issue{
		"一个月内": []*github.Issue{},
		"一年内":  []*github.Issue{},
		"一年前":  []*github.Issue{},
	}

	// result, err := github.SearchIssues(os.Args[1:])
	var repo = []string{"PKUFlyingPig/cs-self-learning"}
	result, err := github.SearchIssues(repo)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%d issues:\n", result.TotalCount)
	for _, item := range result.Items {
		if item.CreatedAt.After(oneMonthAgo) {
			classifyIssues["一个月内"] = append(classifyIssues["一个月内"], item)
		} else if item.CreatedAt.After(oneYearAgo) {
			classifyIssues["一年内"] = append(classifyIssues["一年内"], item)
		} else {
			classifyIssues["一年前"] = append(classifyIssues["一年前"], item)
		}
	}

	for k, v := range classifyIssues {
		fmt.Printf("Issues %s:\n", k)
		for _, item := range v {
			fmt.Printf("#%-5d %9.9s %.55s %v\n", item.Number, item.User.Login, item.Title, item.CreatedAt)
		}
	}

}
