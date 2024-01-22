const database = require('./database')
const databasecache = require('./cache')

function retrievePatientListList() {
    return database.patientList;
}

function retrievePatientList() {
    return database.patients;
}

function retrievePatientCache() {
    return databasecache.patients;
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

module.exports = { retrievePatientListList, retrievePatientCache, retrievePatientList, retrievePatient }