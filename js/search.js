const pageMapping = {
    '카카오톡': 'kakaotalk.html',
    '배달의민족': 'dilivery.html',
    '마이페이지': 'mypage.html'
};

function handleKeyPress(event) {
    if (event.keyCode === 13) { 
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

document.addEventListener("DOMContentLoaded", function() {
    const toggleHeartButtons = document.querySelectorAll(".toggleheart");

    toggleHeartButtons.forEach(button => {
        const heartIcon = button.querySelector(".hearticon");
        let isFilled = false;

        button.addEventListener("click", function() {
            if (isFilled) {
                heartIcon.src = "img/empty_heart.png";
                heartIcon.alt = "Empty Heart";
            } else {
                heartIcon.src = "img/filled_heart.png";
                heartIcon.alt = "Filled Heart";
            }
            isFilled = !isFilled;
        });
    });
});
