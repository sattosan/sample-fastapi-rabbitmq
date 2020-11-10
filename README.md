# FastAPIを使ったRabbitMQのサンプル
# デモ

# 動作環境
* docker ver:19
* docker-compose ver:1.27

# インストール
## クローン
```bash
$ git clone git@github.com:sattosan/sample-fastapi-rabbitmq.git
```
## コンテナの構築
```bash
$ docker-compose up -d --build
```

# ユースケース
## クライアントを起動
```bash
$ docker-compose run --rm consumer sh
$ python consumer.py
```

## メッセージの送信と受信
### heyの送信
```bash
 $ curl http://localhost:8000/add-job/hey
 {"send":"hey"}
```

### heyの受信
メッセージ送信後，クライアント側に下記が表示されるはずです
```bash
 [x] Received b'hey'
hey there
 [x] Done
```

### helloの送信
```bash
 $ curl http://localhost:8000/add-job/hello
 {"send":"hello"}
```

### helloの受信
メッセージ送信後，クライアント側に下記が表示されるはずです
```bash
 [x] Received b'hello'
well hello there
 [x] Done
```
