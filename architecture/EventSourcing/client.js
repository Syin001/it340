const patientService = require('./patientService');

patientService.addPatient('toto', 'titi');
patientService.addPatient('Daniel', 'Foo');

patientService.savePatient(0, 'toto2', 'titi2');