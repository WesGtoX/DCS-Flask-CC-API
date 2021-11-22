import sqlite3
from flask import Blueprint, request, jsonify

cliente = Blueprint("cliente", __name__)


def conectar():
    return sqlite3.connect("database/data.db")


@cliente.route("/", methods=["GET"])
def get_all():
    clientes = []
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente")

        for i in cur.fetchall():
            cliente = {}
            cliente["id"] = i["id"]
            cliente["nome"] = i["nome"]
            cliente["email"] = i["email"]
            cliente["telefone"] = i["telefone"]
            clientes.append(cliente)
    except Exception as e:
        print(e)
        clientes = []

    return jsonify(clientes)


@cliente.route("/<id>", methods=["GET"])
def get_by_id(id):
    cliente = {}
    try:
        conn = conectar()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tb_cliente where id=?", (id,))
        row = cur.fetchone()

        cliente["id"] = row["id"]
        cliente["nome"] = row["nome"]
        cliente["email"] = row["email"]
        cliente["telefone"] = row["telefone"]

    except Exception as e:
        print(str(e))
        cliente = {}

    return jsonify(cliente)


@cliente.route("/", methods=["POST"])
def add():
    cliente = request.get_json()
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tb_cliente (nome, email, telefone) VALUES (?, ?, ?)",
            (cliente["nome"], cliente["email"], cliente["telefone"]),
        )
        conn.commit()
        resposta = jsonify(
            {"mensagem": "Operacao realizada com sucesso", "id": cur.lastrowid}
        )
    except Exception as e:
        conn.rollback()
        resposta = jsonify({"erro": str(e)})
    finally:
        conn.close()
    return resposta


@cliente.route("/", methods=["PUT"])
def update():
    cliente = request.get_json()

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute(
            "UPDATE tb_cliente SET nome=?, email=?, telefone=? WHERE id=?",
            (
                cliente["nome"], cliente["email"],
                cliente["telefone"], cliente["id"]
            ),
        )
        conn.commit()
        resposta = jsonify({"mensagem": "Operacao realizada com sucesso"})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({"erro": str(e)})
    finally:
        conn.close()

    return resposta


@cliente.route("/<id>", methods=["DELETE"])
def delete(id):
    print(id)
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM tb_cliente WHERE id=?", (id,))
        conn.commit()
        resposta = jsonify({"mensagem": "Registro apagado com sucesso"})

    except Exception as e:
        conn.rollback()
        resposta = jsonify({"erro": str(e)})
    finally:
        conn.close()

    return resposta
