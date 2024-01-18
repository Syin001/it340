const patientService= require('./patientService')

patientService.addPatient('toto', 'titi')
patientService.addPatient('Daniel', 'tutu')

console.log(patientService.getPatientList())

patientService.savePatient(0, 'toto2', 'titi2')

console.log(patientService.getPatientList())

console.log(patientService.getPatient(0));