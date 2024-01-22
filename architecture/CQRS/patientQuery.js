const patientQueryDAO = require('./patientQueryDAO')

function getPatientListList() {
    return patientQueryDAO.retrievePatientListList()
}

function getPatientList() {
    return patientQueryDAO.retrievePatientList()
}

function getPatientCache() {
    return patientQueryDAO.retrievePatientCache()
}

function getPatient(id) {
    try {
        return patientQueryDAO.retrievePatient(id);
    } catch (error) {
        console.log(error);
    }
    
}

module.exports = { getPatientListList, getPatientCache, getPatientList, getPatient }