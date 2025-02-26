import sqlite3

# Connexion à la base de données (ou création si elle n'existe pas)
conn = sqlite3.connect('transport.db')

# Création du curseur
cur = conn.cursor()

# -----------------------------Création des tables-----------------------

# Table Etudiants
cur.execute("""
        CREATE TABLE IF NOT EXISTS Chauffeurs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            telephone TEXT NOT NULL UNIQUE,
            permis TEXT NOT NULL UNIQUE,
            statut TEXT CHECK(statut IN ('actif', 'inactif')) NOT NULL
        )""")


cur.execute("""   CREATE TABLE IF NOT EXISTS Vehicules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            immatriculation TEXT NOT NULL UNIQUE,
            marque TEXT NOT NULL,
            modele TEXT NOT NULL,
            capacite INTEGER NOT NULL,
            statut TEXT CHECK(statut IN ('disponible', 'en service')) NOT NULL
        )""")

cur.execute (""" CREATE TABLE IF NOT EXISTS Trajets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            depart TEXT NOT NULL,
            destination TEXT NOT NULL,
            heure_depart TEXT NOT NULL,
            duree INTEGER NOT NULL,
            vehicule_id INTEGER NOT NULL,
            chauffeur_id INTEGER NOT NULL,
            FOREIGN KEY (vehicule_id) REFERENCES Vehicules(id),
            FOREIGN KEY (chauffeur_id) REFERENCES Chauffeurs(id)
        )""")

cur.execute ("""CREATE TABLE IF NOT EXISTS Reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trajet_id INTEGER NOT NULL,
            client_nom TEXT NOT NULL,
            client_contact TEXT NOT NULL,
            places INTEGER NOT NULL,
            statut TEXT CHECK(statut IN ('confirmée', 'annulée')) NOT NULL,
            FOREIGN KEY (trajet_id) REFERENCES Trajets(id)
        )    """)
conn.commit()


# Gestion des chauffeurs 

def ajouter_chauffeur(nom, prenom, telephone, permis, statut="actif"):
    """Ajoute un nouveau chauffeur."""
    cur.execute("""
        INSERT INTO Chauffeurs (nom, prenom, telephone, permis, statut) 
        VALUES (?, ?, ?, ?, ?)""",
        (nom, prenom, telephone, permis, statut))
    conn.commit()

def obtenir_chauffeurs():
    """Récupère tous les chauffeurs."""
    cur.execute("SELECT * FROM Chauffeurs")
    return cur.fetchall()

def modifier_chauffeur(self, chauffeur_id, nom, prenom, telephone, permis, statut):
    """Modifie un chauffeur existant."""
    cur.execute("""
        UPDATE Chauffeurs 
        SET nom = ?, prenom = ?, telephone = ?, permis = ?, statut = ? 
        WHERE id = ?""",
        (nom, prenom, telephone, permis, statut, chauffeur_id))
    conn.commit()

def supprimer_chauffeur(self, chauffeur_id):
    """Supprime un chauffeur."""
    self.cursor.execute("DELETE FROM Chauffeurs WHERE id = ?", (chauffeur_id,))
    self.conn.commit()




# Gestion des Véhicules 


    def ajouter_vehicule(immatriculation, marque, modele, capacite, statut="disponible"):
        """Ajoute un véhicule."""
        cur.execute("""
            INSERT INTO Vehicules (immatriculation, marque, modele, capacite, statut) 
            VALUES (?, ?, ?, ?, ?)""",
            (immatriculation, marque, modele, capacite, statut))
        conn.commit()

    def obtenir_vehicules():
        """Récupère tous les véhicules."""
        cur.execute("SELECT * FROM Vehicules")
        return cur.fetchall()

    def modifier_vehicule(vehicule_id, immatriculation, marque, modele, capacite, statut):
        """Modifie un véhicule existant."""
        cur.execute("""
            UPDATE Vehicules 
            SET immatriculation = ?, marque = ?, modele = ?, capacite = ?, statut = ? 
            WHERE id = ?""",
            (immatriculation, marque, modele, capacite, statut, vehicule_id))
        conn.commit()

    def supprimer_vehicule(vehicule_id):
        """Supprime un véhicule."""
        cur.execute("DELETE FROM Vehicules WHERE id = ?", (vehicule_id,))
        conn.commit()

# gestions des trajets 

    def ajouter_trajet(depart, destination, heure_depart, duree, vehicule_id, chauffeur_id):
        """Ajoute un trajet."""
        cur.execute("""
            INSERT INTO Trajets (depart, destination, heure_depart, duree, vehicule_id, chauffeur_id) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (depart, destination, heure_depart, duree, vehicule_id, chauffeur_id))
        conn.commit()

    def obtenir_trajets():
        """Récupère tous les trajets."""
        cur.execute("SELECT * FROM Trajets")
        return self.cursor.fetchall()

    def supprimer_trajet(self, trajet_id):
        """Supprime un trajet."""
        cur.execute("DELETE FROM Trajets WHERE id = ?", (trajet_id,))
        conn.commit()


# Gestion des réservations
    def ajouter_reservation(trajet_id, client_nom, client_contact, places, statut="confirmée"):
        """Ajoute une réservation."""
        cur.execute("""
            INSERT INTO Reservations (trajet_id, client_nom, client_contact, places, statut) 
            VALUES (?, ?, ?, ?, ?)""",
            (trajet_id, client_nom, client_contact, places, statut))
        conn.commit()

    def obtenir_reservations():
        """Récupère toutes les réservations."""
        cur.execute("SELECT * FROM Reservations")
        return cur.fetchall()

    def annuler_reservation(reservation_id):
        """Annule une réservation."""
        self.cursor.execute("""
            UPDATE Reservations 
            SET statut = 'annulée' 
            WHERE id = ?""",
            (reservation_id,))
        conn.commit()





# fermeture de la base de données 
    def close(self):
        """Ferme la connexion à la base de données."""
        self.conn.close()
