$(document).ready(function() {
    // Listen for form messages
    var formMessage = "{% if messages %}{% for message in messages %}{{ message }}{% endfor %}{% endif %}";

    // Check if a message exists
    if (formMessage.trim() !== "") {
        // Display the message in the pop-up
        $("#notification-message").text(formMessage);
        $("#popup-notification").fadeIn();

        // Close the pop-up when the "Close" button is clicked
        $("#close-notification").click(function() {
            $("#popup-notification").fadeOut();
        });
    }
});