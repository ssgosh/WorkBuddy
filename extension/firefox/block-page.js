browser.storage.local.get('blockPageData').then((result) => {
    if (result.blockPageData) {
        document.getElementById('category').innerText = result.blockPageData.category;
        document.getElementById('explanation').innerText = result.blockPageData.explanation;
        document.getElementById('page_title').innerText = result.blockPageData.page_title;
        document.getElementById('page_url').innerText = result.blockPageData.page_url;
    } else {
        console.error('No data found in browser.storage.local');
    }
});
