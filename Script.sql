CREATE DATABASE DBEmpresa;


CREATE TABLE DBEmpresa.Departamentos
(
id_departamento int(10) primary key AUTO_INCREMENT,
Nombre_departamento varchar(40),
direccion varchar(100)
);


CREATE TABLE DBEmpresa.Empleados 
(
id_empleado integer primary key AUTO_INCREMENT ,
id_departamento integer,
Nombre_empleado VARCHAR(30),
edad integer ,
constraint foreign key(id_departamento) references DBEmpresa.Departamentos(id_departamento)
);




CREATE TABLE DBEmpresa.Notas
(
id_nota integer primary key AUTO_INCREMENT,
id_empleado integer,
contenido varchar(500),
constraint foreign key(id_empleado) references DBEmpresa.Empleados(id_empleado)
);


CREATE TABLE DBEmpresa.Comentarios
(
id_comentario integer primary key AUTO_INCREMENT,
id_empleado integer ,
id_nota integer ,
contenido varchar(400), 
constraint foreign key(id_empleado) references DBEmpresa.Empleados(id_empleado),
constraint foreign key(id_nota) references DBEmpresa.Notas(id_nota)
);


CREATE TABLE DBEmpresa.Likes
(
id_like integer primary key  AUTO_INCREMENT,
id_empleado integer ,
id_nota integer ,
constraint foreign key(id_empleado) references DBEmpresa.Empleados(id_empleado),
constraint foreign key(id_nota) references DBEmpresa.Notas(id_nota)
);

CREATE TABLE DBEmpresa.Programas
(
id_programada integer primary key AUTO_INCREMENT,
fecha date   ,
hora time ,
id_nota integer,
constraint foreign key(id_nota) references DBEmpresa.Notas(id_nota)
);

CREATE TABLE DBEmpresa.Recordatorios
(
id_recordatorio integer primary key AUTO_INCREMENT,
id_nota integer,
fecha date  ,
constraint foreign key(id_nota) references DBEmpresa.Notas(id_nota)
);

ALTER TABLE dbempresa.Notas ADD id_recordatorio int null;
ALTER TABLE dbempresa.Notas add id_programada INT NULL ;

ALTER TABLE dbempresa.Notas ADD FOREIGN KEY (id_recordatorio) REFERENCES Recordatorios(id_recordatorio);
ALTER TABLE dbempresa.Notas ADD FOREIGN KEY (id_programada) REFERENCES Programas(id_programada);

INSERT INTO DBEmpresa.Departamentos(id_departamento, Nombre_departamento, direccion )
VALUES 
(987654321, 'Tecnologia', 'calle falsa 123'),
(987654322, 'Administracion', 'calle falsa 3141592'),
(987654323, 'Contaduria', 'calle falsa 321');
 
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(1234, 987654323, 'Richard Genom', 31);
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(12345789, 987654323, 'Tomas Optimus', 25);
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(123456689, 987654323, 'Tomas Reinhald', 24);
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(123456779, 987654322, 'Tomas Celis', 23);
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(123456785, 987654322, 'Samot Garcia', 20);
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(123456788, 987654322, 'Tomas Kopelson', 22);
INSERT INTO dbempresa.empleados (id_empleado, id_departamento, Nombre_empleado, edad) VALUES(123456789, 987654321, 'Tomas Garcia', 20);


INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(4934, 123456789, 'kjajajajajaja', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(5195, 12345789, 'esta es una nueva nota , igual de contaduria', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(37631, 12345789, 'esta nota la tiene que ver Reinhald', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(46810, 12345789, 'nueva nota de contaduria 
jeje', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(50810, 123456789, 'nueva nota', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(55453, 123456779, 'DORIM
RREEE', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(55777, 123456779, 'nota 2 de mi tom celis', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(65774, 123456779, 'DORIME', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(69510, 123456788, 'Hola , Me llamo Tomas Kopelson', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(92545, 123456779, 'nota 1 de mi
', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(97691, 123456789, 'nueva nota', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(98454, 123456789, 'nueva nota', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(345678911, 123456689, 'nota mas comentada', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(345678912, 123456789, 'nota 1 ', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(345678913, 123456788, 'nota 1 ', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(356789122, 123456689, 'nota 2', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(356789124, 123456789, 'nota 2', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(356789126, 123456788, 'nota 2', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(567891233, 123456689, 'nota 3', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(567891234, 123456789, 'nota 3', NULL, NULL);
INSERT INTO dbempresa.notas (id_nota, id_empleado, contenido, id_recordatorio, id_programada) VALUES(567891237, 123456788, 'nota 3', NULL, NULL);


INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(111, 123456689, 345678911, 'hola');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(11111, 1234, 345678911, 'eesto val ');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(12345, 123456789, 345678912, 'nota 1 puede mejorar');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(13849, 123456689, 356789122, 'estoyu');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(14219, 123456788, 356789126, 'dorime');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(14531, 123456789, 4934, 'esta nota , fue buenisima');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(16948, 123456779, 65774, 'ameno');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(21084, 123456789, 50810, 'jajajajja');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(23459, 12345789, 5195, 'comentario 1 
');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(38865, 123456779, 92545, 'nuevo comentraio , saldra bien ?');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(42582, 123456789, 97691, 'es mucho esta nota ?
');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(50586, 12345789, 46810, 'excelente nota');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(75143, 123456689, 345678911, 'yo');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(81656, 123456779, 55777, 'he comentado');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(91653, 12345789, 37631, 'este va a ser un buen comentario');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(97231, 123456779, 55453, 'dooorime');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(97985, 123456788, 69510, 'dorime');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(123456, 123456789, 356789124, 'nota 2 me parece correcto');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(1234567, 123456789, 567891234, 'nota 3 nais');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(12345678, 123456788, 345678913, 'nota 1 es buena ');
INSERT INTO dbempresa.comentarios (id_comentario, id_empleado, id_nota, contenido) VALUES(123456789, 123456689, 567891233, 'nota 3 antes salia mejor');


INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(3424, 123456788, 345678913);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(3434, 123456789, 345678912);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(6868, 123456689, 345678911);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(7734, 123456788, 356789124);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(11370, 123456779, 92545);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(12343, 123456689, 356789122);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(13526, 123456789, 98454);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(18557, 12345789, 46810);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(28031, 123456785, 356789124);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(32549, 123456788, 356789126);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(37366, 123456785, 356789122);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(38984, 123456689, 567891233);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(39152, 123456779, 356789124);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(39426, 123456789, 4934);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(42884, 123456789, 356789122);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(44489, 12345789, 5195);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(48805, 123456788, 567891237);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(58160, 123456789, 97691);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(59333, 123456785, 92545);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(74888, 12345789, 37631);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(79343, 123456788, 69510);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(87735, 123456789, 50810);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(89877, 123456789, 356789124);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(93457, 12345789, 356789124);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(97996, 123456779, 55777);
INSERT INTO dbempresa.likes (id_like, id_empleado, id_nota) VALUES(123456, 123456789, 567891234);



/*
# Obtener las 3 notas con más "likes
select n.contenido , count(l.id_nota)
from likes l ,empleados e ,notas n 
where 
n.id_nota  = l.id_nota and
l.id_empleado  = e.id_empleado  
group by l.id_nota  
order by count(l.id_nota) desc limit 3;

# Obtener las 10 notas más comentadas.
select n.id_nota , n.contenido, count(c.id_nota )
from Comentarios c , Empleados e , Notas n 
where 
n.id_nota = c.id_nota and
c.id_empleado = e.id_empleado  
group by c.id_nota 
order by count( c.id_nota ) desc limit 10;

# Obtener una lista de usuarios ordenada de manera ascendente según la cantidad de notas propias
select n.id_empleado , e.Nombre_empleado  ,count(n.id_nota) 
from notas n ,empleados e 
where 
n.id_empleado  = e.id_empleado  
group by n.id_empleado  
order by count(n.id_nota) desc;
*/



