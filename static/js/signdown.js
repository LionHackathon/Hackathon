/* 백엔드 서버로 요청*/
const fetch = require("node-fetch"); // 혹은 다른 HTTP 요청 라이브러리 사용 가능

const userData = {
  username: "사용자명",
  email: "이메일",
  password: "비밀번호",
  passwordcheck: "비밀번호 확인",
  userId: "아이디",
};

const apiUrl = "http://127.0.0.1:8000/user/user/signup/";

// 회원가입 요청
async function signUpUser(userData) {
  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(userData),
    });

    if (response.ok) {
      const jsonResponse = await response.json();
      alert("회원가입 성공:", jsonResponse);
    } else {
      alert("회원가입 실패:", response.statusText);
    }
  } catch (error) {
    console.log("오류 발생:", error);
  }
}

// 회원가입 함수를 호출합니다.
signUpUser(userData);

/*회원가입 유효성검사*/
function formsubmit(event){
   event.preventDefault();
}
inputForm.addEventListener("submit",formsubmit);


window.onload = function () {
  var join = document.join; //form데이터를 모두 join변수에 저장

  // 유효성검사할 부분을 class로 부여했기에 check class 태그를 모두 input에 저장 가져옴
  // 이때 input 한 태그당 배열 인덱스로 받는다.
  var input = document.querySelectorAll(".check");

  // 오류 문구 //errorId : span의 id들(각 요소마다 나타낼 오류를 표시하기 위함)
  // error : class list의 하위 span을 모두 불러냄(일괄 처리를 위함 - 반복문)
  var errorId = [
    "idError",
    "pwError",
    "pwCheckError",
    "nameError",
    "phoneNumError",
    "emailError",
  ];
  var error = document.querySelectorAll(".list > span");

  // 오류문구 초기화 메서드
  // 오류 표시 후, 사용자가 올바르게 수정을 하면 텍스트가 사라지는 모습을 구현
  function innerReset(error) {
    for (var i = 0; i < error.length; i++) {
      error[i].innerHTML = "";
    }
  }

  // 초기화 메서드 호출
  innerReset(error);

  // [ ID 입력문자 유효성검사 ]
  join.id.onkeydown = function () {
    innerReset(error); // 초기화 메서드 호출
    var idLimit = /^[a-zA-Z0-9-_]{5,20}$/; //정규식 5~20자 (a~z, A~Z, 0~9, -, _만 입력가능)
    if (!idLimit.test(input[0].value)) {
      //입력값과 정규식 범위와 같지 않다면
      // id의 오류 문구삽입
      document.getElementById(errorId[0]).innerHTML =
        "5~20자의 영문 소대문자, 숫자와 특수기호(_),(-)만 사용 가능합니다.";
    }
  };

  // [ PW 입력문자 유효성검사 ]
  join.pw.onkeydown = function () {
    innerReset(error);
    var pwLimit = /^[a-zA-Z0-9~!@#$%^&*()_-]{10,20}$/;
    if (!pwLimit.test(input[1].value)) {
      // pw의 오류 문구삽입
      document.getElementById(errorId[1]).innerHTML =
        " 10~20자의 영문 소대문자, 숫자와 특수기호 '~!@#$%^&*()_-'만 사용 가능합니다.";
    }
  };
  // [ PW 재확인 입력문자 초기화 ]
  //비밀번호 동일여부는 submit 버튼 클릭시 검사해줄 예정
  join.pwCheck.onkeydown = function () {
    // pw의 오류 문구삽입
    innerReset(error); // 오류문구 초기화
  };

  // [ 이메일 입력 유효성검사 ]
  join.email.onkeydown = function () {
    innerReset(error); //
    var emailLimit = /[0-9a-zA-Z-_.]/;
    if (!emailLimit.test(input[5].value)) {
      // 이메일의 오류 문구삽입
      document.getElementById(errorId[5]).innerHTML =
        " 올바른 형식이 아닙니다. 영문,숫자, (-)(_)(.) 입력만 가능합니다.";
    }
  };
};
join.onsubmit = function () {
  //join에서 submit이 실행된다면 수행할 함수
  var errorStr = [
    " 아이디를",
    " 비밀번호를",
    " 비밀번호 확인을",
    " 성함을",
    " 휴대폰번호를",
    " 이메일을",
  ];

  innerReset(error); // 오류문구 초기화

  // [ input 공백확인 ]
  for (var i = 0; i < input.length - 1; i++) {
    // -1 == submit제외
    if (!input[i].value) {
      document.getElementById(errorId[i]).innerHTML =
        errorStr[i] + " 입력해 주세요.";
      input[i].focus(); // 포커스 이동
      return false;
    }
  }

  const REGPASSSWORD =
    /(?=.*\d{1,50})(?=.*[~`!@#$%\^&*()-+=]{1,50})(?=.*[a-zA-Z]{2,50}).{8,20}$/;


  /*유효성검사) 비밀번호 재확인
         if (join.pw.value != join.pwCheck.value) {
            document.getElementById("pwCheckError").innerHTML = " 비밀번호가 일치하지 않습니다.";
            join.pwCheck.focus(); // 포커스 이동
            return false;
         }*/


  

  // [ ID 유효성검사 ]
  const REGID = /^[a-z]+[a-z0-9]{5,19}$/g;

  function idCheck(){
      if(!REGID.test(idInput.value)){
         idError.style.display= 'unset'
        }else(idError.style.display= 'none')};
  
   idInput.addEventListener("keyup",idCheck);

  // [ PW 유효성검사 ]
  if (!pwLimit.test(input[1].value)) {
    document.getElementById(errorId[1]).innerHTML =
      " 10~20자의 영문 소대문자, 숫자와 특수기호 '~!@#$%^&*()_-'만 사용 가능합니다.";
    //console.log(input[1].value);
    //console.log(pwLimit.test(input[1].value));
    join.pw.focus(); // 포커스 이동
    return false;
  }

  function passwordCheck() {
   if (
     passwordInputBox.value.length < 8 ||
     passwordInputBox.value.length > 20
   ) {
     passwordError.style.display = "unset";
     passwordError.innerHTML = "8이상 20자 이내로 입력해주세요";
   } else if (!REGPASSSWORD.test(passwordInputBox.value)) {
     passwordError.style.display = "unset";
     passwordError.innerHTML = "비밀번호는 문자, 숫자,특수문자 포함입니다";
   } else {
     passwordError.style.display = "none";
   }
 }
 passwordInputBox.addEventListener("keyup", passwordCheck);

  // [ email 아이디 유효성검사 ]
  if (!emailLimit.test(input[5].value)) {
    document.getElementById(errorId[5]).innerHTML =
      " 올바른 형식이 아닙니다. 영문,숫자, (-)(_)(.) 외 입력은 불가합니다.";
    join.email.focus(); // 포커스 이동
    return false;
  }

  // [ email 주소선택 유효성검사 ]
  if (document.getElementById("mail_Select").value == "이메일 선택") {
    document.getElementById(errorId[5]).innerHTML = " 이메일을 선택해주세요.";
    return false;
  }
  //console.log(document.getElementById("mail_Select").value);
};
