**Project Name:** Courses Getter 

**Stack:** PySpark, Kafka, Docker, Firebase, Selenium 

**Description:** 
This project involves gathering course data from websites, specifically from the Data Flair website so far. The data is processed and labeled into courses.
The gathered data is then stored in a Firebase bucket after handling a Firebase role that provides the required permissions. When a user requests a course, 
Kafka ( running in a docker container ) interacts to gather the data from the bucket (our producer in this case) and displays it in the console (our consumer).
The details about the website and its rating are also provided.

**Next Steps:** 
The current focus is on preparing for certification. The next step might involve setting up a Docker container for the entire project to avoid any version conflicts. 
Setting up the pipeline via Jenkins could also be beneficial for creating an automated application. 
Additionally, adding other data sources (different website formats and file types) could enhance the application and also serve as good practice.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Voici une traduction en français de votre description de projet :

**Nom du projet :** Courses Getter 

**Pile :** PySpark, Kafka, Docker, Firebase, Selenium 

**Description :** 
Ce projet consiste à collecter des données de cours à partir de sites web, notamment du site Data Flair jusqu'à présent. Les données sont traitées et étiquetées en cours.
 Les données collectées sont ensuite stockées dans un seau Firebase après avoir géré un rôle Firebase qui fournit les permissions requises. Lorsqu'un utilisateur demande un cours,
  Kafka (fonctionnant dans un conteneur Docker) interagit pour récupérer les données du seau (notre producteur dans ce cas) et les affiche dans la console (notre consommateur). 
  Les détails sur le site web et sa note sont également fournis.

**Prochaines étapes :** 
L'objectif actuel est de se préparer à la certification. L'étape suivante pourrait consister à mettre en place un conteneur Docker pour l'ensemble du projet afin d'éviter
 tout conflit de version. La mise en place du pipeline via Jenkins pourrait également être bénéfique pour créer une application automatisée. De plus, l'ajout d'autres sources 
 de données (différents formats et types de fichiers de sites web) pourrait améliorer l'application et servir également de bonne pratique.