"""Publicación de eventos de dominio en RabbitMQ (Laboratorio 3)."""
import json
import logging
import os
import pika

RABBIT = os.getenv("RABBITMQ_HOST", "rabbitmq")
PARAMS = (pika.URLParameters(RABBIT) if "://" in RABBIT else pika.ConnectionParameters(RABBIT))
EXCHANGE = "tienda.eventos"

def publicar(clave: str, datos: dict) -> bool:
    """Publica un evento con persistencia de mensaje y tres intentos."""
    for intento in range(3):
        try:
            con = pika.BlockingConnection(PARAMS)
            canal = con.channel()
            canal.exchange_declare(EXCHANGE, exchange_type="topic", durable=True)
            canal.basic_publish(
                exchange=EXCHANGE,
                routing_key=clave,
                body=json.dumps(datos),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    content_type="application/json"
                )
            )
            con.close()
            return True
        except Exception as exc:
            logging.warning(
                "Intento %s: no se publicó %s: %s",
                intento + 1,
                clave,
                exc
            )
    return False


def drenar_outbox(redis_client) -> int:
    """Publica eventos pendientes conservados en Redis."""
    publicados = 0
    pendientes = redis_client.lrange("eventos:pendientes", 0, -1)
    for entrada_json in pendientes:
        entrada = json.loads(entrada_json)
        if publicar(entrada["clave"], entrada["datos"]):
            redis_client.lrem("eventos:pendientes", 1, entrada_json)
            publicados += 1
    return publicados