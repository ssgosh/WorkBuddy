// Function to send POST request
async function classifyPage(data) {
    console.log('Calling classifyPage with data:', data);
    // try {
        const response = await fetch('http://localhost:5000/classify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Get the response and parse it
        const result = await response.json();
        console.log('Category:', result.category);
        console.log('Explanation:', result.explanation);

        // Here you can handle the response further as needed
    // } catch (error) {
    //     console.error('Error:', error);
    // }
}

document.addEventListener('DOMContentLoaded', (event) => {
    console.log('Page has fully loaded');
    // Extract page title, URL, and content
    const pageTitle = document.title;
    const pageURL = window.location.href;
    // const pageContent = document.body.innerText; // or use other methods for more refined content extraction

    // Create a JSON object with the extracted information
    const data = {
        page_title: pageTitle,
        page_url: pageURL
        // page_content: pageContent
    };

    console.log('Title:', pageTitle);
    console.log('URL:', pageURL);
    // console.log('Content:', pageContent);
    console.log('Data:', data);

    // Call the function with the data
    console.log('Calling the function classifyPage');
    classifyPage(data);
    //   window.location.href = chrome.runtime.getURL('block-page.html');
});


// Call the function with the data
// classifyPage(data);
