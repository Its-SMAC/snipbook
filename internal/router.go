package internal

import (
	"snipbook/internal/config"

	"github.com/go-chi/chi/v5"
)

func StartApp() *chi.Mux {
	r := chi.NewRouter()

	config.LoadMiddlewares(r)
	config.RegisterRoutes(r)

	return r
}
