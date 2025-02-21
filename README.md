# Pw-2.1-GDPR-Abate-Francesco

## Descrizione
Questo repository contiene due script Python sviluppati per gestire dati personali in conformità al GDPR:
1. `Generazione file exel.py`: Genera dati fittizi (nome, cognome, email, telefono) per 10 utenti e li salva in `utenti.xlsx`.
2. `Creazione Tabella da File exel.py`: Importa i dati da `utenti.xlsx` in un database SQLite (`database.db`).

## Installazione
1. Assicurati di avere Python 3.x installato.
2. Clona il repository: `git clone https://github.com/Franssab95/Pw-2.1-GDPR-Abate-Francesco.git`
3. Gli applicativi hanno già all'interno del codice delle instruzioni per scaricare ed installare le funzioni necessarie al loro funzionamento, così da non dover necessitare di altro se non python installato.

## Uso
1. Genera i dati: `python generate_data.py`
2. Importa i dati in SQL: `python import_to_sql.py`
3. Verifica i risultati in `utenti.xlsx` o nel database `database.db`.
