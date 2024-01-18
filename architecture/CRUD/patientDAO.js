const database = require('./database')

function insertPatient(patient) {
    database.patients.push(patient)
}

function retrievePatientList() {
    return database.patients.map(({creationDate, ...patient}) => patient);
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

function updatePatient(patient) {
    let i = 0
    database.patients.forEach(patientData => {
        if (patientData.id == patient.id) {
            patient.creationDate = database.patients[i].creationDate;
            database.patients[i] = patient
        }
        i++
    });
}

module.exports = { insertPatient, retrievePatientList, updatePatient, retrievePatient }