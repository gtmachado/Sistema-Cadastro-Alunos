BEGIN TRANSACTION;
CREATE TABLE Aluno (
                ID_Aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Sobrenome TEXT NOT NULL,
                Matricula TEXT NOT NULL,
                Idade INTEGER,
                Email TEXT NOT NULL
            );
INSERT INTO "Aluno" VALUES(1,'João','Silva','123',20,'joao@email.com');
INSERT INTO "Aluno" VALUES(2,'Maria','Santos','456',25,'maria@email.com');
INSERT INTO "Aluno" VALUES(3,'José','Oliveira','789',30,'jose@email.com');
INSERT INTO "Aluno" VALUES(4,'Ana','Pereira','101',22,'ana@email.com');
INSERT INTO "Aluno" VALUES(5,'Pedro','Lima','202',27,'pedro@email.com');
INSERT INTO "Aluno" VALUES(6,'Clara','Costa','303',35,'clara@email.com');
INSERT INTO "Aluno" VALUES(7,'Fernando','Martins','404',18,'fernando@email.com');
INSERT INTO "Aluno" VALUES(8,'Gabriela','Almeida','505',29,'gabriela@email.com');
INSERT INTO "Aluno" VALUES(9,'Lucas','Melo','606',32,'lucas@email.com');
INSERT INTO "Aluno" VALUES(10,'Camila','Rocha','707',24,'camila@email.com');
INSERT INTO "Aluno" VALUES(11,'Miguel','Rodrigues','808',26,'miguel@email.com');
INSERT INTO "Aluno" VALUES(12,'Amanda','Fernandes','909',31,'amanda@email.com');
INSERT INTO "Aluno" VALUES(13,'Rafael','Lopes','111',23,'rafael@email.com');
INSERT INTO "Aluno" VALUES(14,'Isabela','Carvalho','222',28,'isabela@email.com');
INSERT INTO "Aluno" VALUES(15,'Bruno','Mendes','333',33,'bruno@email.com');
INSERT INTO "Aluno" VALUES(16,'Laura','Nascimento','444',21,'laura@email.com');
INSERT INTO "Aluno" VALUES(17,'Gustavo','Araujo','555',34,'gustavo@email.com');
INSERT INTO "Aluno" VALUES(18,'Carolina','Dias','666',19,'carolina@email.com');
INSERT INTO "Aluno" VALUES(19,'Diego','Correia','777',30,'diego@email.com');
INSERT INTO "Aluno" VALUES(20,'Juliana','Goncalves','888',25,'juliana@email.com');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('Aluno',20);
COMMIT;
