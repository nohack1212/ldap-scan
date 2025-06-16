pip3 install ldap3

from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPSocketOpenError, LDAPException


LDAP_HOST = 'example.com'
LDAP_PORT = 389
USE_SSL = False
BASE_DN = 'dc=remplace,dc=com'  

# --- Définir un filtre LDAP avancé ---
# Par exemple, rechercher tous les objets utilisateurs (person) avec un attribut donné
LDAP_FILTER = '(objectClass=person)'  # Tu peux aussi tester: (cn=*), (uid=*), (sn=*)...

# --- Liste des attributs à récupérer ---
ATTRIBUTES = ['cn', 'sn', 'mail', 'uid', 'givenName']

try:
   
    server = Server(LDAP_HOST, port=LDAP_PORT, use_ssl=USE_SSL, get_info=ALL)
    conn = Connection(server, auto_bind=True)
    print("[✔] Connexion réussie")

  
    success = conn.search(
        search_base=BASE_DN,
        search_filter=LDAP_FILTER,
        search_scope=SUBTREE,
        attributes=ATTRIBUTES
    )

    if success and conn.entries:
        print(f"[ℹ️] {len(conn.entries)} résultats trouvés :")
        for entry in conn.entries:
            print("=" * 40)
            print(entry.entry_dn)
            for attr in ATTRIBUTES:
                value = entry[attr].value if attr in entry else None
                print(f"{attr}: {value}")
    else:
        print("[❗] Aucune entrée trouvée ou filtre invalide.")

    conn.unbind()

except LDAPSocketOpenError as e:
    print(f"[✘] Erreur de connexion : {e}")
except LDAPException as e:
    print(f"[✘] Erreur LDAP : {e}")
except Exception as e:
    print(f"[✘] Erreur générale : {e}")
