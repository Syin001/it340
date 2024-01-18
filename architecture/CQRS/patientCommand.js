const patientCommandDAO = require('./patientCommandDAO')
const patientQuery = require('./patientQuery')
const Patient = require('./patient')

function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    patientCommandDAO.insertPatient(patient)
    patientCommandDAO.insertPatientList(patient)
}

function savePatient(id, lastName, firstName) {
    const patients = patientQuery.getPatientList()
    patients.forEach(patient => {
        if (patient.id == id) {
            patient.lastName = lastName
            patient.firstName = firstName
            patientCommandDAO.updatePatientList(patient)
            patientCommandDAO.updatePatient(patient)
        }
    });
}

module.exports = { addPatient, savePatient }