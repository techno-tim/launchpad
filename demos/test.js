// Vulnerability: SQL Injection
const username = getRequestParameter('username');
const password = getRequestParameter('password');

const sql = `SELECT * FROM users WHERE username='${username}' AND password='${password}'`;
db.query(sql, (err, result) => {
    if (err) {
        console.error('Error executing SQL query:', err);
        return;
    }

    if (result.length > 0) {
        console.log('Login successful');
    } else {
        console.log('Invalid username or password');
    }
});

// Bug: Infinite Loop
let i = 0;
while (i < 5) {
    console.log(i);
    // Missing increment statement
}