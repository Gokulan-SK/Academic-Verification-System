

document.getElementById("studentForm").addEventListener("submit", function(event) {
    // Prevent the form from submitting by default
    event.preventDefault();
    
    // Get form fields
    var enrollmentDate = document.getElementById("enrollment_date").value;
    var graduationDate = document.getElementById("graduation_date").value;

    // Check if enrollment date is after or equal to graduation date
    if (new Date(enrollmentDate) > new Date(graduationDate)) {
        // Display an error message or alert
        alert("Graduation date should not be before the enrollment date.");
        return; // Stop form submission
    }
    
    // Close the success message if it exists

    // If validation passes, submit the form
    this.submit();
});
