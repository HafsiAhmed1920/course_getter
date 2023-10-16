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