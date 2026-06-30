async function login() {

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const role = document.getElementById("role").value;

  const res = await fetch("http://127.0.0.1:8000/api/v1/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password, role })
  });

  const data = await res.json();

  if (data.token) {

    localStorage.setItem("token", data.token);
    localStorage.setItem("role", role);

    window.location.href = "dashboard.html";

  } else {
    alert("Login failed");
  }
}