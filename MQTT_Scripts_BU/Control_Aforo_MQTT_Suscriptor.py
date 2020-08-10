# encoding: utf-8
import paho.mqtt.client as mqtt  # importa el cliente
import time
from pymongo import MongoClient

stop_subscription = False




# =======================================================================
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


def save_on_database(message):
    try:
        conn = MongoClient()
        print("Conexión con la base de datos establecida!!!")
    except:
        print("Error al establecer conexión con la base de datos")

    db = conn.database
    collection = db.MerakiMV_Subcriptions
    print("Base de datos Configurada")

    detalles_topico = message.topic.split('/')

    for temp in detalles_topico:
        print(temp)

    print("Colección creada")

    publicacion = {
        "camara_serial": message.topic.split('/')[2],
        "zona": message.topic.split('/')[3],
        "topico=": message.topic,
        "publicacion": str(message.payload.decode("utf-8")),
        "qos=": message.qos,
        "retain_flag": message.retain
    }

    print("Recibido: ", publicacion)

    id_suscripcion = collection.insert_one(publicacion)

    print("Suscricion guardada con el id ", id_suscripcion)


# client.unsubscribe("/merakimv/Q2GV-4YBM-YWWJ/#")


# =======================================================================

def on_message(client, userdata, message):
    print("============================================================")
    print("Mensaje Completo: ", message)
    print("Publicación ", str(message.payload.decode("utf-8")))
    print("Topico=", message.topic)
    print("QoS=", message.qos)
    print("Retain Flag=", message.retain)
    save_on_database(message)


# =======================================================================

broker_address = "5.196.27.225"
# broker_address="iot.eclipse.org"
client = mqtt.Client("SMF_MerakiMV")  # crea una nueva instancia

client.on_connect = on_connect
client.on_message = on_message  # asigna la función on_message al callback
#client.tls_set(“/path/to/ca.crt”)
print("Broker configurado")
#client.username_pw_set("admin", "admin")
client.connect(broker_address)  # conecta al broker
#client.loop_start()  # inicia el ciclo de recolección de publicaciones
print("Conexión con el broker: " + broker_address)

#client.subscribe("/merakimv/Q2GV-4YBM-YWWJ/0")  # Realiza la petición de suscripción
client.subscribe("/merakimv/Q2GV-4YBM-YWWJ/#")  # Realiza la petición de suscripción
print("Suscrito al tópico: ", "/merakimv/Q2GV-4YBM-YWWJ/#")

#print("Publicando en broker","/merakimv/Q2GV-4YBM-YWWJ/0")
#client.publish("/merakimv/Q2GV-4YBM-YWWJ/0","OFF")

# while (stop_subscription == False):
# print("waiting...")

# client.unsubscribe("/merakimv/Q2GV-4YBM-YWWJ/#")
# print("Desuscrito al tópico","/merakimv/Q2GV-4YBM-YWWJ/#")

#time.sleep(1000)  # tiempo de espera para que se ejecute el proceso de recolección de publicciones

#client.loop_stop()  # detiene la recolección de publicaciones

client.loop_forever()