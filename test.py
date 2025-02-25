from database import Database

db = Database()

# Ajouter un chauffeur
db.ajouter_chauffeur("Kouame", "Jean", "0102030405", "ABC1234")

# Ajouter un véhicule
db.ajouter_vehicule("AB-123-CD", "Toyota", "Coaster", 25)

# Ajouter un trajet
db.ajouter_trajet("Abidjan", "Yamoussoukro", "08:00", 3, 1, 1)

# Ajouter une réservation
db.ajouter_reservation(1, "Doe John", "0708091011", 2)

# Récupérer et afficher toutes les réservations
print(db.obtenir_reservations())

db.close()
