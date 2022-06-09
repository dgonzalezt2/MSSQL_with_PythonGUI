create table Editoriales(
	id_editorial varchar(5) not null primary key,
	nombre_editorial varchar(255)
);

create table Carreras(
	id_carrera varchar(30) not null primary key,
	nombre_carrera varchar(255)
);
create table Areas(
	AREA varchar(5) not null primary key,
	DESCRIPCION_AREA varchar(255)
);
create table Libro(
	id_Libro		int Not Null Primary key,
	titulo	varchar(255),
	id_editorial varchar(5) references Editoriales,
	AREA  varchar(5) references Areas
);

create table Autor(
	id_Autor	int Not Null primary key,
	nombre varchar(255),
	nacionalidad varchar(3)
);

create table Estudiante(
	id_Lector int Not Null primary key,
	CI		varchar(255),
	nombre	varchar(255),
	direccion varchar(255),
	id_carrera varchar(30) references Carreras,
	edad int,


);

create table LibAut(
	
	id_Autor	int Not Null references Autor,
	id_Libro    int Not Null references Libro,
	primary key (id_Autor,id_Libro)
);

create table Prestamo(
	id_Lector int Not Null references Estudiante,
	id_Libro	int Not Null references Libro,
	fecha_prestamo	date Not Null,
	devuelto bit,
	fecha_Devolucion date,
	valor_multa int
	primary key(fecha_prestamo,id_Lector,id_Libro)
);

