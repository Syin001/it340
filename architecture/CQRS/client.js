const patientCommand = require('./patientCommand')
const patientQuery = require('./patientQuery')

patientCommand.addPatient('toto', 'titi')
patientCommand.addPatient('Daniel', 'tutu')

console.log(patientQuery.getPatientList());

patientCommand.savePatient(0, 'toto2', 'titi2')

console.log(patientQuery.getPatientList())

console.log(patientQuery.getPatient(0));