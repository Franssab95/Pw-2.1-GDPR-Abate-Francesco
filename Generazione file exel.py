import subprocess
import sys

# Funzione per installare moduli, mi serve per non avere errori su altri PC
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Controllo i moduli necessari prima di iniziare
try:
    import pandas as pd
    from faker import Faker
    import openpyxl
except ModuleNotFoundError as e:
    missing_module = str(e).split("'")[1]
    print(f"Modulo mancante: {missing_module}. Lo installo subito...")
    install_package(missing_module)
    # Li importo di nuovo per essere sicuro che funzionino
    import pandas as pd
    from faker import Faker
    import openpyxl

# Inizializzo Faker per generare i dati
fake = Faker()

def validate_phone(phone):
    """Controllo che il numero di telefono sia tra 10 e 15 caratteri"""
    while len(phone) < 10 or len(phone) > 15:
        phone = fake.phone_number()  # Rigenero finché non va bene
    return phone

def generate_data(num_records=10):
    """Genero dati casuali per gli utenti e li salvo in Excel"""
    data = {
        'Nome': [fake.first_name() for _ in range(num_records)],
        'Cognome': [fake.last_name() for _ in range(num_records)],
        'Email': [fake.email() for _ in range(num_records)],
        'Telefono': [validate_phone(fake.phone_number()) for _ in range(num_records)]
    }
    
    # Creo il DataFrame e lo esporto senza indici per pulizia
    df = pd.DataFrame(data)
    df.to_excel("utenti.xlsx", index=False)
    print(f"File Excel creato con {num_records} utenti, numeri di telefono validati!")

if __name__ == "__main__":
    generate_data(10)