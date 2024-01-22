eventStore = []

function addEvent(patientEvent) {
    eventStore.push(patientEvent);
}

function restorePatient(id) {
    let patient = {};
    eventStore.forEach(p => {
        if (p.patientId === id) {
            for (let key in p.payload) {
                if (Object.hasOwnProperty.call(p.payload, key)) {
                    patient[key] = p.payload[key]
                }
            }
        }
    });
    return patient;
}

module.exports = { addEvent, restorePatient }