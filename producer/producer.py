from fastapi import FastAPI
import pika

app = FastAPI()


# ヘルスチェック用
@app.get("/")
def read_root():
    return {"Status": "OK"}


# RabbitMQ用
@app.get("/add-job/{message}")
def add_job(message: str):
    # RabbitMQサーバと接続
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq"))
    # チャンネルの確立
    channel = connection.channel()
    # メッセージを格納するためのキュー(task_queue)を作成
    channel.queue_declare(queue="task_queue", durable=True)
    # メッセージをキュー(task_queue)に格納
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # メッセージの永続化
        ))
    # 接続のクローズ及びメッセージが配信されたことを確認
    connection.close()

    return {"send": message}
