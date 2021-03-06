$(document).ready(function(){

	var loginButton = $("#login-button");
	var registerButton = $("#register-button");
	
	loginButton.on("click", function(){
		username = $("#username").val();
		password = $("#password").val();
		$.ajax({
			url: "/api/login",
			method: "POST",
			data:{"username": username, "password": password},
			complete: function(data){
				token = JSON.parse(data.responseText)["token"]
				if ( token != undefined ) {
					localStorage.setItem("sessionJWT", token)
					alert("Logged In")
				} else {
					alert("Invalid Credentials")
				}
			}
		})
	})

	registerButton.on("click", function(){
		username = $("#username").val();
		password = $("#password").val();
		$.ajax({
			url: "/api/register",
			method: "POST",
			data:{"username": username, "password": password},
			complete: function(data){
				if (data.status != 204) {
					alert("Error: " + data.status + " " + data.responseText)
				} else {
					alert("Success: " + data.status)
				}
			}
		})
	})
})