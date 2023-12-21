// app.js
async function generateResponse() {
    const link = document.getElementById("link").value; // Get the link from the input field
    const formData = new FormData();
    formData.append("link", link); // Append the link to the form data

    try {
        const response = await fetch("/generate_response", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.text();
        document.getElementById("response").innerHTML = data; // Use innerHTML to render HTML content
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("response").innerText = "An error occurred.";
    }
}

