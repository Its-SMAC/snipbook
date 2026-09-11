package main

import (
	"net/http"
	"snipbook/internal"
)

func main() {
	http.ListenAndServe(":3000", internal.StartApp())
}
