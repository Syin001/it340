class Event {
    constructor(name, patientId, payload, creationDate) {
        this.name = name
        this.patientId = patientId
        this.paylaoad = payload
        this.creationDate = creationDate
    };
}

module.exports = Event;