// const blockPageData = JSON.parse();
const blockPageData = localStorage.getItem('blockPageData');

console.log('Block Page Data:', blockPageData);
if (blockPageData) {
    document.getElementById('category').innerText = blockPageData.category;
    document.getElementById('explanation').innerText = blockPageData.explanation;
    document.getElementById('page_title').innerText = blockPageData.page_title;
    document.getElementById('page_url').innerText = blockPageData.page_url;
} else {
    console.error('No data found in local storage');
}
// Listen for the message sent from the content script
// chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
//   console.log(message);
//   console.log("Category: ", message.category);
//   console.log("Explanation: ", message.explanation);
//   console.log("Page Title: ", message.page_title);
//   console.log("Page URL: ", message.page_url);
//   document.getElementById('category').innerText = message.category;
//   document.getElementById('explanation').innerText = message.explanation;
//   document.getElementById('page_title').innerText = message.page_title;
//   document.getElementById('page_url').innerText = message.page_url;
//   sendResponse({ status: "done", text: message });
// });
