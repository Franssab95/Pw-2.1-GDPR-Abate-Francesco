# Pw-2.1-GDPR-Abate-Francesco
Codici per pw 2.1 Abate Francesco 
1.	Questo repository contiene due script Python per un project work sul GDPR:
2.	Generazione file exel.py Genera dati casuali per 10 utenti e li salva in un file Excel.
3.	Creazione Tabella da File exel.pyL egge i dati dall’Excel e li importa in una tabella SQLite.
4.	Lo sviluppo è iniziato configurando l’ambiente con le librerie richieste. Per il primo script, ho generato dati casuali per 10 utenti, ma ho notato che alcuni numeri di telefono generati da Faker erano troppo corti o lunghi. Così ho aggiunto validate_phone, testandola con un paio di esecuzioni per assicurarmi che funzionasse: rigenerare i numeri finché non rientravano nell’intervallo mi è sembrata una soluzione pratica. L’esportazione in Excel è stata fluida dopo aver rimosso gli indici. Per il secondo script, ho definito la tabella SQLite con vincoli, aggiungendo data_registrazione per tracciare gli inserimenti. La sfida è stata gestire la corrispondenza tra Excel e SQL: il controllo delle colonne mi ha salvato da errori iniziali, e ho gestito i duplicati email dopo aver visto che potevano capitare. 
