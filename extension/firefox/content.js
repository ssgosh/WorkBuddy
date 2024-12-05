function redirectToBlockPage() {
  // window.location.href = 'https://www.example.com/block-page.html';
  window.location.href = chrome.runtime.getURL('block-page.html');
}

redirectToBlockPage();
