document.addEventListener('DOMContentLoaded', async () => {
    const newsList = document.getElementById('news-list');
    newsList.innerHTML = '<p class="text-gray-500">Loading latest legal news...</p>';
    try {
        const response = await fetch('/api/latest-news');
        if (!response.ok) throw new Error('Failed to fetch news');
        const data = await response.json();
        if (data.articles && data.articles.length > 0) {
            newsList.innerHTML = data.articles.map(article => `
                <div class="card p-6 bg-gradient-to-br from-blue-50 to-blue-100 rounded-2xl shadow-xl border border-blue-200 flex flex-col justify-between h-full transition-transform hover:scale-105 hover:shadow-2xl duration-200">
                    <a href="${article.url}" target="_blank" class="text-2xl font-extrabold text-blue-800 hover:text-blue-600 hover:underline block mb-2 leading-tight line-clamp-2">${article.title}</a>
                    <p class="text-gray-700 mt-2 text-base line-clamp-3">${article.description || ''}</p>
                    <div class="flex items-center mt-4">
                        <span class="inline-block bg-blue-200 text-blue-800 text-xs px-3 py-1 rounded-full font-semibold mr-2">${article.source || 'Unknown'}</span>
                        <svg class="w-4 h-4 text-blue-400 ml-auto" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
                    </div>
                </div>
            `).join('');
        } else {
            newsList.innerHTML = '<p class="text-gray-500">No news found.</p>';
        }
    } catch (err) {
        newsList.innerHTML = '<p class="text-red-500">Failed to load news. Please try again later.</p>';
    }
});
