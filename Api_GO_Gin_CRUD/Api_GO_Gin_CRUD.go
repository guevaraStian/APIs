// Este es un software api en el cual se puede hacer CRUD
// go version
// go mod init go-gin-crud
// go get -u github.com/gin-gonic/gin

package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Estructura de los datos de libro
type Libro struct {
	ID     string `json:"id"`
	Title  string `json:"title"`
	Author string `json:"author"`
}

// Simulamos una base de datos en memoria em forma de json
var Libros = []Libro{
	{ID: "1", Title: "Cien años de soledad", Author: "Gabiel Garcia Marquez"},
	{ID: "2", Title: "Las venas abiertas de latinoamerica", Author: "Eduardo Galeano"},
}

// Obtener la informacion de todos los libros
func Mostrar_todos_libros(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, Libros)
}

// Mostrar los datos de un libro por ID
func Mostrar_un_libros(c *gin.Context) {
	id := c.Param("id")
	for _, Libro := range Libros {
		if Libro.ID == id {
			c.IndentedJSON(http.StatusOK, Libro)
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{"message": "El libro que busca, no se encontro"})
}

// Crear los datos de un nuevo libro
func Crear_libro(c *gin.Context) {
	var nuevo_libro Libro
	if err := c.BindJSON(&nuevo_libro); err != nil {
		return
	}
	Libros = append(Libros, nuevo_libro)
	c.IndentedJSON(http.StatusCreated, nuevo_libro)
}

// Actualizar la informacion de un libro
func Editar_libro(c *gin.Context) {
	id := c.Param("id")
	var libro_editado Libro
	if err := c.BindJSON(&libro_editado); err != nil {
		return
	}

	for i, Libro := range Libros {
		if Libro.ID == id {
			Libros[i] = libro_editado
			c.IndentedJSON(http.StatusOK, libro_editado)
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{"message": "El Libro que usted busco no se encontro"})
}

// Codigo que sirve para eliminar un libro
func Eliminar_libro(c *gin.Context) {
	id := c.Param("id")
	for i, Libro := range Libros {
		if Libro.ID == id {
			Libros = append(Libros[:i], Libros[i+1:]...)
			c.JSON(http.StatusOK, gin.H{"message": "El libro que usted escogio fue eliminado"})
			return
		}
	}
	c.JSON(http.StatusNotFound, gin.H{"message": "El libro que busca, no se encontro"})
}

func main() {
	router := gin.Default()

	router.GET("/Libros", Mostrar_todos_libros)
	router.GET("/Libros/:id", Mostrar_un_libros)
	router.POST("/Libros", Crear_libro)
	router.PUT("/Libros/:id", Editar_libro)
	router.DELETE("/Libros/:id", Eliminar_libro)

	router.Run(":8080")
}
