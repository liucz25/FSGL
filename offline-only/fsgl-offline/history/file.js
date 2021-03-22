function file() {

    this.read = function() {
        const fs = require('fs');

        let rawdata = fs.readFileSync('student.json');
        let student = JSON.parse(rawdata);
        console.log(student);
    }

    this.write = function() {
        const fs = require('fs');

        let student = {
            name: 'Mike',
            age: 23,
            gender: 'Male',
            department: 'English',
            car: 'Honda'
        };

        let data = JSON.stringify(student);
        fs.writeFileSync('student-2.json', data);
    }
}
module.exports = file;