<<<<<<< HEAD
# tiendaia-equipo1
Integrantes
Jose Maria Santiago Antonio
Saul Gonzales Campillo
Adiel Josafat Aguilar Hernandez

## Inicio rapido

```bash
cp .env.ejemplo .env
docker compose up -d --build
```

Servicios principales:

- Frontend: `http://localhost:8081`
- API Gateway: `http://localhost:8080`
- RabbitMQ: `http://localhost:15672`
- Salud del sistema: `http://localhost:8080/health`

## Configuracion

Copie `.env.ejemplo` a `.env` y configure las contrasenas y credenciales.
No coloque secretos reales en archivos versionados.

## Calidad y operacion

- Los microservicios exponen `/health`.
- Redis y RabbitMQ tienen healthchecks en Docker Compose.
- Los eventos de ventas pendientes se conservan en Redis y se reintentan al publicar.
- El modelo de IA se reemplaza de forma atomica despues de entrenarlo.
- El gateway devuelve `502` ante fallos de conexion y `504` ante timeouts.
=======
# testserver04
>>>>>>> b5d0d9620a8e2bffd63c12b1ee4bb28929f8a11a
