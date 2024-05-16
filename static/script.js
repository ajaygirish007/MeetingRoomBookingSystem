function bookRoom() {
    var roomId = document.getElementById("roomId").value;
    var dateTime = document.getElementById("dateTime").value;
    var duration = document.getElementById("duration").value;
    var userName = document.getElementById("userName").value;

    var bookingStatus = document.getElementById("bookingStatus");

    // Validation
    if (!roomId || !dateTime || !duration || !userName) {
        bookingStatus.innerText = "Please fill in all fields.";
        return;
    }

    // Send booking request to server (AJAX call)
    // Replace this with actual AJAX call to server-side script

    // Simulated success response
    bookingStatus.innerText = "Room booked successfully!";
    window.location.href = '/logout';
}
