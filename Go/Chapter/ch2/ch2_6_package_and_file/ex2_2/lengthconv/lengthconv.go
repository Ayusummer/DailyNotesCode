// 定义长度（英尺和米）以及长度转换相关的类型和函数
package lengthconv

import "fmt"

type Feet float64
type Meter float64

const (
	FeetToMeter = 0.3048
)

func (f Feet) String() string  { return fmt.Sprintf("%g ft", f) }
func (m Meter) String() string { return fmt.Sprintf("%g m", m) }

func FToM(f Feet) Meter { return Meter(f * FeetToMeter) }
func MToF(m Meter) Feet { return Feet(m / FeetToMeter) }
