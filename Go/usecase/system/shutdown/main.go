// 半小时自动关机 shutdown -s -t 1800
package main

import "os/exec"

func main() {
	cmd := exec.Command("shutdown", "-s", "-t", "1800")
	cmd.Run()
}
