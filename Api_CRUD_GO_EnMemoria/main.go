//Con el siguiente codigo en el terminal, se descarga la libreria que pertenece a go llamada MUX
//go get github.com/gorilla/mux

package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

var gente []Personas

type Personas struct {
	Cedula    string     `json:"cedula,omitempty"`
	Nombre    string     `json:"nombre,omitempty"`
	Apellido  string     `json:"apellido,omitempty"`
	Direccion *Direccion `json:"direccion,omitempty"`
}

type Direccion struct {
	Ciudad string `json:"ciudad,omitempty"`
	Barrio string `json:"barrio,omitempty"`
}

// EndPoints
func ObtenerPersonasEndPoint(w http.ResponseWriter, req *http.Request) {
	params := mux.Vars(req)
	for _, item := range gente {
		if item.Cedula == params["cedula"] {
			json.NewEncoder(w).Encode(item)
			return
		}
	}
	json.NewEncoder(w).Encode(&Personas{})
}

func ObtenergenteEndPoint(w http.ResponseWriter, req *http.Request) {
	json.NewEncoder(w).Encode(gente)
}

func CrearPersonasEndPoint(w http.ResponseWriter, req *http.Request) {
	params := mux.Vars(req)
	var Personas Personas
	_ = json.NewDecoder(req.Body).Decode(&Personas)
	Personas.Cedula = params["cedula"]
	gente = append(gente, Personas)
	json.NewEncoder(w).Encode(gente)

}

func DeletePersonasEndpoint(w http.ResponseWriter, req *http.Request) {
	params := mux.Vars(req)
	for index, item := range gente {
		if item.Cedula == params["cedula"] {
			gente = append(gente[:index], gente[index+1:]...)
			break
		}
	}
	json.NewEncoder(w).Encode(gente)
}

func main() {
	router := mux.NewRouter()

	// adding example data
	gente = append(gente, Personas{Cedula: "1", Nombre: "ejmplo_nombre1", Apellido: "ejemplo_apellido1", Direccion: &Direccion{Ciudad: "gris", Barrio: "Barrios"}})
	gente = append(gente, Personas{Cedula: "2", Nombre: "ejemplo_nombre2", Apellido: "ejemplo_apellido2", Direccion: &Direccion{Ciudad: "gris", Barrio: "Barrios"}})

	// endpoints
	router.HandleFunc("/gente", ObtenergenteEndPoint).Methods("GET")
	router.HandleFunc("/gente/{cedula}", ObtenerPersonasEndPoint).Methods("GET")
	router.HandleFunc("/gente/{cedula}", CrearPersonasEndPoint).Methods("POST")
	router.HandleFunc("/gente/{cedula}", DeletePersonasEndpoint).Methods("DELETE")

	log.Fatal(http.ListenAndServe(":3000", router))
}
