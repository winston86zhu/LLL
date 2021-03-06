// 牛家村的货币是一种很神奇的连续货币。

// 他们货币的最大面额是n，并且一共有面额为1，面额为2.....面额为n，n种面额的货币。

// 牛牛每次购买商品都会带上所有面额的货币，支付时会选择给出硬币数量最小的方案。

// 现在告诉你牛牛将要购买的商品的价格，你能算出牛牛支付的硬币数量吗？ (假设牛牛每种面额的货币都拥有无限个。)

// 输入格式
// 共一行，包含两个整数n和m，分别表示货币的最大面额以及商品的价格。

// 输出格式
// 一个整数表示牛牛支付的硬币数量。

// 数据范围
// 1≤n≤105,
// 1≤m≤109
// 输入样例1：
// 6 7
// 输出样例1：
// 2
// 输入样例2：
// 4 10
// 输出样例2：
// 3

package main

import (
	"fmt"
	"os"
)

func minCoins(n, m int) int {
	mod := 0
	if m%n != 0 {
		mod = 1
	}
	return int(m/n) + mod
}

func main() {
	var n, m int
	fmt.Fscanln(os.Stdin, &n, &m)
	fmt.Println(minCoins(n, m))
}
