# ldap-scan

Le script ldap-anonymous-vuln-scan.py est un outil utilisé pour vérifier si un serveur LDAP (Lightweight Directory Access Protocol) permet une connexion anonyme et si cette connexion donne accès à des informations sensibles ou non restreintes.

## Description

**`ldap-anonymous-vuln-scan.py`** est un script Python conçu pour identifier si un serveur LDAP (Lightweight Directory Access Protocol) autorise une connexion **anonyme** et si cette connexion permet d’accéder à des **informations sensibles** ou **non protégées**.

Ce type de vulnérabilité peut exposer des informations critiques (utilisateurs, groupes, structures d'annuaire...) et constitue une porte d'entrée pour des attaques plus ciblées.



## 🚀 Installation

Avant d'exécuter le script, installez la dépendance nécessaire :

```bash

pip install ldap3
python ldap-anonymous-vuln.py


## ⚠️ Clause de non-responsabilité

Ce script est fourni **à des fins éducatives et de test de sécurité autorisé uniquement**.  
L’auteur décline **toute responsabilité** en cas d’utilisation **abusive**, **illégale** ou **non autorisée**.

> ⚠️ **N'utilisez cet outil que sur des systèmes dont vous possédez l'autorisation explicite.**  
> Toute utilisation sur des infrastructures tierces sans consentement préalable est **illégale** et **strictement interdite**.
