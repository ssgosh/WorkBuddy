// Function to send POST request
async function classifyPage(data) {
    console.log('Calling classifyPage with data:', data);
    try {
        const response = await fetch('http://localhost:5000/classify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        // Get the response and parse it
        const result = await response.json();
        console.log('Result:', result, typeof result);
        const res1 = JSON.parse(result);
        console.log('Category:', res1.category);
        console.log('Explanation:', res1.explanation);

        if (res1.category === 'non-work') {
            console.log('Category is non-work, hence blocking');
            // window.location.href = chrome.runtime.getURL('block-page.html');
            // document.getElementById('category').innerText = res1.category;
            // document.getElementById('explanation').innerText = res1.explanation;
            // // Also update the block-page.html with the page title and URL
            // document.getElementById('page_title').innerText = pageTitle;
            // document.getElementById('page_url').innerText = pageURL;

            // Store the result in local storage
            localStorage.setItem('blockPageData', JSON.stringify({
                category: res1.category,
                explanation: res1.explanation,
                page_title: data.page_title,
                page_url: data.page_url
            }));
            window.location.href = chrome.runtime.getURL('block-page.html');

            // chrome.runtime.sendMessage({
            //     category: result.category,
            //     explanation: result.explanation,
            //     page_title: data.page_title,
            //     page_url: data.page_url
            // }, function (response) {
            //     console.log("Within sendMessage callback");
            //     console.log(response);
            //     // window.location.href = chrome.runtime.getURL('block-page.html');
            // });
        } else {
            console.log('Category is work, hence not blocking');
        }

        // Return the category and explanation
        return res1;

    } catch (error) {
        console.error('Error:', error);
    }
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
});


// Call the function with the data
// classifyPage(data);
