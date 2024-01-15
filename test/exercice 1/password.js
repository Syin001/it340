function isPasswordValid(s, length = 8, charlength = 1, numlength = 1, listspechar = "[^\\w\\s]*[\\W\\S]", userRegex = "") {
    if (s.length < length) {
        console.log('object 0');
        return false;
    }
    if (!RegExp("^(?=(?:[^a-zA-Z]*[a-zA-Z]){" + charlength + ",}).*$").test(s)) {
        console.log('object 01');
        return false;
    }
    if (!RegExp("^(?:\\D*\\d){" + numlength + "}\\D*$").test(s)) {
        console.log('object 111');
        return false;
    }
    if (!RegExp("^(?:[^\\w\\s]*[\\W\\S])[^\\w\\s]*$").test(s)) {
        console.log('object 3');
        return false;
    }
    if ((userRegex == "")? false: !userRegex.test(s)) {
        console.log('object 4');
        return false;
    }
    return true;
}

module.exports = isPasswordValid;

