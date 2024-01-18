const database = require('./database')

function insertPatient(patient) {
    database.patients.push(patient)
}

function insertPatientList(patient) {
    const {creationDate, ...patientNoDate} = patient
    database.patientList.push(patientNoDate)
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

function updatePatientList(patient) {
    let i = 0
    database.patientList.forEach(patientData => {
        if (patientData.id == patient.id) {
            database.patientList[i] = patient
        }
        i++
    });
}

module.exports = {insertPatient, insertPatientList, updatePatient, updatePatientList }