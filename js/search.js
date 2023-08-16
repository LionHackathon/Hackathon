const pageMapping = {
    '카카오톡': 'kakaotalk.html',
    '배달의민족': 'dilivery.html',
    '마이페이지': 'mypage.html'
};

function handleKeyPress(event) {
    if (event.keyCode === 13) { // 엔터 키의 keyCode는 13
        navigateToPage();
    }
}

function navigateToPage() {
    const searchInput = document.getElementById('searchinput').value;

    let matchedPage = null;
    for (const keyword in pageMapping) {
        if (keyword.toLowerCase().includes(searchInput)) {
            matchedPage = pageMapping[keyword];
            break;
        }
    }

    if (matchedPage) {
        window.location.href = matchedPage;
    } else {
        alert('검색 결과가 없습니다.');
    }
}
document.getElementById('searchinput').addEventListener('keydown', handleKeyPress);
