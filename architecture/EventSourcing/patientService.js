const Patient = require('./patient')
const Event = require('./event')
const eventStore = require('./eventStore')

function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    const patientEvent = new Event('patientAdded', patient.id, patient, new Date())
    eventStore.addEvent(patientEvent)
}

function savePatient(id, lastName, firstName) {
    const patient = eventStore.restorePatient(id);
    patient.lastName = lastName;
    patient.firstName = firstName;
    const patientEvent = new Patient('patientSaved', patient.id, patient, new Date());
    eventStore.addEvent(patientEvent);
}

module.exports = { addPatient, savePatient }