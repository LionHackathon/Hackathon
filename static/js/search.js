const dictionary = {
    '카카오톡': 'kakaotalk.html',
    '배달의민족': 'dilivery.html',
    '앱 설치':'app.html',
    '기차표 예매': 'train.html',
    '카카오택시': 'taxi.html',
    '삼성페이': 'samsungpay.html',
    '네이버지도': 'map.html',
    '당근마켓': 'carrot.html',
    '쿠팡': 'coupang.html'
};

function handleKeyPress(event) {
  if (event.keyCode === 13) {
    navigateToPage();
  }
}


function updateSearchResults() {
  const searchInput = document.getElementById("searchinput").value;
  const searchResultsContainer = document.getElementById("searchResults");
  searchResultsContainer.innerHTML = ""; // 기존 결과 지움

  if (searchInput.trim() === "") {
      return; // 검색어가 비어있으면 결과 표시하지 않음
  }

  const matchedWords = Object.keys(dictionary).filter(word => word.includes(searchInput));
  
  if (matchedWords.length > 0) {
      const resultList = document.createElement("ul");
      resultList.style.padding = "0"; //목록 간격 줌
      matchedWords.forEach(word => {
          const listItem = document.createElement("li");
          listItem.textContent = word;
          listItem.onclick = function() {
              document.getElementById("searchinput").value = word; // 단어 클릭 시 입력란에 반영 ㅠㅠㅠㅠㅠㅠㅠㅠ
              searchResultsContainer.innerHTML = ""; 
          };
          resultList.appendChild(listItem);
      });
      searchResultsContainer.appendChild(resultList);
  }
}

/*검색 기능*/
function navigateToPage() {
    const searchInput = document.getElementById("searchinput").value;
    const matchedWord = dictionary[searchInput];
    
    if (matchedWord) {
        window.location.href = matchedWord;
    } else {
        alert("검색어를 다시 입력해주세요");
    }
}

/*찜 하기*/
document.getElementById("searchinput").addEventListener("keydown", handleKeyPress);

document.addEventListener("DOMContentLoaded", function () {
  const toggleHeartButtons = document.querySelectorAll(".toggleheart");

  toggleHeartButtons.forEach((button) => {
    const heartIcon = button.querySelector(".hearticon");
    let isFilled = false;

    button.addEventListener("click", function () {
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

/*글씨 강조*/
const hoverWait = document.querySelector(".hover_wait");

hoverWait.addEventListener("mouseover", () => {
  hoverWait.style.color = "red";
  hoverWait.style.fontSize = "53px";
});

hoverWait.addEventListener("mouseout", () => {
  hoverWait.style.color = "black";
  hoverWait.style.fontSize = "35px";
});


