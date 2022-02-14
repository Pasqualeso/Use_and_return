# Use_and_return
Back_end progetto Tecnologie Web svolto da Pasquale Sorrentino, Eduardo Autore e Sara Terlizzi.

Per eseguire il progetto eseguire i passaggi:

Spostarsi nella cartella "use_and_return" e creare un virtual environment per Python :

python3 -m venv venv

Una volta attivato il virtual environment, istallare le liberire richieste:

pip install wheel

pip install -r requirements.txt

Spostarsi nella cartella Flask e partire il web-server

flask run --host 0.0.0.0

Cosi il webserver parte in modo tale da essere raggiugibile su tutta la rete locale, per farlo partire solo sul localhost 
flask run


Istruzioni database:
Nella cartella "Database" sono presenti i file per la creazione delle tabelle del database in linguaggio SQL.
Abbiamo utilizzato Mysql:

https://dev.mysql.com/downloads/workbench/
https://dev.mysql.com/downloads/mysql/

Eseguire lo script CREA_DB_NOLEGGIO_OGGETTI.sql per creare tutte le tabelle e per inizializzare le due tuple con i ruoli User e Administrator.
