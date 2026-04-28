//Primero se ejecutan los siguientes comando en la terminal
//go mod init main
//go get github.com/labstack/echo

package main

import (
	"net/http"

	"github.com/labstack/echo"
)

func ObtenerUsuario(c echo.Context) error {
	id := c.Param("id")
	return c.String(http.StatusOK, id)
}

func main() {
	e := echo.New()

	e.GET("/prueba", func(c echo.Context) error {
		return c.String(http.StatusOK, "!Probado!")
	})

	e.GET("usuario/:id", ObtenerUsuario)
	e.Logger.Fatal(e.Start(":1000"))
}
