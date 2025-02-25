import sqlite3

class Database:
    def __init__(self, db_name="transport.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Crée les tables si elles n'existent pas déjà."""
        self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS Chauffeurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                telephone TEXT NOT NULL UNIQUE,
                permis TEXT NOT NULL UNIQUE,
                statut TEXT CHECK(statut IN ('actif', 'inactif')) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Vehicules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                immatriculation TEXT NOT NULL UNIQUE,
                marque TEXT NOT NULL,
                modele TEXT NOT NULL,
                capacite INTEGER NOT NULL,
                statut TEXT CHECK(statut IN ('disponible', 'en service')) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Trajets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                depart TEXT NOT NULL,
                destination TEXT NOT NULL,
                heure_depart TEXT NOT NULL,
                duree INTEGER NOT NULL,
                vehicule_id INTEGER NOT NULL,
                chauffeur_id INTEGER NOT NULL,
                FOREIGN KEY (vehicule_id) REFERENCES Vehicules(id),
                FOREIGN KEY (chauffeur_id) REFERENCES Chauffeurs(id)
            );

            CREATE TABLE IF NOT EXISTS Reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                trajet_id INTEGER NOT NULL,
                client_nom TEXT NOT NULL,
                client_contact TEXT NOT NULL,
                places INTEGER NOT NULL,
                statut TEXT CHECK(statut IN ('confirmée', 'annulée')) NOT NULL,
                FOREIGN KEY (trajet_id) REFERENCES Trajets(id)
            );
        """)
        self.conn.commit()



# Gestion des chauffeurs 

    def ajouter_chauffeur(self, nom, prenom, telephone, permis, statut="actif"):
        """Ajoute un nouveau chauffeur."""
        self.cursor.execute("""
            INSERT INTO Chauffeurs (nom, prenom, telephone, permis, statut) 
            VALUES (?, ?, ?, ?, ?)""",
            (nom, prenom, telephone, permis, statut))
        self.conn.commit()

    def obtenir_chauffeurs(self):
        """Récupère tous les chauffeurs."""
        self.cursor.execute("SELECT * FROM Chauffeurs")
        return self.cursor.fetchall()

    def modifier_chauffeur(self, chauffeur_id, nom, prenom, telephone, permis, statut):
        """Modifie un chauffeur existant."""
        self.cursor.execute("""
            UPDATE Chauffeurs 
            SET nom = ?, prenom = ?, telephone = ?, permis = ?, statut = ? 
            WHERE id = ?""",
            (nom, prenom, telephone, permis, statut, chauffeur_id))
        self.conn.commit()

    def supprimer_chauffeur(self, chauffeur_id):
        """Supprime un chauffeur."""
        self.cursor.execute("DELETE FROM Chauffeurs WHERE id = ?", (chauffeur_id,))
        self.conn.commit()




# Gestion des Véhicules 


    def ajouter_vehicule(self, immatriculation, marque, modele, capacite, statut="disponible"):
        """Ajoute un véhicule."""
        self.cursor.execute("""
            INSERT INTO Vehicules (immatriculation, marque, modele, capacite, statut) 
            VALUES (?, ?, ?, ?, ?)""",
            (immatriculation, marque, modele, capacite, statut))
        self.conn.commit()

    def obtenir_vehicules(self):
        """Récupère tous les véhicules."""
        self.cursor.execute("SELECT * FROM Vehicules")
        return self.cursor.fetchall()

    def modifier_vehicule(self, vehicule_id, immatriculation, marque, modele, capacite, statut):
        """Modifie un véhicule existant."""
        self.cursor.execute("""
            UPDATE Vehicules 
            SET immatriculation = ?, marque = ?, modele = ?, capacite = ?, statut = ? 
            WHERE id = ?""",
            (immatriculation, marque, modele, capacite, statut, vehicule_id))
        self.conn.commit()

    def supprimer_vehicule(self, vehicule_id):
        """Supprime un véhicule."""
        self.cursor.execute("DELETE FROM Vehicules WHERE id = ?", (vehicule_id,))
        self.conn.commit()

# gestions des trajets 

    def ajouter_trajet(self, depart, destination, heure_depart, duree, vehicule_id, chauffeur_id):
        """Ajoute un trajet."""
        self.cursor.execute("""
            INSERT INTO Trajets (depart, destination, heure_depart, duree, vehicule_id, chauffeur_id) 
            VALUES (?, ?, ?, ?, ?, ?)""",
            (depart, destination, heure_depart, duree, vehicule_id, chauffeur_id))
        self.conn.commit()

    def obtenir_trajets(self):
        """Récupère tous les trajets."""
        self.cursor.execute("SELECT * FROM Trajets")
        return self.cursor.fetchall()

    def supprimer_trajet(self, trajet_id):
        """Supprime un trajet."""
        self.cursor.execute("DELETE FROM Trajets WHERE id = ?", (trajet_id,))
        self.conn.commit()


# Gestion des réservations
    def ajouter_reservation(self, trajet_id, client_nom, client_contact, places, statut="confirmée"):
        """Ajoute une réservation."""
        self.cursor.execute("""
            INSERT INTO Reservations (trajet_id, client_nom, client_contact, places, statut) 
            VALUES (?, ?, ?, ?, ?)""",
            (trajet_id, client_nom, client_contact, places, statut))
        self.conn.commit()

    def obtenir_reservations(self):
        """Récupère toutes les réservations."""
        self.cursor.execute("SELECT * FROM Reservations")
        return self.cursor.fetchall()

    def annuler_reservation(self, reservation_id):
        """Annule une réservation."""
        self.cursor.execute("""
            UPDATE Reservations 
            SET statut = 'annulée' 
            WHERE id = ?""",
            (reservation_id,))
        self.conn.commit()





# fermeture de la base de données 
    def close(self):
        """Ferme la connexion à la base de données."""
        self.conn.close()
