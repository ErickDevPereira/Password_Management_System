USE Safe_PW;
---------------------------------Creating Tables------------------------------------
--Creating the table Users that will store the register data of the Users.
CREATE TABLE IF NOT EXISTS Users (
    Id_user INT UNSIGNED AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Phone_number VARCHAR(255) NOT NULL,
    CHECK( EMAIL LIKE '_%@%_.com' ),
    PRIMARY KEY (Id_user)
);
CREATE TABLE IF NOT EXISTS PW_Data (
    Id_record INT UNSIGNED AUTO_INCREMENT,
    Platform VARCHAR(255) NOT NULL,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Id_user INT UNSIGNED, /*id from the logged user that is putting data into the table.*/
    UNIQUE ( Platform, Username, Id_user ), /*Can't reapeat username and platform for the same user*/
    FOREIGN KEY (Id_user) REFERENCES Users(Id_user), /*This FK constraint is important to guarantee data consistency.*/
    PRIMARY KEY (Id_record),
    CHECK ( Platform <> "" AND Username <> "" AND Password <> "")
);
----------------------------Showing data from the tables----------------------------
SELECT * FROM Users;
SELECT * FROM PW_data;
----------------------------Deleting the tables(ATENTION!!!)-------------------------
DROP TABLE Users;
DROP TABLE PW_data;
-----------------------------Testing data--------------------------------------------
INSERT INTO Users VALUES (DEFAULT, '1', '1', 'Tchaca@butiaca.com', '12345'),
                        (DEFAULT, '2', '2', 'Tchaca@butiaca.com', '12345');
INSERT INTO PW_data (Platform, Username, Password, Id_user) VALUES ('Steam', 'Paulavado10', 'abx@123', 1),
                                                                    ('Origin', 'cagatronco5000', 'riodejaneiro111', 1),
                                                                    ('Ubisoft', 'KenKenTemTem', 'aranha5000', 1),
                                                                    ('Origin', 'Papintinton', 'regenerator', 2),
                                                                    ('Steam', 'EdwardMonteNegro', 'aaabbbccc', 2);
DELETE FROM Pw_data;
DELETE FROM Users;