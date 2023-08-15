/* const pageMapping = {
    '카카오톡': 'https://www.coupang.com',
    '배달의민족': 'https://www.baemin.com',
    '마이페이지': 'mypage.html'
};


function navigateToPage() {
    const searchInput = document.getElementById('searchInput').value.toLowerCase();

    let matchedPage = null;
    for (const keyword in pageMapping) {
        if (searchInput.includes(keyword.toLowerCase())) {
            matchedPage = pageMapping[keyword];
            break;
        }
    }

    if (matchedPage) {
        window.location.href = matchedPage;
    } else {
        alert('검색 결과가 없습니다.');
    }
}*/

const videoId = 'https://www.youtube.com/watch?v=1Gf6KbR5rfc';
        
        function generateYouTubeURL(videoId) {
            return `https://www.youtube.com/watch?v=${videoId}`;
        }

        function generateThumbnailURL(videoId) {
            return `https://img.youtube.com/vi/${videoId}/0.jpg`;
        }


        const youtubeButton = document.getElementById('youtubeButton');
        const thumbnailContainer = document.getElementById('thumbnailContainer');

        youtubeButton.addEventListener('click', function() {
            const youtubeURL = generateYouTubeURL(videoId);
            window.location.href = youtubeURL;

            const thumbnailURL = generateThumbnailURL(videoId);
            const thumbnailImage = document.createElement('img');
            thumbnailImage.src = thumbnailURL;
            thumbnailContainer.innerHTML = ''; 
            thumbnailContainer.appendChild(thumbnailImage);
        });