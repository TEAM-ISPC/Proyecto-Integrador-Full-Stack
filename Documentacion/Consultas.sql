-- Tabla Usuario
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "Campos", "Emanuel", "email@com.com", 1234, "351241214");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "rojas", "marcos", "marcos@com.com", 'marcos2k', "3523092919");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "cardelli", "yohana", "yohana@com.com", 'yoha2020', "353412231");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "garelli", "mauricio", "mauricio@com.com",'mauri2k', "351231235");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "salas", "santiago", "santiago@com.com", 'dog2022', "355421313");
SELECT * FROM usuarios;
SELECT idUsuario, nombre FROM usuarios;
SELECT * FROM usuarios where nombre = 'yohana';
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados) VALUES (0,'igualdad 5886', 10 , 330);
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados) VALUES (0,'colon 1290', 3 , 120);
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados) VALUES (0,'marcelo t alvear 493', 1 , 20);
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados) VALUES (0,'calazan 1233', 34 , 12330);
SELECT * FROM Clientes
-- Continuar aqui