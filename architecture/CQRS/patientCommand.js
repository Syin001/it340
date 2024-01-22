const patientCommandDAO = require('./patientCommandDAO')
const patientQuery = require('./patientQuery')
const Patient = require('./patient')
const patientcache = require('./cache')

function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    patientCommandDAO.insertPatient(patient)
    patientCommandDAO.insertPatientList(patient)
    patientcache.patients.push({id: patient.id, name: patient.lastName + ' ' + patient.firstName})
}

function savePatient(id, lastName, firstName) {
    const patientsList = patientQuery.getPatientListList();
    patientsList.forEach(patient => {
        if (patient.id == id) {
            patient.lastName = lastName
            patient.firstName = firstName
            patientCommandDAO.updatePatientList(patient)
        }
    });
    const patients = patientQuery.getPatientList();
    patients.forEach(patient => {
        if (patient.id == id) {
            patient.lastName = lastName
            patient.firstName = firstName
            patientCommandDAO.updatePatient(patient)
        }
    });
    patientcache.patients.forEach(patient => {
        if (patient.id == id) {
            patient.name = lastName + ' ' + firstName;
        }        
    });
}

module.exports = { addPatient, savePatient }