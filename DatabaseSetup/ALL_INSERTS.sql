insert into Areas values(1,'Literatura');
insert into Areas values(2,'Biologia');
insert into Areas values(3,'Matematicas');
insert into Areas values(4,'Fisica');
insert into Areas values(5, 'Cuentos');
insert into Areas values(6, 'Computacion');
insert into Areas values(7, 'Derecho');
insert into Areas values(8, 'Multimedia');
insert into Areas values(9, 'Quimica');
insert into Areas values(10, 'Ciencias Politicas');
insert into Areas values(11, 'Educacion');

insert into Editoriales values(1, 'Alfaguara')
insert into Editoriales values(2, 'Black cat')
insert into Editoriales values(3, 'Educar')
insert into Editoriales values(5, 'Norma')
insert into Editoriales values(6, 'Eureka')
insert into Editoriales values(8, 'Enlace')

INSERT INTO Carreras VALUES(1,'DERECHO')
INSERT INTO Carreras VALUES(2,'NEGOCIOS INTERNACIONALES')
INSERT INTO Carreras VALUES(10,'INGENIERIA DE SISTEMAS')

---- ======================================
----- INSERT DE DATOS PARA LIBROS----------
------------------------------------------
insert into libro values (1,'El Aleph',2,5);
insert into libro values (2,'Alicia en el pais de las maravillas',1,1);
insert into libro values (3,'Matematica estas ahi',2,3);
insert into libro values (4,'Martin Fierro',3,1);
insert into libro values (5,'Martin Fierro',2,1);
insert into Libro values  (6, 'Diseño de Pagina Web con XHTML, JavaScript y CSS', 6, 6);
insert into Libro values  (7, 'Prgramación de graficos 3D', 6, 6);
insert into Libro values  (8, 'MySQl y JAVA',2, 6);
insert into Libro values  (9, 'Manual básico de derecho administrativo', 5, 7);
insert into Libro values(10, 'Sistema Juridico de administración publica', 5, 7);
insert into Libro values(11, 'Derecha administrativo 1ra Ed.', 5, 7);
insert into Libro values(12, 'Derecho administrativo 2da Ed.',5, 7);
insert into Libro values(13, 'Sistemas de bases de datos', 6,6);
insert into Libro values(14, 'Fundamentos de diseño de bases de datos', 5, 6);
insert into Libro values(15, 'SQL Server 2008',8, 6);
insert into Libro values(16, 'Microsoft Visual Basic.Net',8, 6);
insert into Libro values(17, '3d Studio Max', 8, 8);

insert into autor values (100,'Jorge Luis Borges','ARG');
insert into autor values( 200, 'Lewis Carroll','GRB');
insert into autor values( 300,'Adrian Paenza','ARG'); 
insert into autor values( 400,'Jose hernandez','ARG');
insert into autor values( 500, 'Mª Nieves Navas Martinez','COL');
insert into autor values( 600,'Juan carlos oros cabello','ESP');
insert into autor values( 700, 'Eduardo Gamero Casado','ESP');
insert into autor values( 705, 'Severiano Fernández Ramos','ARG');
insert into autor values( 710,'Mark Matthews','USA');
insert into autor values( 720,'FrAANCISCO JaVIER bermal','COL');
insert into autor values( 510,'Thomas M. Connolly','USA');
insert into autor values( 520,' S. Sudarshan', 'USA');
insert into autor values( 530,'  Abraham Silberschatz', 'USA');
insert into autor values( 540,'  Jérôme Gabillaud','FRA');
insert into autor values( 900, ' CEBALLOS FCO.JAVIER', 'ESP');
insert into autor(id_Autor,nombre) values( 1000, ' TecnoBook')

-------------------------------ESTUDIANTE---------------
Insert into Estudiante values(32311,'CC-7175822','Moises Alejandro Pérez','CALLE 18 N25 30',10,29);
insert into Estudiante  values(23411,'TI-48987599','America Maria Gómez',NULL,1,15 );
insert into Estudiante  values(6782,'CE-AER52000','Javier Adrian Serrano',NULL ,2,51 );
insert into Estudiante  values(67812,'CC-369871', 'JUAN RAFAEL LOZANO',NULL,1,30);
insert into Estudiante  values(92112,'TI-300785070','Melissa Mendoza Palacios',NULL,1, NULL);

-------------------------------------------------------
----------LIBROS ASOCIADOS A SUS AUTORES --------------
insert into libAut values(100,1);
insert into libAut values(200,2);
insert into libAut values(300,3);
insert into libAut values(400,4);
insert into libAut values(400,5);
insert into libAut values(500,6);
insert into libAut values(600,6);
insert into libAut values(500,7);
insert into libAut values(600,7);
insert into libAut values(710,8);
insert into libAut values(700,9);
insert into libAut values(705,9);
insert into libAut values(720,10);
insert into libAut values(720,11);
insert into libAut values(720,12);
insert into libAut values(510,13);
insert into libAut values(520,14);
insert into libAut values(530,14);
insert into libAut values(540,15);
insert into libAut values(900,16);
insert into libAut values(600,17);

insert into Prestamo values (23411, 1, '3/6/2022', 0, NULL,0);