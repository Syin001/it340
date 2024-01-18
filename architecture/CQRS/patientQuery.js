const patientQueryDAO = require('./patientQueryDAO')

function getPatientList() {
    return patientQueryDAO.retrievePatientList()
}

function getPatient(id) {
    try {
        return patientQueryDAO.retrievePatient(id);
    } catch (error) {
        console.log(error);
    }
    
}

module.exports = { getPatientList, getPatient }