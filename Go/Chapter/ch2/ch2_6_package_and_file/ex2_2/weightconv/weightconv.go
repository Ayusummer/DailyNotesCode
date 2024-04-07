// 定义重量(磅和公斤)以及重量转换相关的类型和函数
package weightconv

import "fmt"

type Pound float64
type Kilogram float64

const (
	PoundToKilogram = 0.45359237
)

func (p Pound) String() string    { return fmt.Sprintf("%g lb", p) }
func (k Kilogram) String() string { return fmt.Sprintf("%g kg", k) }

func PToK(p Pound) Kilogram { return Kilogram(p * PoundToKilogram) }
func KToP(k Kilogram) Pound { return Pound(k / PoundToKilogram) }
