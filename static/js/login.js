document.getElementById("kakaoLoginButton").addEventListener("click", function() {
    // Django 서버로 API 요청 보내기
    fetch("http://localhost:8000/oauth/user/kakao/login")
        .then(response => response.json())
        .then(data => {
            // 요청이 성공했을 때 실행되는 부분
            console.log("서버 응답:", data);
            // 응답 처리 코드를 추가하세요
        })
        .catch(error => {
            // 요청이 실패했을 때 실행되는 부분
            console.error("오류 발생:", error);
            // 오류 처리 코드를 추가하세요
        });
});



//signin
document.getElementById("loginButton").addEventListener("click", function() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // 아이디와 비밀번호를 Django 서버로 전송
    var data = {
        username: username,
        password: password
    };

    fetch("http://127.0.0.1:8000/user/user/signin:", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // 서버 응답 처리
        console.log("서버 응답:", data);
    })
    .catch(error => {
        console.error("오류 발생:", error);
    });
});


