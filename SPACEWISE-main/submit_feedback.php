<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $email = $_POST['email'];
    $feedback = $_POST['feedback'];
    
    // Set recipient email address
    $to = "Khyatisoni1102@gmail.com";

    // Set email subject
    $subject = "Feedback Received";

    // Set email message
    $message = "Feedback received from: $email\n\n";
    $message .= "Feedback:\n$feedback";

    // Set headers
    $headers = "From: $email" . "\r\n" .
               "Reply-To: $email" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();

    // Send email
    if (mail($to, $subject, $message, $headers)) {
        echo "Thank you for your feedback!";
    } else {
        echo "Sorry, there was an error sending your feedback.";
    }
} else {
    // Redirect back to the form if accessed directly
    header("Location: feedback_form.html");
    exit;
}
?>
