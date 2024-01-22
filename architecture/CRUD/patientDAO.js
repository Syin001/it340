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
            database.patients[i].firstName = patient.firstName;
            database.patients[i].lastName = patient.lastName;
        }
        i++
    });
}

module.exports = { insertPatient, retrievePatientList, updatePatient, retrievePatient }