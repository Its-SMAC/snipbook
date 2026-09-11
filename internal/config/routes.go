package config

import (
	"net/http"

	"github.com/go-chi/chi/v5"
)

func RegisterRoutes(r *chi.Mux) {

	r.Get("/ping", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("pong"))
	})

	registerSnips(r)
	registerComments(r)
}

func registerComments(r *chi.Mux) {}

func registerSnips(r *chi.Mux) {}
