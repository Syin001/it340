const database = require('./database')

function retrievePatientList() {
    return database.patientList;
}

function retrievePatient(id) {
    let patient=database.patients.find((patient)=> patient.id === id)
    if (patient!=null){
        const {lastName,firstName,...patientres}= patient;
        patientres.name = lastName + " " + firstName;
        return patientres
    }
    
    throw Error("Invalid id");
}

module.exports = { retrievePatientList, retrievePatient }