
from abc import ABC, abstractmethod

class Paiement(ABC):
    def __init__(self, montant):
        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):
    def __init__(self, montant, numero, cvv):
        super().__init__(montant)
        self._numero = numero
        self._cvv = cvv

    def payer(self):
        if len(self._numero) == 16:
            print("Verification carte bancaire OK.")
        return f"Paiement de {self._montant} EUR effectue par Carte Bancaire (Numero: {self._numero[:4]}****)."


class PayPal(Paiement):
    def __init__(self, montant, email, token):
        super().__init__(montant)
        self._email = email
        self._token = token

    def payer(self):
        return f"Paiement de {self._montant} EUR effectue via PayPal (Compte: {self._email})."


class Crypto(Paiement):
    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)
        self._wallet_id = wallet_id
        self._reseau = reseau

    def payer(self):
        return f"Paiement de {self._montant} EUR effectue en Crypto {self._reseau} (Wallet: {self._wallet_id})."


def traiter_paiements(liste_paiements):
    print("Debut de traitement des paiements")
    for p in liste_paiements:
        confirmation = p.payer()
        print(confirmation)
    print("Fin de traitement des paiements")


if __name__ == "__main__":
    cb1 = CarteBancaire(250.0, "1234567812345678", "168")
    cb2 = CarteBancaire(70.5, "9876543298765432", "654")
    
    pp1 = PayPal(80.0, "etudiant.tp@gmail.com", "token_abc123")
    pp2 = PayPal(12.0, "user.test@yahoo.fr", "token_xyz789")
    
    cr1 = Crypto(300.0, "0x1234abcd", "BTC")
    cr2 = Crypto(500.0, "0x5678efgh", "ETH")
    
    mes_paiements = [cb1, pp1, cr1, cb2, pp2, cr2]
    traiter_paiements(mes_paiements)