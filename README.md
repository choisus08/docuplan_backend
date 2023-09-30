# Doc UPlan- Backend
**Project By:** Susie Gordon


## Descripton
Doc UPlan is a full CRUD app developed with Vue and Django that compiles all doctors appointments (family, dentist, optometrist, specialist, etc.) into a calendar to improve time management, organization, and lifestyle. Users can view a list of various appointments and the calendar month of choice displaying all past and future appointments.  

## Link
- [**Github**](https://github.com/choisus08/docuplan_backend/tree/main)
- [**Deployment**](https://docuplan-backend.onrender.com/appointments/)

## Technologies Used
- Django
- PostgreSQL
- Postman
- Python

## Backend Endpoints

| ENDPOINT | METHOD | PURPOSE |
|----------|--------|---------|
| /appointments | GET | return list of appointment entries|
| /appointments/:id | DELETE | delete a appointment entry from database |
| /appointments/:id | PUT | receive info & update appointment entry in database |
| /appointments | POST | receive info from new form & create new appointment entry in database |
| /appointments/:id | GET | render page with the appointment entry|

## ERD

``` mermaid
erDiagram
    USER {
        id primaryKey
        username string 
        password string
    }
    USER ||--|{ SHIFTS : Create
    SHIFTS {
        name foreignKey
        appointment_title string
        doctor_name string
        doctor_specialist string 
        address string
        date string 
        time string 
        notes string
    }
```
