function isPasswordValid(s, length = 8, charlength = 1, numlength = 1, listspechar = "[^\\w\\s]*[\\W\\S]", userRegex = "") {
    if (s.length < length) {
        return false;
    }
    if (!RegExp("^(?=(?:[^a-zA-Z]*[a-zA-Z]){" + charlength + ",}).*$").test(s)) {
        return false;
    }
    if (!RegExp("^(?:\\D*\\d){" + numlength + "}\\D*$").test(s)) {
        return false;
    }
    if (!RegExp("^(?:[^\\w\\s]*[\\W\\S])[^\\w\\s]*$").test(s)) {
        return false;
    }
    if ((userRegex == "")? false: !userRegex.test(s)) {
        return false;
    }
    return true;
}

module.exports = isPasswordValid;

