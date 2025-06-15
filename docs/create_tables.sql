-- Create Users table first since it's referenced by History
CREATE TABLE Users (
    ID SERIAL PRIMARY KEY,
    Nom VARCHAR(30) NOT NULL
);

-- Create Taches table
CREATE TABLE Taches (
    ID SERIAL PRIMARY KEY,
    Nom VARCHAR(30) NOT NULL,
    Periodicite INTEGER NOT NULL
);

-- Create History table with foreign key references
CREATE TABLE History (
    ID SERIAL PRIMARY KEY,
    done_date DATE NOT NULL,
    user_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(ID),
    FOREIGN KEY (task_id) REFERENCES Taches(ID)
); 