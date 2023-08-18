document.getElementById("loginButton").addEventListener("click", function() {
    // Django ������ API ��û ������
    fetch("http://127.0.0.1:8000/user/user/signin:")
        .then(response => response.json())
        .then(data => {
            // ��û�� �������� �� ����Ǵ� �κ�
            console.log("���� ����:", data);
            // ���� ó�� �ڵ带 �߰��ϼ���
        })
        .catch(error => {
            // ��û�� �������� �� ����Ǵ� �κ�
            console.error("���� �߻�:", error);
            // ���� ó�� �ڵ带 �߰��ϼ���
        });
});