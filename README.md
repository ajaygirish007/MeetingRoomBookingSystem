# Meeting Room Booking System

This is a Meeting Room Booking System built using Flask, HTML, CSS, and JavaScript by Ajay Girish(1KS20CS120),ajaygirish72@gmail.com.

## Instructions

### Prerequisites

Make sure you have Python and Flask installed on your system.

### Running the Application

1. Clone or download this repository to your local machine.

2. Navigate to the project directory in your terminal.

3. Run the following command to start the Flask application:

    ```
    python app.py
    ```

4. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the application.

### Usage

- **Login**: You will be directed to the login page upon accessing the application. Enter the *username:admin* and *password:password* to log in.

- **Booking a Room**: After logging in, you can book a room by entering the room ID, date, duration, and your name. Click the "Book Room" button to make a booking.
    -> As given in the code, the *room_ID* can either be *Room1/Room2*
    -> And the rest of the information is left to the user.

- **Logout**: You can log out by clicking on the "Logout" button. But instead of going to this link, http://localhost:5000, if you click ont the link appearing in the terminal, then for logout you have to update the url in the search bar as http://127.0.0.1:5000/logout.

## File Structure

- **app.py**: Flask application file containing the routes and configurations.
- **MeetingRoomBookingSystem.py.**: For testing the logic of the code

- **templates/**: Folder containing HTML templates.
  - **index.html**: Main page for booking rooms and viewing bookings.
  - **login.html**: Login page.
  - **logout.html**: Logout page.

- **static/**: Folder containing static files (CSS and JavaScript).
  - **styles.css**: CSS styles.
  - **script.js**: JavaScript code for client-side functionality.
  - **login.js**: JavaScript code for login functionality.
