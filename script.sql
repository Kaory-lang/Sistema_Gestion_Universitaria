create database universidad;
use universidad;

create table usuarios(id int primary key auto_increment, nombre varchar(50), psw varchar(50));

insert into usuarios (nombre, psw) values ('admin', 'admin');
insert into usuarios (nombre, psw) values ('rodolfo', 'rodolfo');
insert into usuarios (nombre, psw) values ('rosa', 'rosa');
insert into usuarios (nombre, psw) values ('usuario', 'contraseña');
insert into usuarios (nombre, psw) values ('admin2', 'admin2');
insert into usuarios (nombre, psw) values ('admin3', 'admin3');
insert into usuarios (nombre, psw) values ('administrador', 'administrador');
insert into usuarios (nombre, psw) values ('administradora', 'administradora');
insert into usuarios (nombre, psw) values ('script', 'script');
insert into usuarios (nombre, psw) values ('2021', '2021');

create table materias(id int primary key auto_increment, nombre varchar(50));

insert into materias (nombre) values ('Español');
insert into materias (nombre) values ('Ingles');
insert into materias (nombre) values ('Historia');
insert into materias (nombre) values ('Matemática');
insert into materias (nombre) values ('Química');
insert into materias (nombre) values ('Física');
insert into materias (nombre) values ('Electiva');
insert into materias (nombre) values ('Programación en C');
insert into materias (nombre) values ('Fisiología animal');
insert into materias (nombre) values ('Mecánica de suelos');

create table carreras(id int primary key auto_increment, nombre varchar(50), materias varchar(50));

insert into carreras (nombre, materias) values ('Informatica','8,5,4,10,1,7');
insert into carreras (nombre, materias) values ('Medicina','4,8,10,1,7'); 
insert into carreras (nombre, materias) values ('Mercadotecnia','2,10,1,7');
insert into carreras (nombre, materias) values ('Ingenieria Civil','5,10,1,7');
insert into carreras (nombre, materias) values ('Contabilidad','2,5,10,1,7');
insert into carreras (nombre, materias) values ('Agrimensura','2,10,8,7');
insert into carreras (nombre, materias) values ('Psicologia','4,2,10,1,7');
insert into carreras (nombre, materias) values ('Derecho','3,9,6,10,1,7');
insert into carreras (nombre, materias) values ('Veterinaria','9,3,6,10,1,7');
insert into carreras (nombre, materias) values ('Administracion De Empresas','2,6,10,1,7');

create table estudiantes(id int primary key auto_increment, nombre varchar(50), carrera varchar(50), materias varchar(50), secciones varchar(50));

insert into estudiantes (nombre, carrera, materias, secciones) values ('Kaory','Informatica','8,5,4','01,04,01S');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Yanel','Medicina','10,7,4','02,08,02S');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Francisco','Mercadotecnia','2,10,1','09,03,02');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Bartolome','Ingenieria Civil','5,10,1','04,06,07');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Pascal','Contabilidad','10,2,1','01,02S,08');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Ramon','Agrimensura','10,2,8','04,01S,09');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Ray','Psicologia','4,2,1','02,01S,04');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Mia','Derecho','3,9,6','02,09,07');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Jenifer','Veterinaria','3,9,6','01,02,03');
insert into estudiantes (nombre, carrera, materias, secciones) values ('Maria','Administracion De Empresas','2,10,6','02S,06,01');

create table profesores(id int primary key auto_increment, nombre varchar(50), carrera varchar(50), materias varchar(50), secciones varchar(50));

insert into profesores (nombre, carrera, materias, secciones) values ('Kaory_profesor','Informatica,otra materia','8,5,4','01,04,01S');
insert into profesores (nombre, carrera, materias, secciones) values ('Yanel_profesor','Medicina,otra materia','10,7,4','02,08,02S');
insert into profesores (nombre, carrera, materias, secciones) values ('Francisco_profesor','Mercadotecnia,otra materia','2,10,1','09,03,02');
insert into profesores (nombre, carrera, materias, secciones) values ('Bartolome_profesor','Ingenieria Civil,otra materia','5,10,1','04,06,07');
insert into profesores (nombre, carrera, materias, secciones) values ('Pascal_profesor','Contabilidad,otra materia','10,2,1','01,02S,08');
insert into profesores (nombre, carrera, materias, secciones) values ('Ramon_profesor','Agrimensura,otra materia','10,2,8','04,01S,09');
insert into profesores (nombre, carrera, materias, secciones) values ('Ray_profesor','Psicologia,otra materia','4,2,1','02,01S,04');
insert into profesores (nombre, carrera, materias, secciones) values ('Mia_profesor','Derecho,otra materia','3,9,6','02,09,07');
insert into profesores (nombre, carrera, materias, secciones) values ('Jenifer_profesor','Veterinaria,otra materia','3,9,6','01,02,03');
insert into profesores (nombre, carrera, materias, secciones) values ('Maria_profesor','Administracion De Empresas,otra materia','2,10,6','02S,06,01');