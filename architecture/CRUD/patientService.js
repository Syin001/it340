const patientDAO = require('./patientDAO')
const Patient = require('./patient')

function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    patientDAO.insertPatient(patient)
}

function getPatientList() {
    return patientDAO.retrievePatientList()
}

function getPatient(id) {
    try {
        return patientDAO.retrievePatient(id);
    } catch (error) {
        console.log(error);
    }
    
}

function savePatient(id, lastName, firstName) {
    const patients = getPatientList()
    patients.forEach(patient => {
        if (patient.id == id) {
            patient.lastName = lastName
            patient.firstName = firstName
            patientDAO.updatePatient(patient)
        }
    });
}

module.exports = { addPatient, getPatientList, savePatient, getPatient }