# PAT Mafate – Mercuriales PDF Automation

> 🇫🇷 Automatisation de la collecte et du traitement des Mercuriales PDF de la DAAF de La Réunion.

> 🇬🇧 Automation of DAAF (Réunion Island) PDF market reports collection and processing.

---

# 🇫🇷 Présentation

Ce projet automatise bi-mensuellement l'ensemble du traitement des **Mercuriales** publiées par la **DAAF de La Réunion**.

L'objectif est de supprimer les manipulations manuelles nécessaires pour récupérer les fichiers PDF, extraire les prix des produits alimentaires, appliquer les règles métier du **PAT Mafate**, puis générer un fichier Excel directement exploitable.

Le workflow est entièrement automatisé grâce à **n8n Cloud**, un **webservice Python** déployé sur **Render**.

---

## Fonctionnalités

* Recherche automatique des nouvelles Mercuriales
* Téléchargement des PDF
* Extraction des données tabulaires
* Nettoyage et structuration des données
* Calcul automatique des prix spécifiques à Mafate (+30 %)
* Génération d'un fichier Excel multi-feuilles
* Exposition via une API REST déployée via Render
* Orchestration complète avec n8n Cloud

---

## Architecture

```text
DAAF Website (https://daaf.reunion.agriculture.gouv.fr)
      │
      ▼
Recherche automatique des PDF
      │
      ▼
Téléchargement PDF (+ récents) GMS + Forains
      │
      ▼
n8n Cloud
      │
      ▼
Webservice Python
      │
      ├── Lecture PDF
      ├── Extraction des tableaux
      ├── Nettoyage
      ├── Transformation
      └── Calcul Mafate
      │
      ▼
Excel (.xlsx)
```

---

## Technologies utilisées

* Python
* pdfplumber
* pandas
* openpyxl
* n8n Cloud
* Render
* REST API via FastAPI

---

## Structure du projet

```text
.
├── app.py
├── mercuriales.py
├── requirements.txt
└── README.md
```

---

## Résultat

Le projet génère automatiquement un fichier Excel contenant :

* Marchés Forains
* Grandes et Moyennes Surfaces (GMS)
* Prix moyens
* Prix spécifiques Mafate (+30 %)

![mercuriales_20260609.xlsx](mercuriales_20260609.xlsx)

---

## Cas d'utilisation

Cette solution est destinée à automatiser bi-mensuellement la production des données de prix des **denrées-fruits et légumes- commercialisés en GSM et sur les marchés forains** dans le cadre du **Projet Alimentaire Territorial (PAT) de Mafate**. 

L'objectif étant d'avoir constamment une actualisation des prix des fruits et légumes sur les marchés réunionnais avec  l'intégration d'une marge propre au territoire de Mafate. 

Ces données permettent d'être au fait des prix des marchés lors des transactions entre les producteurs de Mafate et les gîteurs, services de la restauration scolaire ou tout autre évènement impliquant un achat de denrées locale sur Mafate. 
Ces données sont des éléments clefs pour les **objectifs structurels** du PAT de Mafate.


---

## Présentation du Plan Alimentaire Territorial (PAT) de Mafate 

En 2019, le **Projet Alimentaire Territorial « Planté pou Manzé »** a été sélectionné dans le cadre de l'appel à projets du Plan National pour l'Alimentation (ministère de l'Agriculture). C'est le premier PAT de La Réunion et des territoires d'Outre-mer. Il a été reconnu PAT de niveau 1 en février 2021. Le PAT de Mafate a pour vocation de faire de l'agriculture et de l'alimentation locales des leviers de développement du cirque, tout en sensibilisant habitants et visiteurs aux enjeux de durabilité des systèmes alimentaires — dans l'objectif plus large de faire de Mafate un **« éco-territoire »**.

Depuis 2024 le PAT de Mafate est porté par **l'Association PAT Mafate** qui regroupe les trois structures institutionnelles agissant sur les sujets de l'Alimentation et de l'Agriculture au sein du cirque : 

* Parc National de la Réunion
* Commune de Saint-Paul 
* Commune de la Possession


### Objectifs structurels du PAT :

**1. Renforcer l'autonomie alimentaire du territoire (socle productif)** 
* professionnalisation et installation de producteurs
* diversification agroécologique
* structuration d'un site de transformation locale.

**2. Ancrer l'alimentation locale dans les cantines et les gîtes (socle de commercialisation et de valorisation culinaire)**
* liens producteurs/restauration scolaire et gîtes
* amélioration des jardins pédagogiques
* valorisation de la cuisine créole saine.

**3. Garantir un accès équitable à une alimentation saine (socle de santé publique et justice sociale)**
* lutte contre la précarité alimentaire
* prévention du diabète et de l'obésité
* accompagnement vers de meilleures habitudes alimentaires


---

# 🇬🇧 Overview

This project automates bi-monthly the processing of the monthly **Market Reports (Mercuriales)** published by the **DAAF of Réunion Island**.

Its purpose is to eliminate manual work by automatically downloading PDF reports, extracting product prices, applying the business rules defined for the **PAT Mafate** program, and generating a ready-to-use Excel workbook.

The entire workflow is orchestrated using **n8n Cloud** a dedicated **Python web service** deployed on **Render**.

---

## Features

* Automatic detection of newly published reports
* PDF download (GMS + Forains)
* Table extraction
* Data cleaning and normalization
* Automatic Mafate price calculation (+30%)
* Multi-sheet Excel generation
* REST API endpoint
* Fully automated workflow with n8n Cloud


---

## Architecture

```text
DAAF Website (https://daaf.reunion.agriculture.gouv.fr)
      │
      ▼
PDF Detection (most recents) GMS + Forains
      │
      ▼
Download
      │
      ▼
n8n Cloud
      │
      ▼
Python Web Service
      │
      ├── PDF Parsing
      ├── Table Extraction
      ├── Data Cleaning
      ├── Transformation
      └── Mafate Price Calculation
      │
      ▼
Excel Workbook
```

---

## Technologies

* Python
* pdfplumber
* pandas
* openpyxl
* n8n Cloud
* REST API - FastAPI

---

## Project Structure

```text
.
├── app.py
├── mercuriales.py
├── requirements.txt
└── README.md
```

---

## Output

The application automatically generates an Excel workbook containing:

* Open-air Markets (Forains)
* Supermarkets (GMS)
* Average Prices
* Mafate Prices (+30%)

![mercuriales_20260609.xlsx](mercuriales_20260609.xlsx)

---

## Business Context

This solution is designed to automate bi-monthly the production of **fruit and vegetable price data** collected from **supermarkets (GMS)** and **open-air markets (forains)** as part of the **Mafate Territorial Food Project (PAT Mafate)**.

Its objective is to maintain an up-to-date view of fruit and vegetable prices across Réunion Island while automatically applying the pricing margin specific to the Mafate territory. This provides reliable reference prices for transactions between Mafate's local producers and stakeholders such as mountain lodges (gîtes), school catering services, and any other initiatives involving the purchase of locally produced food within Mafate.

These data play a key role in supporting **Strategic Objectives** of the PAT Mafate by strengthening local food self-sufficiency and promoting the integration of locally produced food into the territory's food supply chain.


---

## About the PAT (Plan Alimentaire Territorial) Mafate Initiative

In 2019, the **"Planté pou Manzé" Territorial Food Project (Projet Alimentaire Territorial – PAT)** was selected under the **French National Food Program (Programme National pour l'Alimentation)** launched by the Ministry of Agriculture. It became the first Territorial Food Project established in **Réunion Island** and across the French Overseas Territories. In February 2021, it was officially recognized as a **Level 1 Territorial Food Project**.

The mission of the **PAT Mafate** is to make local agriculture and food production key drivers of sustainable development within the Mafate cirque, while raising awareness among both residents and visitors about the challenges of sustainable food systems. Its broader ambition is to help transform Mafate into an **eco-territory**.

Since 2024, the PAT Mafate has been managed by the **PAT Mafate Association**, which brings together the three public institutions responsible for food and agricultural development within the Mafate region:

* Réunion National Park
* The Municipality of Saint-Paul
* The Municipality of La Possession

### Strategic Objectives 

The PAT Mafate focuses on three strategic priorities for the coming years:

**1. Strengthen the territory's food self-sufficiency**

* Support the professionalization of local farmers
* Encourage the establishment of new agricultural producers
* Promote agroecological diversification
* Develop local food processing facilities

**2. Integrate local food into schools and tourism**

* Strengthen partnerships between local producers, school cafeterias, and mountain lodges (gîtes)
* Improve educational gardens
* Promote healthy Creole cuisine and local culinary heritage

**3. Ensure equitable access to healthy food**

* Combat food insecurity
* Prevent diabetes and obesity through nutrition initiatives
* Support healthier eating habits for all residents



## 👤 Author

Built by Matthieu Colliaux

[🔗 LinkedIn](https://www.linkedin.com/in/matthieu-colliaux/)

---

Thank you for visiting 🙂
