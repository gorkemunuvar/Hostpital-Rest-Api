# Hospital Rest Api

This projest was intented to deliver as a freelance project but has been canceled by the client. Now, source code is here.

## About

It is a Rest API to handle business logic for the [**Hospital Mobile App**](https://github.com/gorkemunuvar/Hospital-Mobile/tree/main)

### Main Features

 - See the hospital news.
 - Search polyclinics.
 - Search doctors.
 - Take/cancel/see appointments.
 - Multi language support.
 - See hospital locations.

## Tech

During the development, there was and Oracle Database storing all needed data. That's why app communicates with a rest api written in Flask.

App <--> Rest Api <--> Oracle DB

You can reach the mobile app [here](https://github.com/gorkemunuvar/Hospital-Mobile/tree/main). 

In addition to MVC there is a Service layer added to handle database queries. (MVC+S)
Apart from that cx-oracle is used to communicate with Oracle DB.

SQL queries were given by my client.
