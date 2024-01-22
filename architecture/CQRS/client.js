const patientCommand = require('./patientCommand')
const patientQuery = require('./patientQuery')

patientCommand.addPatient('toto', 'titi')
patientCommand.addPatient('Daniel', 'tutu')

console.log('patientList:');
console.log(patientQuery.getPatientListList());

patientCommand.savePatient(0, 'toto2', 'titi2')

console.log('patientList:');
console.log(patientQuery.getPatientListList())

console.log('patients[0]:');
console.log(patientQuery.getPatient(0));

console.log('patientCache:');
console.log(patientQuery.getPatientCache());