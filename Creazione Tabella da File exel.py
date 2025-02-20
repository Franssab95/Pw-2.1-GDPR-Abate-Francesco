import sqlite3
import pandas as pd
import subprocess
import sys
import time

# Funzione per installare pacchetti mancanti, utile per test su macchine diverse
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Verifico i moduli necessari per evitare problemi di esecuzione
try:
    import pandas as pd
    import sqlite3
    import openpyxl
except ModuleNotFoundError as e:
    missing_module = str(e).split("'")[1]
    print(f"Modulo mancante: {missing_module}. Lo installo ora...")
    install_package(missing_module)
    # Ripeto l’import per sicurezza dopo l’installazione
    import pandas as pd
    import sqlite3
    import openpyxl

DATABASE_NAME = "database.db"  # Nome del database, scelto per semplicità
EXCEL_FILE = "utenti.xlsx"

def create_database():
    """Creo la tabella utenti con vincoli per garantire integrità dei dati"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Struttura della tabella con campi obbligatori e un timestamp per tracciare
    cursor.execute('''CREATE TABLE IF NOT EXISTS utenti (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cognome TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        telefono TEXT NOT NULL,
                        data_registrazione TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    conn.commit()
    conn.close()
    print("Tabella utenti creata correttamente nel database.")

def import_data_from_excel():
    """Importo i dati da Excel in modo più rapido con executemany"""
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        # Carico il file Excel generato in precedenza
        df = pd.read_excel(EXCEL_FILE)

        # Controllo che le colonne corrispondano a quelle attese
        expected_columns = {"Nome", "Cognome", "Email", "Telefono"}
        file_columns = set(df.columns)
        if file_columns != expected_columns:
            raise ValueError(f"Errore nelle colonne: attese {expected_columns}, trovate {file_columns}")

        # Misuro il tempo per verificare il miglioramento richiesto
        start_time = time.time()

        # Preparo i dati in una lista di tuple per l’inserimento multiplo
        data_to_insert = []
        for _, row in df.iterrows():
            data_to_insert.append((row["Nome"], row["Cognome"], row["Email"], row["Telefono"]))

        # Uso executemany per velocizzare, meglio dei singoli INSERT
        cursor.executemany('''INSERT OR IGNORE INTO utenti (nome, cognome, email, telefono) 
                              VALUES (?, ?, ?, ?)''', data_to_insert)

        conn.commit()

        # Calcolo il tempo impiegato per confrontarlo con il target del 20%
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Dati importati in {elapsed_time:.3f} secondi: {len(data_to_insert)} record trasferiti.")

    except Exception as e:
        print(f"Errore nell’importazione: {e}. Da controllare!")

    finally:
        conn.close()  # Chiudo la connessione per liberare risorse

if __name__ == "__main__":
    create_database()
    import_data_from_excel()