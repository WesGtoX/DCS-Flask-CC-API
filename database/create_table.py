import sqlite3

try:
    conn = sqlite3.connect("database/data.db")
    conn = sqlite3.connect("DROP TABLE IF EXISTS tb_cliente;")
    conn.execute(
        """
        CREATE TABLE tb_cliente (
            id INTEGER PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        );
        """
    )
    conn.execute(
        """
        INSERT INTO `tb_cliente` (`id`,`nome`,`email`,`telefone`)
        VALUES
            (1,"Jessamine Mccormick","aenean.massa@hotmail.com","1-717-423-8711"),
            (2,"Whoopi Morrow","mauris@icloud.com","1-283-983-7455"),
            (3,"Jackson Warner","dis@aol.couk","(486) 570-0422"),
            (4,"Lev Whitley","fermentum.vel@outlook.net","1-763-754-0116"),
            (5,"Bryar James","dolor@outlook.couk","1-223-348-6102"),
            (6,"Jescie Cruz","ut.dolor.dapibus@icloud.edu","1-373-223-2728"),
            (7,"Lacey Madden","pretium.aliquet@yahoo.ca","1-377-359-7657"),
            (8,"Bethany Bonner","ac.turpis@google.com","1-413-322-4874"),
            (9,"Sawyer Garcia","odio.vel.est@hotmail.com","(551) 495-4664"),
            (10,"Regina Gilmore","ante.vivamus.non@outlook.org","(590) 262-4619");
        """
    )
    conn.commit()
    print("Operacao realizada com sucesso!")
except Exception as e:
    print(f"ERRO {e}")
finally:
    conn.close()
