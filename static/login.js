function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    var loginStatus = document.getElementById("loginStatus");

    // Validation
    if (!username || !password) {
        loginStatus.innerText = "Please enter username and password.";
        return;
    }

    // Send login credentials to server (AJAX call)
    // Replace this with actual AJAX call to server-side authentication logic

    // Simulated success response
    if (username === "admin" && password === "password") {
        // Redirect to the booking page on successful login
        window.location.href = "/booking";
    } else {
        loginStatus.innerText = "Invalid username or password.";
    }
}
