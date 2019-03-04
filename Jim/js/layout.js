var email = document.getElementById('email').value;
var password = document.getElementById('password').value;

var login_credentials = new Object();
login_credentials.email = email;
login_credentials.password = password;

var credentials_json = JSON.stringify(login_credentials);
