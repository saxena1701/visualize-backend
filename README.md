# Project Title

Movement Logistics Visualizer
(This is the repository containing the source code for the backend. For the frontend, the source code can be found here: github.com/saxena1701/visualize-frontend)

## Description
This application visualizes the spatial movement logistics across the map. It allows loading of the data from the CSV files placed in the directory - movement.csv and population.csv. The application also allows the addition of data through the web interface. 
To import data via new files, ensure that the files are in a similar format as the ones given in the repository and replace them in the project directory.

# Technology Stack

The project uses React (TypeScript) for the front end, Flask(Python) as the backend, and PostgreSQL as the database.
The application is containerized on Docker for easy environment replication and deployment.
For map visualizations, the React Leaflet library is used.

The deployment uses a Docker Image for the backend and PostgreSQL and Redis services running on Render. Frontend for the application is deployed on Vercel.
 

### Installing

Make sure you have docker installed in the system. Ensure the Docker application is running and you're in the project directory before you run the command.
This single command will build the images and containers required for the application to run. 

```
docker-compose up --build
```

### Executing program
The application can be accessed by typing the following web address in the browser : 

```
http://localhost:3000
```

* Register as a new user, you will be redirected to the login page.
* Login using the credentials.
* The movements can be visualized on the "Visualize Movements" tab.
* The details of inventories and recorded movements can be seen on the "Inventories" and "Movements" tab.
* The pages also allow adding data using "Add a new Inventory" and "Add a new movement".
* Any new movement data will automatically show up on the map and the Inventory data will be updated automatically.
* You can click over the circular marks on the map, and details of the corresponding movement will pop up. 


## Help
Check the docker application if you encounter any issues in running the application.
If the backend does not start via the docker-compose script, just restart the container again through docker, or retype the docker-compose command in the terminal again.

## Authors

Contributors names and contact info

Akshat Saxena

asaxen24@ncsu.edu




