let loginData;

(function () {
    let url = 'accounts.json';
    console.log(url)

    fetch(url)
        .then((response) => response.text()
            .then((text) => {
                loginData = JSON.parse(text);
            }));

    document.getElementById('login-button').addEventListener('click', (ev) => {
        ev.preventDefault();

        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;

        loginData.forEach(element => {
            console.log(element);
            if (username == element.Username) {
                if (password == element.Password) {
                    window.location = "https://www.google.com";
                } else {
                    console.log("failure");
                }
            } else {
                console.log("failure")
            }
        });
    });        
})();

